
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'IDENTIFICADOR',    # [a-zA-Z_][a-zA-Z0-9_]*
    'NUMERO',           # [0-9]
    'STRING',           # [a-zA-Z0-9_]*
    
    #OPERACIONES

    'SUMA',             # +
    'RESTA',            # -
    'MULTIPLICACION',   # *
    'DIVICION',         # /
    'IGUAL',            # =

    #AGRUPACION

    'LPAREN',           # (
    'RPAREN',           # )
    'LLLAVE',           # {
    'RLLAVE',           # }
    'LCORCH',           # [
    'RCORCH',           # ]

    #SEPARADOR

    'COMA',             #,
    'DOSPUN',           #:
    'COMILLA'           #"
    )

# Tokens

t_IDENTIFICADOR = r'[a-zA-Z][a-zA-Z0-9]*'
t_STRING = r'[a-zA-Z0-9][a-zA-Z0-9]*'
#OPERADORES
t_SUMA = r'\+'
t_RESTA = r'-'
t_MULTIPLICACION   = r'\*'
t_DIVICION = r'/'
t_IGUAL = r'='
#AGRUPACION
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCORCH = r'\['
t_RCORCH = r'\]'
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
#SEPARADOR
t_COMA = r'\,'
t_DOSPUN = r'\:'
t_COMILLA = r'\"'

def t_NUMERO(t):
    r'\d+'
    try:    
        t.value = int(t.value)
    except ValueError:
        print("Valor entero demasiado grande %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
from .ply import lex
lexer = lex.lex()

# Parsing rules

precedence = (
    ('left','SUMA','RESTA'),
    ('left','MULTIPLICACION','DIVICION'),
    ('right','UMINUS'),
    )


def p_statement_assign(t):
    'statement : IDENTIFICADOR IGUAL expression'
    t[0] = t[1] 

def p_statement_expr(t):
    'statement : expression'
    print(t[1])
    t[0] = t[1] 

def p_expression_binop(t):
    '''expression : expression RESTA expression
                  | expression SUMA expression
                  | expression MULTIPLICACION expression
                  | expression DIVICION expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

def p_expression_uminus(t):
    'expression : RESTA expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMERO'
    t[0] = t[1]

def p_expression_json(t):
    'expression : json'
    t[0] = t[1]

def p_expression_name(t):
    'expression : IDENTIFICADOR'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_json_(t):
    'json : LLLAVE sentencia RLLAVE'
    t[0] = t[2]

def p_json_sentencia(t):
    '''sentencia : arreglo COMA sentencia
                 | arreglo
                 | objeto COMA sentencia
                 | objeto'''

def p_json_arreglo(t):
    '''arreglo : COMILLA STRING COMILLA DOSPUN LCORCH vector RCORCH
               | COMILLA STRING COMILLA DOSPUN LCORCH matriz RCORCH'''

def p_json_vector(t):
    '''vector : objeto COMA vector
              | objeto'''

def p_json_matriz(t):
    '''matriz : json COMA matriz
              | json'''

def p_json_objeto(t):
    '''objeto : COMILLA STRING COMILLA DOSPUN COMILLA NUMERO COMILLA
              | COMILLA STRING COMILLA DOSPUN COMILLA STRING COMILLA'''
    print(t[2],t[6])
    t[2] = t[6]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

from .ply import yacc
parser = yacc.yacc()

def evaluar(data):
    return parser.parse(data)