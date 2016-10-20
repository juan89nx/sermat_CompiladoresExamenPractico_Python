#Created by: Juan Perciante
# July 2016
# Get the token map from the lexer.

import sermatLexer
import construcciones
import ply_LexCup.yacc as yacc


class SermatParserCup:
    def __init__(self):
        self.lex = sermatLexer.SermatLexer()
        self.parser = yacc.yacc()
        self.parser.constructions = construcciones.Construcciones()
        #self.c = construcciones.Construcciones()
        self.parser.bindingsList = {}
        self.lex.buildLexer()
        self.tokens = self.lex.tokens #sermatLexer.SermatLexer().tokens

    #par = yacc.yacc()
    #lex = sermatLexer.SermatLexer()
    #lex.buildLexer()
    #tokens = lex.tokens
    #tokens = sermatLexer.SermatLexer.tokens
    #print tokens
    #construcciones = construcciones.Construcciones()

    # Precedence rules
    precedence = (
        ('BINDINGS', 'ID', 'EQUALS', 'STR'),
        ('LEFT_BRACE', 'RIGHT_BRACE'),
        ('RIGHT_BRACK', 'COMMA'),
        )

    # for storing bindings variables
    #bindingsList = {}

    def p_value(self, v):
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
            v[0] = self.parser.bindingsList[v[1]]
        elif (v[2] == '=' and len(v)==4) :
            v[0] = v[3]
            self.parser.bindingsList[v[1]] = v[3]
        elif (v[2] == '(' and v[3]== ')') :
            #v[0] = construcciones.construirEnBaseAFuncion(v[1],[])
            v[0] = self.c.construirEnBaseAFuncion(v[1],[])
        elif (v[2] == '(' and v[4]== ')') :
            #v[0] = construcciones.constrirEnBaseAFuncion(v[1],v[3])
            v[0] = self.parser.constructions.constrirEnBaseAFuncion(v[1], v[3])

    def p_value_boolNumStrNull(self, v):
        '''value : TRUE
                 | FALSE
                 | NUM
                 | STR
                 | NULL'''
        v[0] = v[1]


    def p_value_str_rules(self, v):
        '''value : STR LEFT_PAR  RIGHT_PAR
                 | STR LEFT_PAR elements RIGHT_PAR'''
        if (v[2]=="(" and v[3]==")"):
            v[0] = []
            #v[0] = construcciones.construirEnBaseAFuncion(v[1],[])
            v[0] = self.parser.constructions.construirEnBaseAFuncion(v[1],[])
        elif (len(v)==5):
            #v[0] = construcciones.construirEnBaseAFuncion(v[1],v[3])
            v[0] = self.parser.constructions.construirEnBaseAFuncion(v[1],v[3])

    def p_members_mem_str_val(self, m):
            'members : members COMMA STR COLON value'
            m[0] = m[1]
            m[0][m[3]] = m[5]

    def p_members_mem_id_val(self, m):
            'members : members COMMA ID COLON value'
            if(m[2]=="," and m[4]== ":"):
                m[0] = m[1]
                m[0][m[3]] = m[5]

    def p_members_str_val(self, m):
            'members : STR COLON value'
            if(m[2]==':' and type(m[1]) == type(" ")):
                m[0] = {}
                m[0][m[1]] = m[3]

    def p_members_id_val(self, m):
            'members : ID COLON value'
            m[0] = {}
            m[0][m[1]] = m[3]


    def p_elements(self, e):
        '''elements : value
                    | elements COMMA value'''
        if (len(e)==4) :
            e[0] = e[1]
            e[0].append(e[3])
        else:
            e[0] = [e[1]]

    def p_error(self, p):
        print("Syntax error at '%s'" % p.value)

    #parser = yacc.yacc()

    def parsear(self, entrada):
        result = self.parser.parse(entrada)

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