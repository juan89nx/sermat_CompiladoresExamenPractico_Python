#Created by: Juan Perciante
# July 2016
# Get the token map from the lexer.

import construcciones
import ply_LexCup.lex as lex
import ply_LexCup.yacc as yacc


tokens = (
    'EQUALS',
    'COMMA',
    'COLON',
    'LEFT_BRACE',
    'RIGHT_BRACE',
    'LEFT_BRACK',
    'RIGHT_BRACK',
    'LEFT_PAR',
    'RIGHT_PAR',
    'NULL',
    'TRUE',
    'FALSE',
    'NUM',
    'ID',
    'STR',
    'BINDINGS'
)

# Tokens
t_EQUALS = r'='
t_COMMA = r','
t_COLON = r':'
t_LEFT_BRACE = r'\{'
t_RIGHT_BRACE = r'\}'
t_LEFT_BRACK = r'\['
t_RIGHT_BRACK = r'\]'
t_LEFT_PAR = r'\('
t_RIGHT_PAR = r'\)'

def t_ID(t):
    r'[A-Z_a-z][\-\.A-Z_a-z0-9]*'
    if t.value == 'true':
        t.type = 'TRUE'
    elif t.value == 'false':
        t.type = 'FALSE'
    elif t.value == 'null':
        t.type = "NULL"
    elif t.value == "NaN":
        t.type = "NUM"
        t.value = float("NaN")
    elif t.value == "Infinity":
        t.type = "NUM"
        t.value = float("Infinity")
    return t

# token created for Bindings
def t_BINDINGS(t):
    r'\$[\-\.A-Z_a-z0-9]+'
    return t

def t_NUM(t):
    r'[+-]Infinity|[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
    t.value = float(t.value)
    return t

def t_STR(t):
    r'\"([^\\\"]|\\[\0-\uFFFF])*\"'
    escaped = 0
    myString = t.value[1:-1]
    new_str = ""
    for i in range(0, len(myString)):
        c = myString[i]
        if escaped:
            if c == "n":
                c = "\n"
            elif c == "t":
                c = "\t"
            new_str += c
            escaped = 0
        else:
            if c == "\\":
                escaped = 1
            else:
                new_str += c
    t.value = new_str
    return t

def t_regular_exp_ignoro(t):
    r'[ \t\r\n\f]+|\/\*+([^\*]|\*+[^\/])*\*+\/'
    pass
    # No return value. Token discarded

# Ignored characters
t_ignore = ' \t\r\n\f'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Unexpected input < '%s' >" % t.value[0])
    t.lexer.skip(1)


# Precedence rules
precedence = (
    ('BINDINGS', 'ID', 'EQUALS', 'STR'),
    ('LEFT_BRACE', 'RIGHT_BRACE'),
    ('RIGHT_BRACK', 'COMMA'),
    )

def p_value_boolNumStrNull(v):
    '''value : TRUE
             | FALSE
             | NUM
             | STR
             | NULL'''
    v[0] = v[1]

def p_value_bind(p):
    '''value : BINDINGS'''
    p[0] = p.parser.sermat.bindingsList[p[1]]

def p_value_obj0(v):
    '''value : obj0 RIGHT_BRACE'''
    v[0]= v[1]

def p_value_obj1(v):
    '''value : obj1 RIGHT_BRACE'''
    v[0] = v[1]

def p_value_array0(v):
    '''value : array0 RIGHT_BRACK'''
    v[0] =  v[1]

def p_value_array1(v):
    'value : array1 RIGHT_BRACK'
    v[0] = v[1]

def p_value_cons0(v):
    'value : cons0 RIGHT_PAR'
    v[0] = v[1]
    #construcciones.Point2D_Construction.materialize(v[0][0], v[0][1])
    v[0]= v.parser.sermat.constructions.construirEnBaseAFuncion_Materialize(v[0][0], v[0][1], v[0][2])
    #[id_Funcion, instancia, listaDeValores]

def p_value_cons1(v):
    'value : cons1 RIGHT_PAR'
    v[0] = v[1]
    v[0] = v.parser.sermat.constructions.construirEnBaseAFuncion_Materialize(v[0][0], v[0][1], v[0][2])

##########################################################################

def p_obj0(obj0):
    '''obj0 : LEFT_BRACE
            | BINDINGS EQUALS LEFT_BRACE'''
    if(obj0[1] == "{"):
        obj0[0] = {}
    elif (obj0[2] == "="):
        obj0[0] = obj0.parser.sermat.bindingsList[obj0[1]] = {}

def p_obj1_A(obj1):
    '''obj1 : obj0 ID COLON value'''
    obj1[0] = obj1[1]
    obj1[0][obj1[2]]= obj1[4]

def p_obj1_B(obj1):
    '''obj1 : obj0 STR COLON value'''
    obj1[0] = obj1[1]
    obj1[0][obj1[2]]= obj1[4]

def p_obj1_C(obj1):
    '''obj1 : obj1 COMMA ID COLON value'''
    obj1[0] = obj1[1]
    obj1[0][obj1[3]]= obj1[5]

def p_obj1_D(obj1):
    '''obj1 : obj1 COMMA STR COLON value'''
    obj1[0] = obj1[1]
    obj1[0][obj1[3]]= obj1[5]


def p_array0(array0):
    '''array0 : LEFT_BRACK
              | BINDINGS EQUALS LEFT_BRACK'''
    if (array0[1] == "["):
        array0[0] = []
    else:
        array0[0] = array0.parser.sermat.bindingsList[array0[1]] = []

def p_array1_COMMA(array1):
    'array1 : array1 COMMA value'
    array1[0] = array1[1]
    array1[0].append(array1[3])

def p_array1(array1):
    'array1 : array0 value'
    if(len(array1) == 3 ):
        array1[0] = array1[1]
        array1[0].append(array1[2])



def p_cons0_ID(c): ##>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>REVISAR
    '''cons0 : BINDINGS EQUALS ID LEFT_PAR
             | ID LEFT_PAR'''
    if(c[2]== "="):
        instancia = c.parser.sermat.constructions.devolverInstanciaSiExiste(c[3])
        c[0] = [c[3],instancia, []] #id_Funcion, instancia, listaAtributos
        #Agrego a bindigList
        c.parser.sermat.bindingsList[c[1]] = instancia
    elif(c[2] == "("):
        instancia = c.parser.sermat.constructions.devolverInstanciaSiExiste(c[1])
        c[0] = [c[1],instancia, []] #id_Funcion, instancia, listaAtributos


def p_cons0_STR(c): #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>REVISAR
    '''cons0 : BINDINGS EQUALS STR LEFT_PAR
             | STR LEFT_PAR'''
    if (c[2] == "="):
        instancia = c.parser.sermat.constructions.devolverInstanciaSiExiste(c[3])
        c[0] = [c[3], instancia, []]  # id_Funcion, instancia, listaAtributos
        # Agrego a bindigList
        c.parser.sermat.bindingsList[c[1]] = instancia
    elif (c[2] == "("):
        instancia = c.parser.sermat.constructions.devolverInstanciaSiExiste(c[1])
        c[0] = [c[1], instancia, []]  # id_Funcion, instancia, listaAtributos

def p_cons1(c):
    '''cons1 : cons1 COMMA value
             | cons0 value'''
    if(c[2] == ","):
        c[0] = c[1]
        c[0][2].append(c[3])
    else:
        c[0] = c[1]
        c[0][2].append(c[2])



def p_error(p):
    print("Syntax error at '%s'" % p.value)

lex = lex.lex()
parser = yacc.yacc()

class SermatParserCup:
    def __init__(self):
        self.constructions = construcciones.Construcciones()
        self.bindingsList = {}

    def parsear(self, entrada):
        global parser
        parser.sermat = self
        result = parser.parse(entrada)
        parser.sermat = None
        print "Parser Result:"
        print(result)
        print "bindingList:"
        print self.bindingsList
        return result

    def serialize(self, obj, visited=None):
        if not visited:
            visited = []
        #TODO serialize
        if obj is None:
            return "null"
        elif obj is True:
            return "true"
        else:
            pass