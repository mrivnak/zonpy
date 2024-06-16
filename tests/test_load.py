from zonpy import *


def test_loads_empty():
    input = ".{}"
    output = loads(input)

    assert output == {}


def test_loads_single_key():
    input = """.{.key = "value"}"""
    output = loads(input)

    assert output == {"key": "value"}


def test_loads_multiple_keys():
    input = """.{.key1 = "value1", .key2 = "value2"}"""
    output = loads(input)

    assert output == {"key1": "value1", "key2": "value2"}


def test_loads_nested_keys():
    input = """.{.key1 = "value1", .key2 = .{.key3 = "value3"}}"""
    output = loads(input)

    assert output == {"key1": "value1", "key2": {"key3": "value3"}}

def test_loads_list():
    input = """.{.key = .{ "one", "two", "three" }}"""
    output = loads(input)

    assert output == {"key": ["one", "two", "three"]}
