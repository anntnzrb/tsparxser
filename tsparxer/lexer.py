import ply.lex as lex
from typing import Dict, Tuple

# ------------------------------------------------------------------------------
# Reserved words
# ------------------------------------------------------------------------------
reserved: Dict[str, str] = {
    # JA
    "any": "ANY",
    "bool": "BOOL",
    "break": "BREAK",
    "case": "CASE",
    "catch": "CATCH",
    "class": "CLASS",
    "const": "CONST",
    "continue": "CONTINUE",
    "else": "ELSE",
    "false": "FALSE",
    "finally": "FINALLY",
    "for": "FOR",
    "function": "FUNCTION",
    "constructor": "CONSTRUCTOR",
    "if": "IF",
    "import": "IMPORT",
    "let": "LET",
    "new": "NEW",
    "number": "NUMBER",
    "private": "PRIVATE",
    "protected": "PROTECTED",
    "public": "PUBLIC",
    # Paul
    "while": "WHILE",
    "return": "RETURN",
    "true": "TRUE",
    "try": "TRY",
    "throw": "THROW",
    "var": "VAR",
    "string": "STRING",
    "error": "ERROR"
    # Chris
}

# ------------------------------------------------------------------------------
# Tokens
# ------------------------------------------------------------------------------
tokens: Tuple[str] = (
    # JA
    # Paul
    "STRINGCONTENT",
    "OPENPAREN",
    "CLOSEPAREN",
    "OPENBRACKET",
    "CLOSEBRACKET",
    "OPENBRACE",
    "CLOSEBRACE",
    "COMMA",
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
