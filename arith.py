# Most trivial: arithmetic expression lexer

import ply.lex as lex
from common import lex_shell

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
)

# Simple tokens
t_PLUS  = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE= r'/'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    # Do processing if needed, before returning t (the token object)
    t.value = float(t.value)
    return t

t_ignore = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Process input
lex_shell(lexer)
