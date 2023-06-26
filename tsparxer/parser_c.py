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
        """

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

    def p_assignment_values(self, p: YaccProduction) -> None:
        """
        assignment_values : assignment_value 
                          | assignment_value COMMA assignment_values
        """
    
    def p_array(self, p: YaccProduction) -> None:
        """
        array : OPENBRACKET  assignment_values CLOSEBRACKET
        """

    def p_assignment_array(self, p: YaccProduction) -> None:
        """
        assignment : assignment_type ID COLON data_type OPENBRACKET CLOSEBRACKET EQUALS array SEMICOLON
        """

    def p_condition(self, p: YaccProduction) -> None:
        """
        condition : ID LESSTHAN NUMBER
                  | ID LESSTHANEQUALS NUMBER
                  | ID GREATERTHAN NUMBER
                  | ID GREATERTHANEQUALS NUMBER
                  | ID EQUALSEQUALS NUMBER
                  | ID EXCLAMATIONEQUALS NUMBER 
        """

    def p_iteration(self, p: YaccProduction) -> None:
        """
        iteration : ID PLUSPLUS
                  | ID MINUSMINUS
        """

    def p_block(self, p: YaccProduction) -> None:
        """
        block : OPENBRACE CLOSEBRACE 
        """

    def p_for_loop(self, p: YaccProduction) -> None:
        """
        assignment : FOR OPENPAREN assignment_type ID EQUALS NUMBER SEMICOLON condition SEMICOLON iteration CLOSEPAREN block SEMICOLON
        """

    def p_parameter(self, p: YaccProduction) -> None:
        """
        parameter : ID COLON data_type 
        """
    
    def p_parameters(self, p: YaccProduction) -> None:
        """
        parameters : parameter 
                   | parameter COMMA parameters
        """

    def p_arrow_function(self, p: YaccProduction) -> None:
        """
        assignment : assignment_type ID EQUALS OPENPAREN parameters CLOSEPAREN COLON data_type ARROW block SEMICOLON
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

# 1. array #let arreglo: number[] = [1,2,3,4]; C
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
