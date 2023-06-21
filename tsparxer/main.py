from .lexer import Lexer as TSLexer


def main():
    samples_dir: str = "data"
    file: str = f"{samples_dir}/data.txt"
    with open(file, "r") as file:
        data = file.read()

    # create lexer and feed data
    lexer: TSLexer = TSLexer()
    lexed: List[LexToken] = lexer.lex(data)

    # show tokens
    for t in lexed:
        print(t)


if __name__ == "__main__":
    main()
