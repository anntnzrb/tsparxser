#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
test_parser.py: Parser testing.
"""

import unittest
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

    def test_parser_array(self) -> None:
        tests = [
            # valid
            ("let arr: number[] = [1,2,3,4];", True),
            (r"let arr: string[] = ['hello','world'];", True),
            ("let arr: number[] = [1];", True),
            # invalid
            ("arr: number[] = [1,2,3];", False),
            ("let arr: [] = [1,5]", False),
            ("let arr: number[] = [1,2,3,4]", False),
            (r"let arr: string] = ['hello','world'];", False),
            (r"let arr: string] = 'hello','world';", False),
        ]

        self.run_test(tests)

    def test_parser_tuple(self) -> None:
        tests = [
            # valid
            (r'let tup1: [string, number] = ["hello", 42];', True),
            (
                r'let tup3: [string, boolean, number] = ["example", true, 7];',
                True,
            ),
            #  invalid
            ("let tup5: [string, number];", False),
            (r'let tup2: [number] = "world";', False),
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
            (r'if ( " " ){ var y = "foo"; }', True),
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
            (r"while ( foo ){ var n: number = 10; }", True),
            (r'while ( " " ){ let w = 11; }', True),
            # invalid
            ("while ( !true ){ }", False),
            ("while ( 1 ){ }", False),
            ("while ( && ){ }", False),
        ]

        self.run_test(tests)

    def test_parser_for_loop(self) -> None:
        tests = [
            # valid
            (r"for(let index = 1;10<=index;index++){let foo = 'bar';}", True),
            (
                r"for(let index = 1;index>=5;index--){var n: number = 10;}",
                True,
            ),
            (
                r"for(let index = 1;variable<=index;index++){let foo = 'bar';}",
                True,
            ),
            (
                r"for(let index = 1;index>=5;++index){var n: number = 10;}",
                True,
            ),
            (
                r'for(let numero: number = 20; numero==100; numero++){var y = "foo";}',
                True,
            ),
            # invalid
            (r"for let index = 1;10<=index;index++){let foo = bar; }", False),
            (r"for (let index = 1,10<=index,index++){ let foo = bar;}", False),
            (r"for (let index = 1;index++){let foo = bar; }", False),
            (r"for(let index = 1;10<=index;index++)", False),
        ]

        self.run_test(tests)

    # -----------------------------------------------------------------------------
    # Function Declarations
    # -----------------------------------------------------------------------------

    def test_parser_function_decl_var(self) -> None:
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

    def test_parser_function_decl_keyword(self) -> None:
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

    def test_parser_function_decl_arrow(self) -> None:
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
