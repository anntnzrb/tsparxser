from typing import List
from ply.lex import LexToken

from .util import read_file
from .lexer import Lexer as TSLexer
from .parser import Parser as TSParser


def main():
    samples_dir: str = "data"
    file: str = f"{samples_dir}/data.txt"
    data: str = read_file(file)

    # numerical menu
    print("1: Lex")
    print("2: Yacc")
    choice = int(input("Choose an option: "))

    # create lexer and feed data
    lexer: TSLexer = TSLexer()
    lexed: List[LexToken] = lexer.lex(data)

    # option 1 : lex
    if choice == 1:
        # show tokens
        for t in lexed:
            print(t)

    # option 2 : yacc
    elif choice == 2:
        parser: TSParser = TSParser()
        parser = parser.run()
        while True:
            try:
                s = input("TS Parser> ")
            except EOFError:
                break
            if not s:
                continue
            parsed = parser.parse(s, lexer=lexer)
            if parsed is not None:
                print(parsed)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
