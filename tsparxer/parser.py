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
                  | function_decl
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

    # OBJECT: Paul
    # ARRAY:  Christopher
    # TUPLE:  JA

    def p_data_structure(self, p: YaccProduction) -> None:
        """
        data_structure : structure_object
                       | structure_array
                       | structure_tuple
        """

    # Object

    def p_structure_object(self, p: YaccProduction) -> None:
        """
        structure_object : INTERFACE ID OPENBRACE structure_object_values CLOSEBRACE
        """

    def p_structure_object_values(self, p: YaccProduction) -> None:
        """
        structure_object_values : ID COLON data_type SEMICOLON
                                | ID COLON data_type SEMICOLON structure_object_values
        """

    # Array

    def p_structure_array(self, p: YaccProduction) -> None:
        """
        structure_array : assignment_var_type ID COLON data_type OPENBRACKET CLOSEBRACKET EQUALS structure_array_data SEMICOLON
        """

    def p_structure_array_data(self, p: YaccProduction) -> None:
        """
        structure_array_data : OPENBRACKET assignment_var_values CLOSEBRACKET
        """

    # Tuple

    def p_structure_tuple(self, p: YaccProduction) -> None:
        """
        structure_tuple : assignment_var_type ID COLON OPENBRACKET structure_tuple_type_list CLOSEBRACKET EQUALS structure_tuple_data SEMICOLON
        """

    def p_tuple_type_list(self, p: YaccProduction) -> None:
        """
        structure_tuple_type_list : data_type
                                  | data_type COMMA structure_tuple_type_list
        """

    def p_structure_tuple_data(self, p: YaccProduction) -> None:
        """
        structure_tuple_data : OPENBRACKET assignment_var_values CLOSEBRACKET
        """

    # -----------------------------------------------------------------------------
    # Control Structures
    # -----------------------------------------------------------------------------

    # IF:    Paul
    # WHILE: JA
    # FOR:   Christopher

    def p_control_structure(self, p: YaccProduction) -> None:
        """
        control_structure : control_if
                          | control_if_else
                          | control_while
                          | loop_for
        """

    def p_control_if(self, p: YaccProduction) -> None:
        """
        control_if : IF OPENPAREN condition CLOSEPAREN OPENBRACE statements CLOSEBRACE
        """
        p[0] = ("if", p[3], p[6])

    def p_control_if_else(self, p: YaccProduction) -> None:
        """
        control_if_else : control_if ELSE OPENBRACE statements CLOSEBRACE
        """
        p[0] = ("if_else", p[4])

    def p_control_while(self, p: YaccProduction) -> None:
        """
        control_while : WHILE OPENPAREN condition CLOSEPAREN OPENBRACE statements CLOSEBRACE
        """
        p[0] = ("while", p[3], p[6])

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
        comparative : comparative_values comparative_operators comparative_values
                    | STRINGCONTENT EQUALSEQUALS STRINGCONTENT
                    | STRINGCONTENT EQUALSEQUALSEQUALS STRINGCONTENT
        """

    def p_comparative_values(self, p: YaccProduction) -> None:
        """
        comparative_values : ID
                           | NUMBER
        """

    # -----------------------------------------------------------------------------
    # for loop
    # -----------------------------------------------------------------------------

    def p_loop_for(self, p: YaccProduction) -> None:
        """
        loop_for : FOR OPENPAREN assignment_var_type ID EQUALS NUMBER SEMICOLON loop_for_condition SEMICOLON loop_for_var_delta CLOSEPAREN OPENBRACE statements CLOSEBRACE
                 | FOR OPENPAREN assignment_var_type ID COLON data_type EQUALS NUMBER SEMICOLON loop_for_condition SEMICOLON loop_for_var_delta CLOSEPAREN OPENBRACE statements CLOSEBRACE
        """
        if len(p) == 15:
            p[0] = ("for", p[8], p[10], p[13])
        else:
            p[0] = ("for", p[10], p[12], p[15])

    def p_loop_for_condition(self, p: YaccProduction) -> None:
        """
        loop_for_condition : ID comparative_operators NUMBER
        """

    def p_loop_for_var_delta(self, p: YaccProduction) -> None:
        """
        loop_for_var_delta : ID PLUSPLUS
                           | ID MINUSMINUS
                           | PLUSPLUS ID
                           | MINUSMINUS ID
        """

    # -----------------------------------------------------------------------------
    # Function Declarations
    # -----------------------------------------------------------------------------

    # fn decl var:     Paul
    # fn decl keyword: JA
    # fn decl arrow:   Christopher

    def p_function_decl(self, p: YaccProduction) -> None:
        """
        function_decl : CONST ID EQUALS FUNCTION OPENPAREN function_parameter CLOSEPAREN return_type OPENBRACE function_body CLOSEBRACE SEMICOLON
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

    def get_val_data_type(self, value):
        """
        NOTE: This method is a workaround (hack) to accomplish type verification.

        It works by comparing the given value to Python's built-in types, it does
        not perform a check with the lexed/parsed language.
        """

        if isinstance(value, bool) or value in [
            "TRUE",
            "FALSE",
            "true",
            "false",
            "True",
            "False",
        ]:
            return "boolean"
        elif isinstance(value, str):
            # Remove leading and trailing quotes
            value = value.strip("'\"")
            return "string"
        elif isinstance(value, int) or isinstance(value, float):
            return "number"
        else:
            return "unknown"

    def p_assignment_var(self, p: YaccProduction) -> None:
        """
        assignment_var : assignment_var_type ID EQUALS assignment_var_values SEMICOLON
                       | assignment_var_type ID COLON data_type EQUALS assignment_var_value SEMICOLON
        """
        if len(p) == 8:
            var_type = p[4]
            value_type = self.get_val_data_type(p[6])

            if var_type != value_type:
                print(
                    f"Type mismatch: cannot assign {value_type} to {var_type}"
                )
                p[0] = None
            else:
                p[0] = p[5]

    def p_assignment_var_type(self, p: YaccProduction) -> None:
        """
        assignment_var_type : LET
                            | CONST
                            | VAR
        """
        p[0] = p[1]

    def p_data_type(self, p: YaccProduction) -> None:
        """
        data_type : TYPE_BOOLEAN
                  | TYPE_NUMBER
                  | TYPE_STRING
        """
        p[0] = p[1]

    def p_assignment_var_value(self, p: YaccProduction) -> None:
        """
        assignment_var_value : STRINGCONTENT
                             | NUMBER
                             | TRUE
                             | FALSE
                             | ID
        """
        p[0] = p[1]

    def p_assignment_var_values(self, p: YaccProduction) -> None:
        """
        assignment_var_values : assignment_var_value
                              | assignment_var_value COMMA assignment_var_values
                              | assignment_var_value arithmetic_operators assignment_var_values
        """
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = [p[1]] + p[3]

    def p_logical_exclamation(self, p: YaccProduction) -> None:
        """
        logical_exclamation : EXCLAMATION
        """
        p[0] = p[1]

    def p_comparative_operators(self, p: YaccProduction) -> None:
        """
        comparative_operators : EQUALSEQUALS
                              | EQUALSEQUALSEQUALS
                              | EXCLAMATIONEQUALS
                              | LESSTHAN
                              | LESSTHANEQUALS
                              | GREATERTHAN
                              | GREATERTHANEQUALS
        """
        p[0] = p[1]

    def p_boolean_value(self, p: YaccProduction) -> None:
        """
        boolean_value : TRUE
                      | FALSE
        """
        p[0] = p[1]

    def p_logical_operators(self, p: YaccProduction) -> None:
        """
        logical_operators : AMPERSANDAMPERSAND
                          | OROR
        """
        p[0] = p[1]

    def p_arithmetic_operators(self, p: YaccProduction) -> None:
        """
        arithmetic_operators : PLUS
                             | MINUS
                             | MULTIPLY
                             | DIVIDE
                             | MODULO
                             | XOR
        """
        p[0] = p[1]

    # def p_arithmetic_expression(self, p: YaccProduction) -> None:
    #     """
    #     arithmetic_expression : ID
    #                           | ID arithmetic_operators arithmetic_expression
    #     """
    #     if len(p) == 2:
    #         p[0] = p[1]
    #     else:
    #         p[0] = {"operator": p[2], "left": p[1], "right": p[3]}

    # -------------------------------------------------------------------------

    def __init__(self, lexer: TSLexer) -> None:
        self.lexer = lexer
        self.parser = plyacc.yacc(module=self)

    def parse(self, input: str):
        self.parser.parse(input, self.lexer)

    def run(self, prompt: str = "TSParxser"):
        try:
            s = input(prompt)
            self.parse(s)
        except Exception as e:
            print(f"Error: {e}")

    def run_loop(self, prompt: str):
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
