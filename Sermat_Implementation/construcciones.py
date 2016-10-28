# Created by: Juan Perciante
# July 2016

from abc import ABCMeta, abstractmethod, abstractproperty


class Construcciones:
    def __init__(self):
        # When a new function is defined, it must be added in the following list
        self.listaDeConstrucciones = {
            "suma": Suma(),
            "producto": Producto(),
            "tuple": Tuple()
        }

    def addToListaDeConstrucciones(self):
        self.listaConstrucciones.append()

    def construirEnBaseAFuncion(self, id_Construction, listaAtributosParaConstruccion):
        if (self.listaDeConstrucciones.has_key(id_Construction) ):
            construction = self.listaDeConstrucciones[id_Construction]
            retornoDeConstruccion = construction.materialize(listaAtributosParaConstruccion)
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

    @abstractmethod  # recibe los valores, y devuelve un objeto
    def materialize(self, listaValores):
        pass


class Suma(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "suma"

    def serialize(self, objeto):
        pass

    def materialize(self, listaValores):
        if (len(listaValores) >= 1):
            valorFinal = 0
            for valor in listaValores:
                valorFinal += valor
            return valorFinal


class Producto(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "producto"

    def serialize(self, objeto):
        pass

    def materialize(self, listaValores):
        if ((len(listaValores)) == 1):
            valorFinal = listaValores[0]
            return valorFinal
        if ((len(listaValores)) > 1):
            valorFinal = listaValores[0]
            for i in range(1, len(listaValores)):
                valorFinal = valorFinal * listaValores[i]
            return valorFinal


class Tuple(IConstruction):
    def __init__(self):
        IConstruction.__init__(self)

    @property
    def id_Construction(self):
        return "tuple"

    def serialize(self, objeto):
        pass

    def materialize(self, listaValores):
        return tuple(listaValores)
