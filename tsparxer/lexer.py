import ply.lex as lex

# ------------------------------------------------------------------------------
# Reserved words
# ------------------------------------------------------------------------------
reserved = {
    # JA
    # Paul
    "while": "WHILE",
    "return": "RETURN",
    "true": "TRUE",
    "try": "TRY",
    "throw": "THROW",
    "var": "VAR",
    "with": "WITH",
    "this": "THIS",
    "string": "STRING",
    "error": "ERROR"
    # Chris
}

# ------------------------------------------------------------------------------
# Tokens
# ------------------------------------------------------------------------------
tokens = (
    # JA
    "ANY",
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
    "PLUSEQUALS",
    "MINUSEQUALS",
    # Chris
    "PLUS",
    "ID",
) + tuple(reserved.values())

# ------------------------------------------------------------------------------
# Token-RegEx & Functions
# ------------------------------------------------------------------------------
t_PLUS = r"\+"
t_STRINGCONTENT = r"(\"[^\"]*\"|'[^']*')"
t_OPENPAREN = r"\("
t_CLOSEPAREN = r"\)"
t_OPENBRACKET = r"\["
t_CLOSEBRACKET = r"\]"
t_OPENBRACE = r"\{"
t_CLOSEBRACE = r"\}"
t_COMMA = r"\,"
t_EQUALS = r"="
t_PLUSEQUALS = r"\+="
t_MINUSEQUALS = r"\-="


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value.lower(), "ID")
    return t


# ignored characters
t_ignore = " \t"


# error handling
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def build_lexer():
    return lex.lex()
