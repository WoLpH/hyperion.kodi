# -*- coding: utf-8 -*-

import xbmc
from logger import logger
from addon import __addon__, __addonversion__, __addonid__, __cwd__
from settings import settings


__all__ = [
    '__addon__',
    '__addonversion__',
    '__addonid__',
    '__cwd__',
]


class Monitor(xbmc.Monitor):

    def __init__(self, settings, *args, **kwargs):
        self.settings = settings
        xbmc.Monitor.__init__(self, *args, **kwargs)

    def onSettingsChanged(self):
        logger.error('settings changed')
        settings.clear()
        # if not settings.reconnect:
        #     check_state()

    def onScreensaverDeactivated(self):
        logger.error('screensaver deactivated')
        settings.setScreensaver(False)

    def onScreensaverActivated(self):
        logger.error('screensaver activated')
        settings.setScreensaver(True)


class xPlayer(xbmc.Player):

    def __init__(self, settings=None, *args, **kwargs):
        logger.error('a settings: %r', settings)
        xbmc.Player.__init__(self, *args, **kwargs)
        logger.error('b settings: %r', settings)
        self.settings = settings
        self.playing = False
        self.capture = xbmc.RenderCapture()
        self.legacy_render_api = True

    def onPlayBackStopped(self):
        self.playing = False
        logger.error('stopped')

    def onPlayBackPaused(self):
        pass
        logger.error('paused')

    def onPlayBackEnded(self):
        self.playing = False
        logger.error('ended')

    def onPlayBackStarted(self):
        self.playing = True
        logger.error('started')

        if not self.legacy_render_api:
            self.capture.capture(capture_width, capture_height)



def main():
    logger.debug('Loading %r service version %r',
                 __addonid__, __addonversion__)

    monitor = Monitor(settings)
    logger.error('x settings: %r', settings)
    player = xPlayer()

    while not monitor.abortRequested():
        if monitor.waitForAbort(1):
            break

        logger.error('Whats up?')

    logger.debug('%r shutting down.', __addonid__)


if __name__ == '__main__':
    main()
