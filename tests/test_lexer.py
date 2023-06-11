import unittest
from tsparxer.lexer import build_lexer
from ply.lex import Lexer, LexToken
from typing import Tuple, TypedDict


class TestLexer(unittest.TestCase):
    """
    Testing the lexer implementation.
    """

    # define the TestCase TypedDict for representing test cases
    TestCase = TypedDict("TestCase", {"type": str, "value": str})

    def setUp(self) -> None:
        """
        Set up the test case by initializing the lexer.
        """
        self.lexer: Lexer = build_lexer()

    def run_test(self, data: str, expected: Tuple[TestCase]) -> None:
        """
        Run a test case with the given input data and expected tokens.

        :param data: The input string to be tokenized.
        :param expected: A tuple of expected tokens in the TestCase format.
        """
        # Tokenize the input data
        self.lexer.input(data)
        tokens: Tuple[LexToken] = tuple(iter(self.lexer.token, None))

        # check if number of tokens match expected count
        self.assertEqual(len(expected), len(tokens), "Token count mismatch")

        # compare each token with the expected token
        for test, given in zip(expected, tokens):
            self.assertEqual(test["type"], given.type)
            self.assertEqual(test["value"], given.value)

    # -------------------------------------------------------------------------
    # Tests
    # -------------------------------------------------------------------------
    def test_lex_var_declarations(self) -> None:
        self.run_test(
            data=r'let message: string = "Hello, World!";',
            expected=(
                {"type": "LET", "value": "let"},
                {"type": "ID", "value": "message"},
                {"type": "COLON", "value": ":"},
                {"type": "STRING", "value": "string"},
                {"type": "EQUALS", "value": "="},
                {"type": "STRINGCONTENT", "value": '"Hello, World!"'},
                {"type": "SEMICOLON", "value": ";"},
            ),
        )


if __name__ == "__main__":
    unittest.main()
