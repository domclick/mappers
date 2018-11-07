from mappers.mappers import BaseMapper, Key


def test_mapper_hierarchical_key():
    test_value = 42

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('level1', 'level2', 'level3', 'answer',))

    test_mapper = TestMapper({'level1': {'level2': {'level3': {'answer': test_value}}}})
    assert test_mapper.test_value == test_value


def test_value_type_cast():
    test_value = '42'

    class TestMapper(BaseMapper):
        _required_keys = []
        test_value = Key(('answer',), type_cast=int)

    test_mapper = TestMapper({'answer': test_value})
    assert type(test_mapper.test_value) is int
    assert test_mapper.test_value == int(test_value)
