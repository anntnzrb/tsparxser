import unittest
from ply.lex import LexToken
from typing import List, Tuple

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

    def run_test(self, tests: List[Tuple[str, bool]]) -> None:
        """
        Run a series of tests for the parser.

        :param tests: A list of tuples containing the test data and a boolean
         indicating if the test is valid or not.
        """
        for data, valid in tests:
            if valid:
                self.parser.parse(data)
            else:
                with self.assertRaises(ParserSyntaxError):
                    self.parser.parse(data)

    # -------------------------------------------------------------------------
    # Tests
    # -------------------------------------------------------------------------

    def test_parser_assignment(self) -> None:
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

        self.run_test(tests)

    # -----------------------------------------------------------------------------
    # Data Types
    # -----------------------------------------------------------------------------

    def test_parser_object(self) -> None:
        tests = [
            # valid
            ("interface Person { name: string; age: number;}", True),
            ("interface Animal { type: string; legs: boolean;}", True),
            ("interface Country { name: string; poblation: number;}", True),
            # invalid
            ("interface Person { }", False),
            ("Person { name: string; age: number; }", False),
            ("let Person { name: string; age: number; }", False),
        ]
        self.run_test(tests)

    # -----------------------------------------------------------------------------
    # Control Structures
    # -----------------------------------------------------------------------------

    def test_parser_if(self) -> None:
        tests = [
            # valid
            (r"if ( 8 > 5 && false ){ let foo = bar; }", True),
            (r"if ( true ){ let x = 1; }", True),
            (r'if ( " " ){ let y = "foo"; }', True),
            # invalid
            ("if ( !true ){ }", False),
            ("if ( 1 ){ }", False),
            ("if ( && ){ }", False),
        ]

        self.run_test(tests)

    def test_parser_while(self) -> None:
        tests = [
            # valid
            (r'while ( 9 > 32 && true ){ let c = "c"; }', True),
            (r"while ( foo ){ let n: number = 10; }", True),
            (r'while ( " " ){ let w = 11; }', True),
            # invalid
            ("while ( !true ){ }", False),
            ("while ( 1 ){ }", False),
            ("while ( && ){ }", False),
        ]

        self.run_test(tests)

    # -----------------------------------------------------------------------------
    # Function Declarations
    # -----------------------------------------------------------------------------

    def test_parser_function_dclr_var(self) -> None:
        tests = [
            # valid
            (
                "const multiply = function(a: number, b: number): number { let result = a * b; return result; };",
                True,
            ),
            (
                "const union = function(a: string, b: string) { let result = a + b; return result; };",
                True,
            ),
            # invalid
            (
                "const union = function(a: string, b: string): { let result = a + b; return result; };",
                False,
            ),
            (
                "const multiply = function(a: number, b: number): number { result = a * b; return result; };",
                False,
            ),
            (
                "const union = function(a: string, b: string): string { let result = a + b, return result; };",
                False,
            ),
        ]

        self.run_test(tests)

    def test_parser_function_dclr_keyword(self) -> None:
        tests = [
            # valid
            (
                "function multiply(a: number, b: number): number { let result = a * b; return result; }",
                True,
            ),
            (
                "function union(a: string, b: string) { let result = a + b; return result; }",
                True,
            ),
            # invalid
            (
                "function union(a: string, b: string): { let result = a + b; return result; }",
                False,
            ),
            (
                "function multiply(a: number, b: number): number { result = a * b; return result; }",
                False,
            ),
            (
                "function union(a: string, b: string): string { let result = a + b, return result; }",
                False,
            ),
        ]

        self.run_test(tests)

    def test_parser_function_dclr_arrow(self) -> None:
        tests = [
            # valid
            (
                "const multiply = (a: number, b: number): number => { let result = a * b; return result; }",
                True,
            ),
            (
                "const union = (a: string, b: string) => { let result = a + b; return result; }",
                True,
            ),
            # invalid
            (
                "const union = (a: string, b: string): => { let result = a + b; return result; }",
                False,
            ),
            (
                "const multiply = (a: number, b: number): number => { result = a * b; return result; }",
                False,
            ),
            (
                "const union = (a: string, b: string): string => { let result = a + b, return result; }",
                False,
            ),
        ]

        self.run_test(tests)


if __name__ == "__main__":
    unittest.main()
