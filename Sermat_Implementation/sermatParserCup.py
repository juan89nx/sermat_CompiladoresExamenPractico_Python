#Created by: Juan Perciante
# July 2016
# Get the token map from the lexer.

#import sermatLexer
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

# for storing bindings variables
#bindingsList = {}

def p_value(v):
    '''value : LEFT_BRACE RIGHT_BRACE
             | LEFT_BRACE members RIGHT_BRACE
             | LEFT_BRACK RIGHT_BRACK
             | LEFT_BRACK elements RIGHT_BRACK
             | BINDINGS EQUALS value
             | BINDINGS
             | ID LEFT_PAR RIGHT_PAR
             | ID LEFT_PAR elements RIGHT_PAR'''
    #global bindingsList
    if (v[1] == '{' and v[2] == '}') :
        v[0] = {}
    elif (v[1] == '{' and v[3]  == '}'):
        v[0] = v[2]
    elif (v[1] == '[' and v[2] == ']') :
        v[0] = []
    elif (v[1] == '[' and v[3]  == ']'):
        v[0] = v[2]
    elif (len(v) == 2):
        v[0] = v.parser.sermat.bindingsList[v[1]]
    elif (v[2] == '=' and len(v)==4) :
        v[0] = v[3]
        v.parser.sermat.bindingsList[v[1]] = v[3]
    elif (v[2] == '(' and v[3]== ')') :
        #v[0] = construcciones.construirEnBaseAFuncion(v[1],[])
        v[0] = v.parser.sermat.constructions.construirEnBaseAFuncion(v[1],[])
    elif (v[2] == '(' and v[4]== ')') :
        #v[0] = construcciones.constrirEnBaseAFuncion(v[1],v[3])
        v[0] = v.parser.sermat.constructions.construirEnBaseAFuncion(v[1], v[3])

def p_value_boolNumStrNull(v):
    '''value : TRUE
             | FALSE
             | NUM
             | STR
             | NULL'''
    v[0] = v[1]


def p_value_str_rules(v):
    '''value : STR LEFT_PAR  RIGHT_PAR
             | STR LEFT_PAR elements RIGHT_PAR'''
    if (v[2]=="(" and v[3]==")"):
        v[0] = []
        #v[0] = construcciones.construirEnBaseAFuncion(v[1],[])
        v[0] = v.parser.sermat.constructions.construirEnBaseAFuncion(v[1],[])
    elif (len(v)==5):
        #v[0] = construcciones.construirEnBaseAFuncion(v[1],v[3])
        v[0] = v.parser.sermat.constructions.construirEnBaseAFuncion(v[1],v[3])

def p_members_mem_str_val(m):
        'members : members COMMA STR COLON value'
        m[0] = m[1]
        m[0][m[3]] = m[5]

def p_members_mem_id_val(m):
        'members : members COMMA ID COLON value'
        if(m[2]=="," and m[4]== ":"):
            m[0] = m[1]
            m[0][m[3]] = m[5]

def p_members_str_val(m):
        'members : STR COLON value'
        if(m[2]==':' and type(m[1]) == type(" ")):
            m[0] = {}
            m[0][m[1]] = m[3]

def p_members_id_val(m):
        'members : ID COLON value'
        m[0] = {}
        m[0][m[1]] = m[3]

def p_elements(e):
    '''elements : value
                | elements COMMA value'''
    if (len(e)==4) :
        e[0] = e[1]
        e[0].append(e[3])
    else:
        e[0] = [e[1]]

def p_error(p):
    print("Syntax error at '%s'" % p.value)

lex = lex.lex()
parser = yacc.yacc()

class SermatParserCup:
    def __init__(self):
        #self.lex = sermatLexer.SermatLexer()
        #self.parser = yacc.yacc()
        self.constructions = construcciones.Construcciones()
        #self.c = construcciones.Construcciones()
        self.bindingsList = {}
        #self.lex.buildLexer()
        #self.tokens = self.lex.tokens #sermatLexer.SermatLexer().tokens

    #par = yacc.yacc()
    #lex = sermatLexer.SermatLexer()
    #lex.buildLexer()
    #tokens = lex.tokens
    #tokens = sermatLexer.SermatLexer.tokens
    #print tokens
    #construcciones = construcciones.Construcciones()


    #parser = yacc.yacc()

    def parsear(self, entrada):
        global parser
        parser.sermat = self
        result = parser.parse(entrada)
        parser.sermat = None
            #parser.parse(entrada)
        print "Parser Result:"
        print(result)
        # print "bindingsList:"
        # print bindingsList
        bindingsList = {}
        # except Exception:
        #    print "You need to type a valid enter!"
        return result

'''
    Lex.buildLexer()
    parser = yacc.yacc()


    while True:
        try:
            s = raw_input('Entry > ') # use input() on Python 3
            result = parser.parse(s)
            print "Parser Result:"
            print(result)
            #print "bindingsList:"
            #print bindingsList
            bindingsList = {}
        #except Exception:
        #    print "You need to type a valid enter!"
        except EOFError:
            break
'''