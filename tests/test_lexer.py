import zonpy.lexer as lexer
from zonpy.lexer import Token, TokenType


def test_empty():
    input = ".{}"
    expected = [".{", "}"]
    assert list(lexer.read(input)) == expected


def test_whitespace():
    input = ".{ }"
    expected = [".{", "}"]
    assert list(lexer.read(input)) == expected


def test_whitespace2():
    input = ".{\n}"
    expected = [".{", "}"]
    assert list(lexer.read(input)) == expected


def test_single_key():
    input = '.{.key = "value"}'
    expected = [".{", ".key", "=", '"value"', "}"]
    assert list(lexer.read(input)) == expected


def test_multiple_keys():
    input = '.{.key = "value", .key2 = "value2"}'
    expected = [".{", ".key", "=", '"value"', ",", ".key2", "=", '"value2"', "}"]
    assert list(lexer.read(input)) == expected


def test_nested():
    input = '.{.key = .{.key2 = "value"}}'
    expected = [".{", ".key", "=", ".{", ".key2", "=", '"value"', "}", "}"]
    assert list(lexer.read(input)) == expected


def test_raw_keys():
    input = '.{.@"raw-key" = "value"}'
    expected = [".{", '.@"raw-key"', "=", '"value"', "}"]
    assert list(lexer.read(input)) == expected

def test_list():
    input = '.{.key = .{ "one", "two", "three" }}'
    expected = [".{", ".key", "=", ".{", '"one"', ",", '"two"', ",", '"three"', "}", "}"]
    assert list(lexer.read(input)) == expected


def test_parse_tokens():
    input = '.{.key = "value",.@"raw-key" = 3.14}'
    expected = [
        Token(TokenType.LBRACE, ".{"),
        Token(TokenType.IDENTIFIER, ".key"),
        Token(TokenType.EQUALS, "="),
        Token(TokenType.STRING, '"value"'),
        Token(TokenType.COMMA, ","),
        Token(TokenType.IDENTIFIER, '.@"raw-key"'),
        Token(TokenType.EQUALS, "="),
        Token(TokenType.NUMBER, "3.14"),
        Token(TokenType.RBRACE, "}"),
    ]
    assert list(lexer.parse(lexer.read(input))) == expected


def test_resolve_value_tokens():
    input = [
        Token(TokenType.STRING, '"value"'),
        Token(TokenType.NUMBER, "42"),
        Token(TokenType.NUMBER, "3.14"),
        Token(TokenType.BOOLEAN, "true"),
        Token(TokenType.BOOLEAN, "false"),
        Token(TokenType.IDENTIFIER, ".identifier"),
        Token(TokenType.IDENTIFIER, '.@"raw-identifier"'),
    ]
    expected = [
        "value",
        42,
        3.14,
        True,
        False,
        "identifier",
        "raw-identifier",
    ]
    assert [token.resolve() for token in input] == expected
