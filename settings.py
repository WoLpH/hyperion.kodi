import addon


class Undefined(object):
    pass


converters = dict()


def register(type):
    def _register(function):
        converters[type] = function
        return function
    return _register


class SettingsBase(object):
    converters = dict()
    types = dict()

    def __init__(self):
        self.clear()

    def __getattr__(self, key):
        return self.get(key)

    def get(self, key, default=Undefined):
        if key in self.cache:
            value = self.cache[key]
        else:
            raw_value = addon.__addon__.getSetting(key)
            type_ = self.types.get(key, str)
            converter = self.converters[type_]

            if default is Undefined:
                value = converter(raw_value)
            else:
                value = converter(raw_value, default)

            self.cache[key] = value

        return value

    def clear(self):
        self.cache = dict()

    def __setattr__(self, key, value):
        addon.__addon__.setSetting(key, str(value))

    @register(bool)
    def convert_bool(self, value, default=None):
        return value.lower() == 'true'

    @register(int)
    def convert_int(self, value, default=0):
        try:
            return int(value)
        except ValueError:
            return default

    @register(float)
    def convert_float(self, value, default=0.0):
        try:
            return int(value)
        except ValueError:
            return default

    @register(str)
    def convert_str(self, value, default=''):
        return value or default

    def items(self):
        items = []
        for key in self.types:
            items.append((key, self.get(key)))
            # yield key, self.get(key)
        return items

    def dict(self):
        return dict(self.items())

    def keys(self):
        return self.types.keys()

    def values(self):
        return map(self.get, self.types.keys())

    def __repr__(self):
        return repr({})
        return repr(self.dict())


class Settings(SettingsBase):
    types = dict(
        hyperion_enable=bool,
        screensaver_enable=bool,
        hyperion_host=str,
        hyperion_port=int,
        hyperion_priority=int,
        reconnect_timeout=int,
        capture_width=int,
        capture_height=int,
        framerate=int,
        debug=bool,
        debug_host=str,
        debug_port=int,
    )


settings = Settings()

