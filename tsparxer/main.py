from .lexer import build_lexer


def main():
    # Build the lexer
    lexer = build_lexer()

    file: str = "samples/data.txt"
    with open(file, "r") as file:
        data = file.read()

    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


if __name__ == "__main__":
    main()
