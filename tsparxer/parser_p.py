import ply.yacc as plyacc
from ply.yacc import YaccProduction
from typing import Tuple

from .lexer import Lexer as TSLexer


class ParserSyntaxError(Exception):
    def __init__(self, p: YaccProduction):
        super().__init__(f"Syntax error in input '{p}'!")


class Parser:
    tokens: Tuple[str] = TSLexer.tokens

    def p_assignment(self, p: YaccProduction) -> None:
        """
        assignment : assignment_type ID EQUALS assignment_value SEMICOLON
                   | assignment_type ID COLON data_type EQUALS assignment_value SEMICOLON
                   | assignment_type ID EQUALS calculates SEMICOLON
                   | CONSOLE DOT LOG OPENPAREN assignment_value CLOSEPAREN SEMICOLON
        """

    # -----------------------------------------------------------------------------
    #   FUNCTION
    # -----------------------------------------------------------------------------

    def p_assigment_function(self, p: YaccProduction) -> None:
        """
        assignment : CONST ID EQUALS FUNCTION OPENPAREN function_parameter CLOSEPAREN COLON data_type OPENBRACE function_body CLOSEBRACE SEMICOLON
        """

    def p_function_parameter(self, p: YaccProduction) -> None:
        """
        function_parameter : ID COLON data_type
                           | ID COLON data_type COMMA function_parameter
        """

    def p_function_body(self, p: YaccProduction) -> None:
        """
        function_body : assignment RETURN ID SEMICOLON
        """

    # -----------------------------------------------------------------------------
    #   TERMINALES
    # -----------------------------------------------------------------------------
    def p_data_type(self, p: YaccProduction) -> None:
        """
        data_type : TYPE_BOOLEAN
                  | TYPE_NUMBER
                  | TYPE_STRING
        """

    def p_assignment_type(self, p: YaccProduction) -> None:
        """
        assignment_type : LET
                        | CONST
                        | VAR
        """

    def p_assignment_value(self, p: YaccProduction) -> None:
        """
        assignment_value : STRINGCONTENT
                         | NUMBER
                         | TRUE
                         | FALSE
        """

    def p_calculates(self, p: YaccProduction) -> None:
        """
        calculates : ID
        | ID basic_operators calculates
        """

    def p_error(self, p: YaccProduction) -> None:
        raise ParserSyntaxError(p)

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


# -----------------------------------------------------------------------------
# estructuras de datos
# -----------------------------------------------------------------------------

# 1. array C
# 2. object P
# 3. ??? tuple J

# -----------------------------------------------------------------------------
# estructuras de control
# -----------------------------------------------------------------------------

# 1. if P
# 2. while J
# 3. for (el mas sencillo) C

# -----------------------------------------------------------------------------
# tipo de declaración de función
# -----------------------------------------------------------------------------

# 1. J
# function sum(a: number, b: number): number {
#   return a + b;
# }
#
# 2. P
# const multiply = function(a: number, b: number): number {
#   return a * b;
# };
#
# 3. C
# const divide = (a: number, b: number): number => {
#   return a / b;
# };
