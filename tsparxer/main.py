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
# Token-RegEx
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


# A regular expression rule with some action code
# def t_NUMBER(t):
#     r"\d+"
#     t.value = int(t.value)
#     return t


# Define a rule so we can track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r"[a-zA-Z]+"
    t.type = reserved.get(t.value.lower(), "ID")
    return t


# A string containing ignored characters (spaces and tabs)
t_ignore = " \t"


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# ------------------------------------------------------------------------------

# Build the lexer
lexer = lex.lex()

# Test it out
data = """
"dsadasdas"
()
[]{}
=
+=
-=
,
=
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
