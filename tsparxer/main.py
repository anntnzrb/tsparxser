from .util import read_file
from .lexer import Lexer as TSLexer


def main():
    samples_dir: str = "data"
    file: str = f"{samples_dir}/data.txt"
    data: str = read_file(file)

    # create lexer and feed data
    lexer: TSLexer = TSLexer()
    lexed: List[LexToken] = lexer.lex(data)

    # show tokens
    for t in lexed:
        print(t)


if __name__ == "__main__":
    main()
