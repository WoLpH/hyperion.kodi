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
    FORMAT = b'%(name)s: %(message)s'
    PRE_FORMAT = b'[%(id)s] %(FORMAT)s'

    def __init__(self):
        logging.StreamHandler.__init__(self)
        addon = xbmcaddon.Addon()

        params = dict(
            id=addon.getAddonInfo('id'),
            version=addon.getAddonInfo('version'),
            name=addon.getAddonInfo('name'),
            FORMAT=self.FORMAT,
        )

        self.setFormatter(logging.Formatter(self.PREFIX % params))

    def emit(self, record):
        if getSettingAsBool('debug'):
            try:
                xbmc.log(self.format(record), levels[record.levelno])
            except UnicodeEncodeError:
                xbmc.log(self.format(record).encode('utf-8', 'ignore'), levels[record.levelno])

    def flush(self):
        pass



def log(msg, format='### [%(addon)s] - %(msg)s', level=xbmc.LOGDEBUG,
        **kwargs):
    '''
    Write a debug message to the Kodi log

    Args:
        msg (str): The message itself
        format (str): The format of the log message
        level (int): The log level
    '''
    addon = xbmcaddon.Addon()

    kwargs['addon'] = addon.getAddonInfo('name')
    kwargs['msg'] = msg % kwargs

    xbmc.log(format % kwargs, level=level)


# LOGDEBUG = 0
def debug(msg, **kwargs):
    return log(msg, level=xbmc.LOGDEBUG, **kwargs)


# LOGINFO = 1
def info(msg, **kwargs):
    return log(msg, level=xbmc.LOGINFO, **kwargs)


# LOGNOTICE = 2
def notice(msg, **kwargs):
    return log(msg, level=xbmc.LOGNOTICE, **kwargs)


# LOGWARNING = 3
def warning(msg, **kwargs):
    return log(msg, level=xbmc.LOGWARNING, **kwargs)


# LOGERROR = 4
def error(msg, **kwargs):
    return log(msg, level=xbmc.LOGERROR, **kwargs)


# LOGSEVERE = 5
def severe(msg, **kwargs):
    return log(msg, level=xbmc.LOGSEVERE, **kwargs)


# LOGFATAL = 6
def fatal(msg, **kwargs):
    return log(msg, level=xbmc.LOGFATAL, **kwargs)


# LOGNONE = 7
def none(msg, **kwargs):
    return log(msg, level=xbmc.LOGNONE, **kwargs)


def notify(msg, **kwargs):
    '''Show a notification in Kodi
    '''
    log(msg, **kwargs)
    addon = xbmcaddon.Addon()
    xbmc.executebuiltin('XBMC.Notification(%s,%s,%s,%s)' % (
        addon.getAddonInfo('name'),
        msg % kwargs,
        10000,
        addon.getAddonInfo('icon')))

