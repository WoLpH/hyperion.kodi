'''
Kodi video capturer for Hyperion

Copyright (c) 2013-2016 Hyperion Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import xbmc
import xbmcaddon

import abc
from hyperion.Hyperion import Hyperion
from misc import log
from misc import notify


class BaseState(object):
    '''Base state object, meant to be subclassed'''
    __metaclass__ = abc.ABCMeta

    def __init__(self, settings):
        '''
        State object.

        Args:
            settings (Settings): Settings structure
        '''
        log('Entering %(name)s state', self._class__.__name__.lower())
        self._settings = settings

    @abc.abstractmethod
    def execute(self):
        raise NotImplementedError()


class DisconnectedState(BaseState):
    '''Default state class when disconnected from the Hyperion server '''

    def execute(self):
        '''
        Execute the state

        Returns:
            BaseState: The new state to execute
        '''
        # check if we are enabled
        if not self._settings.grabbing():
            xbmc.sleep(500)
            return self

        # we are enabled and want to advance to the connected state
        try:
            nextState = ConnectedState(self._settings)
            return nextState
        except Exception as exception:
            # unable to connect. notify and go to the error state
            if self._settings.showErrorMessage:
                notify(xbmcaddon.Addon().getLocalizedString(32100))
                self._settings.showErrorMessage = False

            # continue in the error state
            return ErrorState(self._settings, exception)


class ConnectedState(BaseState):
    '''
    State class when connected to Hyperion and grabbing video
    '''

    def __init__(self, settings):
        BaseState.__init__(self, settings)

        self._hyperion = None
        self._capture = None
        self._captureState = None
        self._data = None
        self._useLegacyApi = None

        # try to connect to hyperion
        self._hyperion = Hyperion(
            self._settings.address,
            self._settings.port)

        # create the capture object
        self._capture = xbmc.RenderCapture()
        self._capture.capture(
            self._settings.capture_width,
            self._settings.capture_height)

    def __del__(self):
        '''Destructor'''
        del self._hyperion
        del self._capture
        del self._captureState
        del self._data
        del self._useLegacyApi

    def useLegacyApi(self):
        '''check the xbmc API Version'''
        if self._usageLegacyApi is None:
            try:
                self._capture.getCaptureState()
                self._useLegacyApi = True
            except Exception:
                self._useLegacyApi = False

        return self._useLegacyApi

    def getData(self):
        '''capture an image'''
        data = None
        if self.useLegacyApi():
            self._capture.waitForCaptureStateChangeEvent(200)
            self._captureState = self._capture.getCaptureState()
            if self._captureState == xbmc.CAPTURE_STATE_DONE:
                data = self._capture.getImage()
        else:
            data = self._capture.getImage()

        # retrieve image data and reformat into rgb format
        if self._capture.getImageFormat() == 'ARGB':
            del data[0::4]
        elif self._capture.getImageFormat() == 'BGRA':
            del data[3::4]
            data[0::3], data[2::3] = data[2::3], data[0::3]

        return str(data)

    def execute(self):
        '''Execute the state
            - return: The new state to execute
        '''
        # check if we still need to grab
        if not self._settings.grabbing():
            # return to the disconnected state
            return DisconnectedState(self._settings)

        data = self.getData()
        if data:
            try:
                # send image to hyperion
                self._hyperion.sendImage(
                    self._capture.getWidth(),
                    self._capture.getHeight(),
                    data,
                    self._settings.priority,
                    500,
                )
            except Exception as exception:
                # unable to send image. notify and go to the error state
                notify(xbmcaddon.Addon().getLocalizedString(32101))
                return ErrorState(self._settings, exception)

        if self.useLegacyApi():
            if self._captureState != xbmc.CAPTURE_STATE_WORKING:
                # the current capture is processed or it has failed, we request
                # a new one
                self._capture.capture(
                    self._settings.capture_width,
                    self._settings.capture_height)

        # limit the maximum number of frames sent to hyperion
        xbmc.sleep(int(1. / self._settings.framerate * 1000))

        return self


class ErrorState(BaseState):
    '''State class which is activated upon an error'''

    def __init__(self, settings, exception):
        '''
        Error state object.

        Args:
            settings (Settings): Settings structure
            exception (Exception): The exception that caused this error
        '''
        BaseState.__init__(self, settings)
        self._exception = exception

    def execute(self):
        '''Execute the state
            - return: The new state to execute
        '''
        # take note of the current revision of the settings
        rev = self._settings.rev

        # stay in error state for the specified timeout or until the settings
        # have been changed
        for i in range(self._settings.timeout):
            if rev == self._settings.rev:
                break
            elif self._settings.abort:
                return self
            else:
                xbmc.sleep(1000)

        # continue in the disconnected state
        return DisconnectedState(self._settings)

