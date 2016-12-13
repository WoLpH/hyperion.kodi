import xbmc
import addon
import logging


LOGLEVELS = {
    logging.CRITICAL: xbmc.LOGFATAL,
    logging.ERROR: xbmc.LOGERROR,
    logging.WARNING: xbmc.LOGWARNING,
    logging.INFO: xbmc.LOGINFO,
    logging.DEBUG: xbmc.LOGDEBUG,
    logging.NOTSET: xbmc.LOGNONE,
}


class KodiLogHandler(logging.StreamHandler):
    FORMAT = b'[%(name)s] %(message)s'
    PRE_FORMAT = b'%(FORMAT)s'

    def __init__(self):
        logging.StreamHandler.__init__(self)

        params = dict(
            id=addon.__addonid__,
            name=addon.__addonname__,
            version=addon.__addonversion__,
            FORMAT=self.FORMAT,
        )

        self.setFormatter(logging.Formatter(self.PRE_FORMAT % params))

    def emit(self, record):
        level = LOGLEVELS.get(record.levelno, logging.DEBUG)
        message = self.format(record)

        try:
            xbmc.log(message, level)
        except UnicodeEncodeError:
            xbmc.log(message.encode('utf-8', 'ignore'), level)

    def flush(self):
        pass


logger = logging.getLogger(addon.__addonname__)
logger.addHandler(KodiLogHandler())
logger.setLevel(logging.DEBUG)
