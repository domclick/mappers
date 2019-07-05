from datetime import datetime
from typing import Iterable

import logging 

from .exceptions import MapperException
from .utils import get_in, set_in

logger = logging.getLogger("mappers")

class Key(object):
    """ Key object is an alias to a dict key in multilevel structure."""

    def __init__(self, key, type_cast=None, allow_setter=False, default=None):
        self.key = key
        self.type_cast = type_cast
        if isinstance(self.key, Iterable) and not isinstance(self.key, str):
            self.key_path = list(self.key)
        else:
            self.key_path = [self.key, ]

        self.allow_setter = allow_setter
        self.default = default

    def __get__(self, obj, objtype):
        value = get_in(obj._data, self.key_path, self.default)
        if self.type_cast:
            try:
                value = self.type_cast(value)
            except:
                logger.warning(f"Key {self.key}: can't type cast {value} into {self.type_cast.__name__}")
        return value

    def __set__(self, obj, value):
        if not self.allow_setter:
            raise AttributeError("can't set %s" % self.key_path)

        if self.type_cast:
            try:
                value = self.type_cast(value)
            except:
                logger.warning(f"Key {self.key}: can't type cast {value} into {self.type_cast.__name__}")
                return

        set_in(obj._data, self.key_path, value)


class BaseMapper:
    """Mapper is a flat model class for abstracting away multilevel dict data"""

    _required_keys = []

    def __init__(self, data, **kwargs):
        data.update(kwargs)
        self._data = data
        for field in self._required_keys:
            if not hasattr(self, field):
                raise MapperException('Missing required field {}'.format(field))
