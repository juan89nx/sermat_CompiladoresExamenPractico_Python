# Created by: Juan Perciante
# July 2016

from abc import ABCMeta, abstractmethod, abstractproperty
#Construir instamncia de clase sin iniciarla!!!
#Se debe modificar la gramatica para permitir esto con las construcciones
#__new__ se utiliza para crar una instancia
#despues se usa init para cuando se la quiere iniciar
# -> When to use __new__ vs __init__

class Construcciones:
    def __init__(self):
        # When a new function is defined, it must be added in the following list
        self.listaDeConstrucciones = {
            "Suma": Suma_Construction(),
            "Producto": Producto_Construction(),
            "Tuple": Tuple_Construction(),
            "Point2D": Point2D_Construction()
        }

    def addToListaDeConstrucciones(self):
        self.listaConstrucciones.append()

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

class Point2D_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "Point2D"

    def serialize(self, objeto):
        return [self.x, self.y]

    def materialize_new(self):
        return Point2D.__new__(Point2D)

    def materialize(self, obj, valores):
        return Point2D.__init__(obj, valores[0], valores[1])


class Suma(object):
    def __init__(self, listaValores):
        self.listaValores = listaValores

class Suma_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "Suma"

    def serialize(self, objeto):
        return self.listaValores

    def materialize_new(self):
        return Suma.__new__(Suma)

    def materialize(self, obj, listaValores):
        Suma.__init__(obj, listaValores)
        return obj


class Producto(object):
    def __init__(self, listaValores):
        if ((len(listaValores)) == 1):
            self.valorFinal = listaValores[0]
            return self.valorFinal
        if ((len(listaValores)) > 1):
            self.valorFinal = listaValores[0]
            for i in range(1, len(listaValores)):
                self.valorFinal = self.valorFinal * listaValores[i]
            return self.valorFinal

class Producto_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "Producto"

    def serialize(self, objeto):
        pass

    def materialize_new(self):
        return Producto.__new__(Producto)

    def materialize(self, obj, listaValores):
        return Producto.__init__(obj, listaValores)


class Tuple(object):
    def __init__(self, listaValores):
        return tuple(listaValores)

class Tuple_Construction(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "Tuple"

    def serialize(self, objeto):
        pass

    def materialize_new(self):
        return Tuple.__new__(Tuple)

    def materialize(self, obj, listaValores):
        return Tuple.__init__(obj, listaValores)
