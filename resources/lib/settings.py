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
import misc
import xbmc
import xbmcaddon


class MyMonitor(xbmc.Monitor):
    '''Class to capture changes in settings and screensaver state'''

    def __init__(self, settings):
        xbmc.Monitor.__init__(self)
        self._settings = settings
        self._settings.screensaver = xbmc.getCondVisibility(
            'System.ScreenSaverActive')
        self._settings.abort = xbmc.abortRequested

    def onAbortRequested(self):
        self._settings.abort = True
        return super(MyMonitor, self).onAbortRequested()

    def onSettingsChanged(self):
        self._settings.readSettings()
        return super(MyMonitor, self).onSettingsChanged()

    def onScreensaverDeactivated(self):
        self._settings.screensaver = False
        return super(MyMonitor, self).onScreensaverDeactivated()

    def onScreensaverActivated(self):
        self._settings.screensaver = True
        return super(MyMonitor, self).onScreensaverActivated()


class Settings:
    '''
    Class which contains all addon settings and xbmc state items of interest
    '''

    def __init__(self):
        '''Constructor
        '''
        self.rev = 0
        self._monitor = MyMonitor(self)
        self._player = xbmc.Player()
        self._debugging = False
        self.readSettings()

    def __del__(self):
        '''Destructor'''
        del self._monitor
        del self._player

    def readSettings(self):
        '''(Re-)read all settings'''
        misc.log('Reading settings')
        addon = xbmcaddon.Addon()
        self.enable = addon.getSetting('hyperion_enable') == 'true'
        self.enableScreensaver = addon.getSetting('screensaver_enable') == 'true'
        self.address = addon.getSetting('hyperion_host')
        self.port = int(addon.getSetting('hyperion_port'))
        self.priority = int(addon.getSetting('hyperion_priority'))
        self.timeout = int(addon.getSetting('reconnect_timeout'))
        self.capture_width = int(addon.getSetting('capture_width'))
        self.capture_height = int(addon.getSetting('capture_height'))
        self.framerate = int(addon.getSetting('framerate'))
        self.debug = addon.getSetting('debug') == 'true'
        self.debug_host = addon.getSetting('debug_host')
        self.debug_port = int(addon.getSetting('debug_port'))

        self.showErrorMessage = True
        self.rev += 1

        if self.debug:
            try:
                import pydevd

                pydevd.settrace(host=settings.debug_host, port=settings.debug_port,
                                stdoutToServer=True, stderrToServer=True)
                self._debugging = True
            except Exception as exception:
                misc.notify('Error while enabling debugger: %(exception)r',
                            exception=exception)
        elif self._debugging:
            import pydevd
            pydevd.stoptrace()
            self._debugging = False

    def grabbing(self):
        '''
        Check if we grabbing is requested based on the current state and
        settings
        '''
        return self.enable and self._player.isPlayingVideo() and (
            self.enableScreensaver or not self.screensaver)

