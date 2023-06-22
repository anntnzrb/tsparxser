import ply.yacc as plyacc
from ply.yacc import YaccProduction

from .lexer import Lexer as TSLexer

class Parser:
    tokens = TSLexer.tokens

    def p_consulta(self, p: YaccProduction) -> None:
        "consulta : LET ID"

    def p_error(self, p: YaccProduction) -> None:
        print("Syntax error in input!")

    # -------------------------------------------------------------------------

    def __init__(self) -> None:
        self.parser = plyacc.yacc(module=self, debug=True)

    def run(self):
        return self.parser