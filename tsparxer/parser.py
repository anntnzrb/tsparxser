#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
lexer.py: A lexer for tokenizing a TypeScript input.
"""

import ply.yacc as plyacc
from ply.yacc import YaccProduction
from typing import Tuple

from .lexer import Lexer as TSLexer


class ParserSyntaxError(Exception):
    def __init__(self, p: YaccProduction):
        super().__init__(f"Syntax error in input '{p}'!")


class Parser:
    tokens: Tuple[str] = TSLexer.tokens
    start = "program"

    # -----------------------------------------------------------------------------

    def p_program(self, p: YaccProduction) -> None:
        """
        program : statements
        """

    def p_statement(self, p: YaccProduction) -> None:
        """
        statement : assignment_var
                  | control_structure
                  | data_structure
                  | assignment_function
        """

    def p_statements(self, p: YaccProduction) -> None:
        """
        statements : statement
                   | statement statements
        """

    def p_empty(self, p: YaccProduction) -> None:
        """
        empty :
        """

    def p_error(self, p: YaccProduction) -> None:
        raise ParserSyntaxError(p)

    # -----------------------------------------------------------------------------
    # Data Structures
    # -----------------------------------------------------------------------------

    # OBJECT (Paul)

    def p_data_structure(self, p: YaccProduction) -> None:
        """
        data_structure : assignment_object
        """

    def p_assignment_object(self, p: YaccProduction) -> None:
        """
        assignment_object : INTERFACE ID OPENBRACE object_value CLOSEBRACE
        """

    def p_object_value(self, p: YaccProduction) -> None:
        """
        object_value : ID COLON data_type SEMICOLON
                     | ID COLON data_type SEMICOLON object_value
        """

    # -----------------------------------------------------------------------------
    # Control Structures
    # -----------------------------------------------------------------------------

    # IF:    Paul
    # WHILE: JA

    def p_control_structure(self, p: YaccProduction) -> None:
        """
        control_structure : IF OPENPAREN condition CLOSEPAREN OPENBRACE statements CLOSEBRACE
                          | WHILE OPENPAREN condition CLOSEPAREN OPENBRACE statements CLOSEBRACE
        """

    def p_condition(self, p: YaccProduction) -> None:
        """
        condition : condition_values
                  | logical_exclamation OPENPAREN condition_values CLOSEPAREN
        """

    def p_condition_values(self, p: YaccProduction) -> None:
        """
        condition_values : STRINGCONTENT
                         | logical
        """

    def p_logical(self, p: YaccProduction) -> None:
        """
        logical : logical_values
                | logical_values logical_operators logical_values
                | logical_values logical_operators logical_values logical_operators logical
        """

    def p_logical_values(self, p: YaccProduction) -> None:
        """
        logical_values : ID
                       | boolean_value
                       | comparative
        """

    def p_comparative(self, p: YaccProduction) -> None:
        """
        comparative : comparative_values comparative_operator comparative_values
                    | STRINGCONTENT EQUALSEQUALS STRINGCONTENT
                    | STRINGCONTENT EQUALSEQUALSEQUALS STRINGCONTENT
        """

    def p_comparative_values(self, p: YaccProduction) -> None:
        """
        comparative_values : ID
                           | NUMBER
        """

    # -----------------------------------------------------------------------------
    # Function Declarations
    # -----------------------------------------------------------------------------

    # fn decl var:     Paul
    # fn decl keyword: JA
    # fn decl arrow:   Christopher

    def p_assignment_function(self, p: YaccProduction) -> None:
        """
        assignment_function : CONST ID EQUALS FUNCTION OPENPAREN function_parameter CLOSEPAREN return_type OPENBRACE function_body CLOSEBRACE SEMICOLON
                            | FUNCTION ID OPENPAREN function_parameter CLOSEPAREN return_type OPENBRACE function_body CLOSEBRACE
                            | CONST ID EQUALS OPENPAREN function_parameter CLOSEPAREN return_type ARROW OPENBRACE function_body CLOSEBRACE
        """

    def p_function_parameter(self, p: YaccProduction) -> None:
        """
        function_parameter : ID COLON data_type
                           | ID COLON data_type COMMA function_parameter
        """

    def p_function_body(self, p: YaccProduction) -> None:
        """
        function_body : statements RETURN ID SEMICOLON
                      | statements RETURN assignment_var_value SEMICOLON
                      | RETURN ID SEMICOLON
                      | RETURN assignment_var_value SEMICOLON
        """

    def p_return_type(self, p: YaccProduction) -> None:
        """
        return_type : COLON data_type
                    | empty
        """

    # -----------------------------------------------------------------------------
    # Terminals
    # -----------------------------------------------------------------------------

    def p_assignment_var(self, p: YaccProduction) -> None:
        """
        assignment_var : assignment_var_type ID EQUALS assignment_var_value SEMICOLON
                       | assignment_var_type ID COLON data_type EQUALS assignment_var_value SEMICOLON
                       | assignment_var_type ID EQUALS arithmetic_expression SEMICOLON
        """

    def p_assignment_var_type(self, p: YaccProduction) -> None:
        """
        assignment_var_type : LET
                            | CONST
                            | VAR
        """

    def p_data_type(self, p: YaccProduction) -> None:
        """
        data_type : TYPE_BOOLEAN
                  | TYPE_NUMBER
                  | TYPE_STRING
        """

    def p_assignment_var_value(self, p: YaccProduction) -> None:
        """
        assignment_var_value : STRINGCONTENT
                             | NUMBER
                             | TRUE
                             | FALSE
        """

    def p_logical_exclamation(self, p: YaccProduction) -> None:
        """
        logical_exclamation : EXCLAMATION
        """

    def p_comparative_operators(self, p: YaccProduction) -> None:
        """
        comparative_operator : EQUALSEQUALS
                             | EQUALSEQUALSEQUALS
                             | EXCLAMATIONEQUALS
                             | LESSTHAN
                             | LESSTHANEQUALS
                             | GREATERTHAN
                             | GREATERTHANEQUALS
        """

    def p_boolean_value(self, p: YaccProduction) -> None:
        """
        boolean_value : TRUE
                      | FALSE
        """

    def p_logical_operators(self, p: YaccProduction) -> None:
        """
        logical_operators : AMPERSANDAMPERSAND
                          | OROR
        """

    def p_arithmetic_operators(self, p: YaccProduction) -> None:
        """
        arithmetic_operators : PLUS
                             | MINUS
                             | MULTIPLY
                             | DIVIDE
                             | MODULO
                             | XOR
        """

    def p_arithmetic_expression(self, p: YaccProduction) -> None:
        """
        arithmetic_expression : ID
                              | ID arithmetic_operators arithmetic_expression
        """

    # -------------------------------------------------------------------------

    def __init__(self, lexer: TSLexer) -> None:
        self.lexer = lexer
        self.parser = plyacc.yacc(module=self)

    def parse(self, input: str):
        self.parser.parse(input, self.lexer)

    def run(self, prompt: str):
        while True:
            try:
                s = input(prompt)
                if not s:
                    continue
                self.parse(s)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
