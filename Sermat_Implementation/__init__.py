#import construcciones
#import sermatLexer
import sermatParserCup


#construcciones = construcciones()
#sermatParser = sermatParserCup()

#lexer = sermatLexer.SermatLexer()
#lexer.buildLexer()
#print lexer.tokenize("{}")

parser = sermatParserCup.SermatParserCup()

#parser.parsear("{x:tuple(1,2)}")
#parser.parsear('{ idObject1: [$id1=1, $id2=2, suma($id1, $id2, 3)], "idObject2StrWithAnotherObject": [{ idObject3Anidado: [3,4] }, "elem2", true, [ ] ], "idObject4":[true, false, null, 2, "SoyString"]  }')
#parser.parsear("{idObject1:[$id1=1, $id2=5, suma($id1, $id2, 3)]}")
#parser.parsear("{idObject1:[$id1=2, suma(5,$id1)]}")
#parser.parsear("$id1=[$id1]")

#keyId:[$sum=Suma(2,3), 6, $sum]
parser.parsear('{keyId:[$sum=Suma(2,3), 6, $sum]  }')





