import typing
import logging

logger = logging.getLogger('mappers')


def get_in(dct, keys, default=None):
    val = dct
    for key in keys[:-1]:
        if val is None:
            return
        val = val.get(key, {})
        if not isinstance(val, typing.Dict):
            logger.warning("path doesn't exists %s %s return default=%s",
                           keys, dct, default)
            return default

    val = val.get(keys[-1], default)
    return val


def set_in(dct, keys, value):
    val = dct
    keys = list(keys)
    if not keys:
        raise AttributeError('empty keys: %s' % keys)

    for key in keys[:-1]:
        val.setdefault(key, {})
        val = val.get(key)
    val[keys[-1]] = value