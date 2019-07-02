import pytest

from mappers.exceptions import MapperException
from mappers.mappers import BaseMapper, Key


def test_plain_key():
    test_value = 42

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key('level1')

    test_mapper = TestMapper({'level1': test_value})
    assert test_mapper.test_value == test_value


def test_mapper_hierarchical_key():
    test_value = 42

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('level1', 'level2', 'level3', 'answer',))

    test_mapper = TestMapper({'level1': {'level2': {'level3': {'answer': test_value}}}})
    assert test_mapper.test_value == test_value


def test_required_key():
    test_value = 42

    class TestMapper(BaseMapper):
        _required_keys = ['test_value']
        not_test_value = Key('level1')
    with pytest.raises(MapperException, match=r".*Missing required field.*"):
        test_mapper = TestMapper({'level1': test_value})


def test_allow_setter():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), allow_setter=True)

    test_mapper = TestMapper({'answer': 1})
    test_mapper.test_value = test_value
    assert type(test_mapper.test_value) is str
    assert test_mapper.test_value == test_value


def test_default_with_value():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), default=5)

    test_mapper = TestMapper({'answer': test_value})
    assert test_mapper.test_value == test_value


def test_default_without_value():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), default=5)

    test_mapper = TestMapper({'reply': test_value})
    assert test_mapper.test_value == 5


def test_getter_type_cast():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), type_cast=int)

    test_mapper = TestMapper({'answer': test_value})
    assert type(test_mapper.test_value) is int
    assert type(test_mapper._data.get('answer')) is str
    assert test_mapper.test_value == int(test_value)


def test_setter_type_cast():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), type_cast=int, allow_setter=True)

    test_mapper = TestMapper({'answer': 1})
    test_mapper.test_value = test_value
    assert type(test_mapper.test_value) is int
    assert type(test_mapper._data.get('answer')) is int
    assert test_mapper.test_value == int(test_value)


def test_failed_type_cast():
    test_value = 'nah'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), type_cast=int)

    test_mapper = TestMapper({'answer': test_value})
    assert type(test_mapper.test_value) is str
