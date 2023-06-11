import ply.lex as lex

# ------------------------------------------------------------------------------
# Reserved words
# ------------------------------------------------------------------------------
reserved = {
    # JA
    # Paul
    "while": "WHILE",
    "return": "RETURN",
    # Chris
}
# ------------------------------------------------------------------------------
# Tokens
# ------------------------------------------------------------------------------
tokens = (
    "ID",
    # JA
    "ANY",
    # Paul
    # "STRING",
    # Chris
    "PLUS",
) + tuple(reserved.values())

# ------------------------------------------------------------------------------
# Token-RegEx
# ------------------------------------------------------------------------------
t_PLUS = r"\+"

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
3 + 4 * 10
  + -20 *2
  while
  WHILE
  while2
"""

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
