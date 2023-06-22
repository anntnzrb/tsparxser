import ply.yacc as plyacc
from ply.yacc import YaccProduction
from typing import Tuple

from .lexer import Lexer as TSLexer


class Parser:
    tokens: Tuple[str] = TSLexer.tokens

    def p_assignment(self, p: YaccProduction) -> None:
        """
        assignment : LET ID EQUALS assignment_value
                   | LET ID COLON data_type EQUALS assignment_value
        """

    def p_data_type(self, p: YaccProduction) -> None:
        """
        data_type : TYPE_BOOLEAN
                  | TYPE_NUMBER
                  | TYPE_STRING
        """

    def p_assignment_value(self, p: YaccProduction) -> None:
        """
        assignment_value : STRINGCONTENT
                         | NUMBER
                         | TRUE
                         | FALSE
        """

    def p_error(self, p: YaccProduction) -> None:
        print(f"Syntax error in input '{p}'!")

    # -------------------------------------------------------------------------

    def __init__(self, lexer: TSLexer) -> None:
        self.lexer = lexer
        self.parser = plyacc.yacc(module=self, debug=True)

    def run(self, prompt: str):
        while True:
            try:
                s = input(prompt)
                if not s:
                    continue
                self.parser.parse(s, self.lexer)
            except EOFError:
                break
            except Exception as e:
                print(f"Error: {e}")
                continue
