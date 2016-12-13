import xbmcaddon

__addonname__ = 'script.hyperion'
__addon__ = xbmcaddon.Addon(__addonname__)
__addonversion__ = __addon__.getAddonInfo('version')
__addonid__ = __addon__.getAddonInfo('id')
__cwd__ = __addon__.getAddonInfo('path')

'''

import os
import sys
import xbmc
import xbmcaddon


# Add the library path before loading Hyperion
__addon__ = xbmcaddon.Addon()
__cwd__ = __addon__.getAddonInfo('path')
sys.path.append(xbmc.translatePath(os.path.join(__cwd__, 'resources', 'lib')))

if __name__ == '__main__':
    import misc
    from settings import Settings
    from state import DisconnectedState

    # read settings
    settings = Settings()

    misc.log('%(settings)s', settings=settings.__dict__)

    # initialize the state
    state = DisconnectedState(settings)

    # start looping
    while not settings.abort:
        # execute the current state
        next_state = state.execute()

        # delete the old state if necessary
        if state != next_state:
            del state

        # advance to the next state
        state = next_state

    # clean up the state closing the connection if present
    del state
    del settings
'''
