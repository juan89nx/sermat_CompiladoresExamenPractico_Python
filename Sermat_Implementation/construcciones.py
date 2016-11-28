# Created by: Juan Perciante
# December 2016

from abc import ABCMeta, abstractmethod, abstractproperty

class Construcciones:
    def __init__(self):
        # When a new Construction is defined, it must be added in the following list
        self.listaDeConstrucciones = {
            "Suma": Suma_Construction(),
            "Producto": Producto_Construction(),
            "Tuple": Tuple_Construction(),
            "Point2D": Point2D_Construction()
        }

    def devolverInstanciaSiExiste(self, id_Construction):
        if (self.listaDeConstrucciones.has_key(id_Construction)):
            instancia_new = self.listaDeConstrucciones[id_Construction].materialize_new()
            return instancia_new

    def construirEnBaseAFuncion_Materialize(self, id_Construction, instancia , listaAtributosParaConstruccion):
        if (self.listaDeConstrucciones.has_key(id_Construction) ):
            construction = self.listaDeConstrucciones[id_Construction]
            retornoDeConstruccion = construction.materialize(instancia, listaAtributosParaConstruccion)
            return retornoDeConstruccion
        else:
             return "id_Construction doesn't exist"


    def serializeGenerico(self, obj):
        typeSerializer = type(obj)
        id_construction = typeSerializer.myTypeInString(obj)
        if ( self.listaDeConstrucciones.has_key(id_construction) ):
            serializer = self.listaDeConstrucciones[id_construction]
            retornoDeSerializacion = serializer.serialize(obj)
            return str(id_construction)+retornoDeSerializacion
        else:
            return "Construction doesn't exist"

class IConstruction(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def id_Construction(self):
        pass

    @abstractmethod  # Recibe objeto, y devuelve los valores
    def serialize(self, objeto):
        pass

    @abstractmethod  # devuelve la instancia sin inicializar
    def materialize_new(self):
        pass

    @abstractmethod  # recibe los valores, y devuelve un objeto
    def materialize(self, listaValores):
        pass

class Point2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def myTypeInString(self):
        return "Point2D"

class Point2D_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    def type(self):
        return Point2D

    @property
    def id_Construction(self):
        return "Point2D"

    def serialize(self, objeto):
        return str((objeto.x, objeto.y))

    def materialize_new(self):
        return Point2D.__new__(Point2D)

    def materialize(self, obj, valores):
        Point2D.__init__(obj, valores[0], valores[1])
        return obj

class Suma(object):
    def __init__(self, listaValores):
        self.listaValores = listaValores

    def myTypeInString(self):
        return "Suma"

class Suma_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "Suma"

    def serialize(self, obj):
        return "(%s)" % ",".join(str(valor) for valor in obj.listaValores)


    def materialize_new(self):
        return Suma.__new__(Suma)

    def materialize(self, obj, listaValores):
        Suma.__init__(obj, listaValores)
        return obj


class Producto(object):
    def __init__(self, listaValores):
        self.listaValores = listaValores

    def myTypeInString(self):
        return "Producto"

class Producto_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    def type(self):
        return Producto

    @property
    def id_Construction(self):
        return "Producto"

    def serialize(self, objeto):
        return "(%s)" % ",".join(str(valor) for valor in objeto.listaValores)

    def materialize_new(self):
        return Producto.__new__(Producto)

    def materialize(self, obj, listaValores):
        Producto.__init__(obj, listaValores)
        return obj

class Tuple(object):
    def __init__(self, listaValores):
        self.listaValores = listaValores

    def myTypeInString(self):
        return "Tuple"

class Tuple_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    def type(self):
        return Tuple

    @property
    def id_Construction(self):
        return "Tuple"

    def serialize(self, objeto):
        return "(%s)" % ",".join(str(valor) for valor in objeto.listaValores)

    def materialize_new(self):
        return Tuple.__new__(Tuple)

    def materialize(self, obj, listaValores):
        Tuple.__init__(obj, listaValores)
        return obj