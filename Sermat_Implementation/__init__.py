import construcciones as construcciones
#import sermatLexer
import sermatParserCup


#lexer = sermatLexer.SermatLexer()
#lexer.buildLexer()
#print lexer.tokenize("{}")

parser = sermatParserCup.SermatParserCup()

#parser.parsear("{x:tuple(1,2)}")
#parser.parsear('{ idObject1: [$id1=1, $id2=2, suma($id1, $id2, 3)], "idObject2StrWithAnotherObject": [{ idObject3Anidado: [3,4] }, "elem2", true, [ ] ], "idObject4":[true, false, null, 2, "SoyString"]  }')
#parser.parsear("{idObject1:[$id1=1, $id2=5, suma($id1, $id2, 3)]}")
#parser.parsear("{idObject1:[$id1=[2], Suma(5,$id1)]}")
#parser.parsear('{keyId:[$sum=Suma(2,3), 6, $sum]  }')

print parser.serialize(parser.parsear("$id=Suma(2,3,4,5)"))



dict = {'k1': 1, 'k2':2 }
#for key,value in dict.iteritems():
#    print (key, value)

#serialize = parser.serialize(dict, [])
#serialize = parser.serialize({'""': construcciones.Suma([2,3]), 'y':True}, [])
a = []
s = construcciones.Suma([2,3])
a.append(s)
a.append(s)


serialize = parser.serialize(a , [])
parser.parsear(serialize)
#print "Serialize result:"
#print serialize