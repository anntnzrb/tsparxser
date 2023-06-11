import ply.lex as lex
from typing import Dict, Tuple

# ------------------------------------------------------------------------------
# Reserved words
# ------------------------------------------------------------------------------
reserved: Dict[str, str] = {
    keyword: keyword.upper()
    for keyword in [
        # JA
        "any",
        "bool",
        "break",
        "case",
        "catch",
        "class",
        "const",
        "continue",
        "else",
        "false",
        "finally",
        "for",
        "function",
        "constructor",
        "if",
        "import",
        "let",
        "new",
        "number",
        "private",
        "protected",
        "public",
        # Paul
        "while",
        "return",
        "true",
        "try",
        "throw",
        "var",
        "string",
        "error",
    ]
}


# ------------------------------------------------------------------------------
# Tokens
# ------------------------------------------------------------------------------
tokens: Tuple[str] = (
    # Paul
    "STRINGCONTENT",
    "OPENPAREN",
    "CLOSEPAREN",
    "OPENBRACKET",
    "CLOSEBRACKET",
    "OPENBRACE",
    "CLOSEBRACE",
    "COMMA",
    "COLON",
    "SEMICOLON",
    "EQUALS",
    "EQUALSEQUALS",
    "PLUSEQUALS",
    "MINUSEQUALS",
    # Chris
    "PLUS",
    "ID",
) + tuple(reserved.values())

# ------------------------------------------------------------------------------
# Token-RegEx & Functions
# ------------------------------------------------------------------------------
t_PLUS: str = r"\+"
t_STRINGCONTENT: str = r"(\"[^\"]*\"|'[^']*')"
t_OPENPAREN: str = r"\("
t_CLOSEPAREN: str = r"\)"
t_OPENBRACKET: str = r"\["
t_CLOSEBRACKET: str = r"\]"
t_OPENBRACE: str = r"\{"
t_CLOSEBRACE: str = r"\}"
t_COMMA: str = r"\,"
t_EQUALS: str = r"="
t_EQUALSEQUALS: str = r"=="
t_PLUSEQUALS: str = r"\+="
t_MINUSEQUALS: str = r"\-="
t_COLON: str = r"\:"
t_SEMICOLON: str = r"\;"

# ignored characters
t_ignore: str = " \t"


def t_newline(t: lex.LexToken) -> None:
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_ID(t: lex.LexToken) -> lex.LexToken:
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value.lower(), "ID")

    return t


# error handling
def t_error(t: lex.LexToken) -> None:
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def build_lexer() -> lex.Lexer:
    return lex.lex()
