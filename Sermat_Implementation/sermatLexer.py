# Created by: Juan Perciante
# July 2016

import ply_LexCup.lex as lex


class SermatLexer:
    def __init__(self):
        pass

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

    def t_ID(self,t):
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
    def t_BINDINGS(self,t):
        r'\$[\-\.A-Z_a-z0-9]+'
        return t

    def t_NUM(self,t):
        r'[+-]Infinity|[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
        t.value = float(t.value)
        return t

    def t_STR(self,t):
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

    def t_regular_exp_ignoro(self,t):
        r'[ \t\r\n\f]+|\/\*+([^\*]|\*+[^\/])*\*+\/'
        pass
        # No return value. Token discarded

    # Ignored characters
    t_ignore = ' \t\r\n\f'

    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += t.value.count("\n")

    def t_error(self,t):
        print("Unexpected input < '%s' >" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def buildLexer(self):
        #myLexer = lex.lex()
        #return myLexer
        myLexer = lex.lex(self)
        return myLexer

    # Utility function to test tokens. Given a string of text, tokenize into a list of tokens
    def tokenize(self,text):
        tokens = []
        lexer = self.buildLexer()
        lexer.input(text)
        while True:
            tok = lexer.token()
            if not tok: break
            tokens.append(tok)
        return tokens

