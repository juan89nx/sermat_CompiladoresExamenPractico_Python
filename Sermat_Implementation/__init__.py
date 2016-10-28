#import construcciones
#import sermatLexer
import sermatParserCup



#construcciones = construcciones()
#sermatParser = sermatParserCup()

#lexer = sermatLexer.SermatLexer()
#lexer.buildLexer()
#print lexer.tokenize("a")


parser = sermatParserCup.SermatParserCup()
#parser = yacc.yacc()

parser.parsear("{x:tuple(1,2)}")



'''
while True:
    try:
        s = raw_input('Entry > ')  # use input() on Python 3
        result = parser.parse(s)
        print "Parser Result:"
        print(result)
        # print "bindingsList:"
        # print bindingsList
        bindingsList = {}
    # except Exception:
    #    print "You need to type a valid enter!"
    except EOFError:
        break
'''