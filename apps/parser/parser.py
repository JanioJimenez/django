from .ply import lex as lex
from .ply import yacc as yacc

resultado_lexema = []

reservada = (
   
    'INCLUIR',
    'MOSTRAR',
    'LEER',
    'NUMERICO',
    'DEVUELVE',
    'VACIO',
    'ENTERO',
    'BOOL',
)
tokens = reservada + (
    'IDENTIFICADOR',
    'ASIGNADOR',
    'NOVARIABLE',

    'SUMADOR',
    'RESTANDO',
    'MULTIPLICADOR',
    'DIVISOR',
    'POTENCIADOR',
    'MODULO',

    'SI',
    'YSINO',
    
    'MIENTRAS',
    'PARA',
    'Y',
    'O',
    'NEGACION',
    'ELMENOR',
    'MENOROIGUAL',
    'ELMAYOR',
    'MAYOROIGUAL',
    'IGUAL',
    'DESIGUAL',
    
    'PARENIZQ',
    'PARENDER',
    'LLAVEIZQ',
    'LLAVEDER',
  
)



t_SUMADOR = r'\&'
t_RESTANDO = r'-'
t_MULTIPLICADOR = r'\*'
t_DIVISOR = r'/'
t_MODULO = r'\%'
t_POTENCIADOR = r'(\*{2} | \^)'
t_ASIGNADOR = r'='

t_Y= r'\&\&'
t_O = r'\|{2}'
t_NEGACION= r'\!'
t_ELMENOR = r'<'
t_ELMAYOR = r'>'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'
t_LLAVEIZQ = r'{'
t_LLAVEDER = r'}'
t_ignore =' \t'



def t_INCLUIR(t):
    r'incl'
    return t

def t_NUMERICO(t):
    r'num'
    return t

def t_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_MOSTRAR(t):
    r'msg'
    return t

def t_LEER(t):
    r'rec'
    return t

def t_BOOL(t):
    r'bool'
    return t

def t_YSINO(t):
    r'sino'
    return t

def t_SI(t):
    r'si'
    return t

def t_DEVUELVE(t):
   r'retorna'
   return t

def t_VACIO(t):
   r'vac'
   return t

def t_MIENTRAS(t):
    r'mtras'
    return t

def t_PARA(t):
    r'para'
    return t

def t_IDENTIFICADOR(t):
    r'[a-zA-Z_][a-zA-Z0-9]*'
    return t

def t_MENOROIGUAL(t):
    r'<='
    return t

def t_MAYOROIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'=='
    return t

def t_DESIGUAL(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comments(t):
    r'\$.*'
    pass

def t_error(t):
    global resultado_lexema
    estado = "Token no valido en la Linea: {:4} ".format(str(t.lineno))
    resultado_lexema.append(estado)
    t.lexer.skip(1)


class AnalizadorLexico:
    def __init__(self,tokens):
        self.tokens=tokens
    
    def getTokens(self):
        return self.tokens
    
    def prueba(self,data):
        global resultado_lexema
        analizador = lex.lex()
        analizador.input(data)
        resultado_lexema.clear()
        while True:
            tok = analizador.token()
            if not tok:
                break
            estado = "Linea {:4} Tipo {:16} ".format(str(tok.lineno),str(tok.type) )
            resultado_lexema.append(estado)
        return resultado_lexema

# resultado del analisis
resultado_gramatica = []

precedence = (
    ('right','ASIGNADOR'),
    ('left', 'SUMADOR', 'RESTANDO'),
    ('left', 'MULTIPLICADOR', 'DIVISOR'),
)
nombres = {}

def p_declaracion_asignar(t):
    'declaracion : IDENTIFICADOR ASIGNADOR expresion'
    nombres[t[1]] = t[3]

def p_declaracion_expr(t):
    'declaracion : expresion'
    # print("Resultado: " + str(t[1]))
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMADOR expresion
                |   expresion RESTANDO expresion
                |   expresion MULTIPLICADOR expresion
                |   expresion DIVISOR expresion
                |   expresion POTENCIADOR expresion
                |   expresion MODULO expresion

    '''
    if t[2] == '&':
        t[0] = t[1] + t[3]
    elif t[2] == '-':
        t[0] = t[1] - t[3]
    elif t[2] == '*':
        t[0] = t[1] * t[3]
    elif t[2] == '/':
        t[0] = t[1] / t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1


def p_expresion_grupo(t):
    '''
    expresion  : PARENIZQ expresion PARENDER
                | LLAVEIZQ expresion LLAVEDER
    '''
    t[0] = t[2]
# sintactico de expresiones logicas
def p_expresion_logicas(t):
    '''
    expresion   :  expresion ELMENOR expresion 
                |  expresion ELMAYOR expresion 
                |  expresion MENOROIGUAL expresion 
                |   expresion MAYOROIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DESIGUAL expresion
                |  PARENIZQ expresion PARENDER ELMENOR PARENIZQ expresion PARENDER
                |  PARENIZQ expresion PARENDER ELMAYOR PARENIZQ expresion PARENDER
                |  PARENIZQ expresion PARENDER MENOROIGUAL PARENIZQ expresion PARENDER 
                |  PARENIZQ  expresion PARENDER MAYOROIGUAL PARENIZQ expresion PARENDER
                |  PARENIZQ  expresion PARENDER IGUAL PARENIZQ expresion PARENDER
                |  PARENIZQ  expresion PARENDER DESIGUAL PARENIZQ expresion PARENDER
    '''
    if t[2] == "<": t[0] = t[1] < t[3]
    elif t[2] == ">": t[0] = t[1] > t[3]
    elif t[2] == "<=": t[0] = t[1] <= t[3]
    elif t[2] == ">=": t[0] = t[1] >= t[3]
    elif t[2] == "==": t[0] = t[1] is t[3]
    elif t[2] == "!=": t[0] = t[1] != t[3]
    elif t[3] == "<":
        t[0] = t[2] < t[4]
    elif t[2] == ">":
        t[0] = t[2] > t[4]
    elif t[3] == "<=":
        t[0] = t[2] <= t[4]
    elif t[3] == ">=":
        t[0] = t[2] >= t[4]
    elif t[3] == "==":
        t[0] = t[2] is t[4]
    elif t[3] == "!=":
        t[0] = t[2] != t[4]


# gramatica de expresiones booleanadas
def p_expresion_booleana(t):
    '''
    expresion   :   expresion Y expresion 
                |   expresion O expresion 
                |   expresion NEGACION expresion 
                |  PARENIZQ expresion Y expresion PARENDER
                |  PARENIZQ expresion O expresion PARENDER
                |  PARENIZQ expresion NEGACION expresion PARENDER
    '''
    if t[2] == "&&":
        t[0] = t[1] and t[3]
    elif t[2] == "||":
        t[0] = t[1] or t[3]
    elif t[2] == "!":
        t[0] =  t[1] is not t[3]
    elif t[3] == "&&":
        t[0] = t[2] and t[4]
    elif t[3] == "||":
        t[0] = t[2] or t[4]
    elif t[3] == "!":
        t[0] =  t[2] is not t[4]



def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_nombre(t):
    'expresion : IDENTIFICADOR'
    try:
        t[0] = nombres[t[1]]
    except LookupError:
        print("Nombre desconocido ", t[1])
        t[0] = 0

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico "
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)

parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("resultado: ", resultado_gramatica)
    return resultado_gramatica

