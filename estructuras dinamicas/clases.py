class Cancion():
    def __init__(self):
        self.nombre = str
        self.artista = str
        self.like = int

class nodolista(object):
    info,siguente =None, None
    
class lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0

class nodoCola(object):
    info, siguiente = None, None

class Cola(object):
    def __init__(self):
        self.entrada, self.salida = None, None
        self.tamanio = 0

class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class nodoPila(object):
    info, siguiente = None, None

class Pila(object):
    def __init__(self):
        self.cima = None
        self.tamanio = 0

