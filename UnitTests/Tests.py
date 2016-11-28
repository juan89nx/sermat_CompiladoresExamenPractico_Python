#Created by: Juan Perciante
# December 2016

import Sermat_Implementation.construcciones as construcciones
import Sermat_Implementation.sermatParserCup as sermatParserCup
import unittest

parser = sermatParserCup.SermatParserCup()

class Test_Parser_Serialize_Methods(unittest.TestCase):

    def setUp(self):
        self.parser = sermatParserCup.SermatParserCup()

    def test_parser_parsear_basics(self):
        self.assertEqual(self.parser.parsear("true"), "true")
        self.assertEqual(self.parser.parsear("false"), "false")
        self.assertEqual(self.parser.parsear("null"), "null")
        self.assertEqual(self.parser.parsear("8"), 8)
        self.assertEqual(self.parser.parsear("123.45"), 123.45)

    def test_parser_parsear_construcciones(self):
        self.assertTrue(self.parser.parsear("Point2D(2,3)"), construcciones.Point2D )
        self.assertTrue(self.parser.parsear("Suma([2,3])"), construcciones.Suma)
        self.assertTrue(self.parser.parsear("Producto([2,3])"), construcciones.Producto)
        self.assertTrue(self.parser.parsear("Tuple([2,3])"), construcciones.Tuple)
        self.assertTrue(self.parser.parsear("[Tuple([2,3]), Suma(4,5)]"), [construcciones.Tuple, construcciones.Suma])

    def test_parsear_parser_ComplexStructures(self):
        self.assertTrue(self.parser.parsear("{idObject1:[$id1=[1], $id2=[5], Suma($id1, $id2, 3)]}"), {'idObject1': [[1.0],[5.0], [construcciones.Suma]] } )
        self.assertTrue(self.parser.parsear("{idObject1:[$id1=[1], $id2=[5], $tup=Tuple($id1, $id2, 3, 8), Producto($id1, $tup) ] }"), {'idObject1': [[1.0], [5.0], construcciones.Tuple, construcciones.Producto]})
        self.assertTrue(self.parser.parsear("$idObj1={key:[$id1=[2,3]], key2: [ {key3:4}, Producto(7,8,9)] }"), {'idObj1':[{'key2': [{'key3': 4.0}]},construcciones.Producto, {'key': [2.0, 3.0]}]} )
        self.assertTrue(self.parser.parsear("{idObject1:[$id1=[1], $id2=[5], Suma($id1, $id2, 3), true, null]}"), {'idObject1': [[1.0], [5.0], [construcciones.Suma], True, None]})
        self.assertTrue(self.parser.parsear("$idObj1={key:[$id1=[2,3]], key2: [ Point2d(2,3),{key3:4}, Producto(7,8,9)] }"), {'idObj1': [{'key2': [construcciones.Point2D(2,3),{'key3': 4.0}]}, construcciones.Producto, {'key': [2.0, 3.0]}]})

    def test_parsear_serialize(self):
        self.assertTrue(self.parser.serialize([]), '$0=[]')
        self.assertTrue(self.parser.serialize({'""': construcciones.Suma([2,3]), 'y':True}), '$0={"y":true, "\"\"":$1=Suma(2,3)}' )
        a = []
        s = construcciones.Suma([2, 3])
        a.append(s), a.append(s)
        self.assertTrue(self.parser.serialize(a),'$0 = [$1 = Suma(2, 3)]')
        self.assertTrue(self.parser.serialize({'idObj0': construcciones.Suma([2, 3]), 'dict2': [{'dict3': 3}, 5, 6, construcciones.Point2D(1, 2)]}), '$0={"idObj0":$1=Suma(2,3), "dict2":$2=[$3={"dict3":3},5,6,$4=Point2D(1, 2)]}')
        self.assertTrue(self.parser.serialize([]), '$0=[]')

    def test_parsear_materialize_serialize(self):
        self.assertTrue(self.parser.serialize(parser.parsear("$id=Suma(2,3,4,5)")),construcciones.Suma([2.0,3.0,4.0,5.0]) )
        self.assertTrue(self.parser.serialize(parser.parsear("$idObj1={key:[$id1=[2,3]], key2: [ Point2d(2,3),{key3:4}, Producto(7,8,9)] }")),{'idObj1': [{'key2': [construcciones.Point2D(2,3),{'key3': 4.0}]}, construcciones.Producto, {'key': [2.0, 3.0]}]} )
        self.assertTrue(self.parser.parsear(parser.serialize({'""': construcciones.Suma([2,3]), 'y':True})),{'""': construcciones.Suma([2,3]), 'y':True} )
        self.assertTrue(self.parser.parsear(parser.serialize({'idObj0': construcciones.Suma([2, 3]), 'dict2': [{'dict3': 3}, 5, 6, construcciones.Point2D(1, 2)]})), '$0={"idObj0":$1=Suma(2,3), "dict2":$2=[$3={"dict3":3},5,6,$4=Point2D(1, 2)]}')
        self.assertTrue(parser.serialize({'""': construcciones.Producto([2,3]), 'y':True}), parser.serialize(parser.parsear('$0={"y":true, id:$1=Producto(2,3)}')) )

if __name__ == '__main__':
    unittest.main(verbosity=2)

testClass = Test_Parser_Serialize_Methods()
testClass.run()
