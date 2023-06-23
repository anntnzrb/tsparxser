import unittest
from ply.lex import LexToken

from tsparxer.lexer import Lexer as TSLexer
from tsparxer.parser import Parser as TSParser
from tsparxer.parser import ParserSyntaxError


class TestParser(unittest.TestCase):
    """
    Testing the parser implementation.
    """

    def setUp(self) -> None:
        """
        Set up the test case by initializing the lexer and parser.
        """
        self.lexer: TSLexer = TSLexer()
        self.parser: TSParser = TSParser(self.lexer)

    # -------------------------------------------------------------------------
    # Tests
    # -------------------------------------------------------------------------

    def test_valid_and_invalid_inputs(self) -> None:
        tests = [
            # valid
            ("let x = 5;", True),
            ("let y: number = 10;", True),
            (r'let z: string = "test";', True),
            (r"let z = 'test';", True),
            # invalid
            ("let x = 5", False),
            ("let x = ;", False),
            ("let y: unknown_type = 'test';", False),
            (r"let z: = 'test';", False),
            ("let", False),
        ]

        for data, valid in tests:
            if valid:
                self.parser.parse(data)
            else:
                with self.assertRaises(ParserSyntaxError):
                    self.parser.parse(data)


if __name__ == "__main__":
    unittest.main()
