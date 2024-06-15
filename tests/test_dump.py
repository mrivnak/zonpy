from zonpy import *


def test_dumps_empty():
    input = {}
    output = dumps(input)

    assert output == ".{}"


def test_dumps_single_key():
    input = {"key": "value"}
    output = dumps(input)

    assert output == """.{.key = "value"}"""


def test_dumps_multiple_keys():
    input = {"key1": "value1", "key2": "value2"}
    output = dumps(input)

    assert output == """.{.key1 = "value1", .key2 = "value2"}"""


def test_loads_nested_keys():
    input = {"key1": "value1", "key2": {"key3": "value3"}}
    output = dumps(input)

    assert output == """.{.key1 = "value1", .key2 = .{.key3 = "value3"}}"""
