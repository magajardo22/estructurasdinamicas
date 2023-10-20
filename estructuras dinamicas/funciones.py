import time
import json
import random
from clases import *

num=100

with open("informe/can.json") as archivo:
    dic_canciones = json.load(archivo)

#listas

def imprimir(lista):
    print("\n")
    actual = lista.inicio
    while actual is not None:
        print(actual.info.nombre)
        print(actual.info.artista)
        print(actual.info.like)
        print("____________________________")
        actual = actual.siguiente
        
def insertar(lista, info):
    nodo = nodolista()
    nodo.info = info
    if lista.inicio is None:
        nodo.siguiente = lista.inicio
        lista.inicio = nodo
    else:
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while siguiente is not None:
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        nodo.siguiente = siguiente
        actual.siguiente = nodo
    lista.tamanio += 1
    
def crear_lista(lista):
    b = 0
    for a in dic_canciones:
        if b == num:
            break
        can = Cancion()
        can.nombre = a.get('Cancion')
        can.artista = a.get('Artista')
        can.like = random.randint(0,10000)
        insertar(lista, can)
        b = b + 1

def tamanio(lista):
    return lista.tamanio

def buscar_index(lista, pos):
    contador = 0
    actual = lista.inicio
    while actual is not None:
        if contador == pos:
            print(actual.info.nombre) 
        actual = actual.siguiente
        contador += 1

def eliminar_lista(lista, info):
    data = None
    print(lista.inicio.info.nombre)
    if(lista.inicio.info.nombre == info):
        data = lista.inicio
        lista.inicio = lista.inicio.siguiente
        lista.tamanio -= 1
    else:      
        actual = lista.inicio
        siguiente = lista.inicio.siguiente
        while (siguiente is not None and info != siguiente.info.nombre):
            actual = actual.siguiente
            siguiente = siguiente.siguiente
        if(siguiente is not None):
            data = siguiente.info
            actual.siguiente = siguiente.siguiente
            lista.tamanio -= 1

def buscar(lista, buscado):

    indice = 0
    actual = lista.inicio
    while actual is not None:
        if actual.info.nombre == buscado:
            print("La cancion se encuentra en la pocicion",
indice,"de la lista")
            return True
        actual = actual.siguiente
        indice += 1
    print("No se encontro la cancion")


def buscar_time_l(lista,dato):
    inicio = time.time()
    actual = lista.inicio
    while actual is not None:
        if actual.info.nombre == dato:
            fin= time.time()
            return (fin-inicio)
        actual = actual.siguiente

#colas

def arribo(cola, info):
    nuevoNodo = nodoCola()
    nuevoNodo.info = info
    if cola.salida is None:
        cola.salida = nuevoNodo
    else:
        cola.entrada.siguiente = nuevoNodo
    cola.entrada = nuevoNodo
    cola.tamanio += 1

def atencion(cola):
    info = cola.salida.info
    cola.salida = cola.salida.siguiente
    if cola.salida is None:
        cola.entrada = None
    cola.tamanio -= 1
    return info    

def esVacia(cola):
    return cola.entrada is None

def imprimir_cola(cola):
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        print(info.nombre)
        print(info.artista)
        print(info.like)
        print("______________")
        arribo(colaAuxiliar, info)
    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)

def crear_cola(lista, cola):
    print("\n")
    contador = 0
    actual = lista.inicio
    while contador != 100:
        arribo(cola, actual.info)
        actual = actual.siguiente
        contador += 1

def estimar_tiempo(cola,posicion,tiempo):
    pos = 1
    time = 0
    colaAuxiliar = Cola()
    while not esVacia(cola):
        info = atencion(cola)
        if pos == posicion:
            print(time)
        arribo(colaAuxiliar,info)
        time += tiempo
        pos += 1
    while not esVacia(colaAuxiliar):
        info = atencion(colaAuxiliar)
        arribo(cola, info)

#ArbolBi

def insertarNodo(raiz, info):
    if(raiz is None):
        raiz = nodoArbol(info)
    elif(info.like < raiz.info.like):
        raiz.izq = insertarNodo(raiz.izq,info)
    else:
        raiz.der = insertarNodo(raiz.der,info)
    return raiz

def arbolVacio(raiz):
    return raiz is None

def crear_arbol(lista):
    raiz = None
    contador = 0
    actual = lista.inicio
    while contador < num:
        raiz = insertarNodo(raiz, actual.info)
        actual = actual.siguiente
        contador += 1
    return raiz

def imprimirInOrden(raiz):
    if(raiz is not None):
        imprimirInOrden(raiz.izq)
        print(raiz.info.nombre)
        imprimirInOrden(raiz.der)

def buscarInOrden(raiz,buscar):
    if(raiz is not None):
        fin = buscarInOrden(raiz.izq,buscar)

        if fin is not None:
            return fin

        if raiz.info.nombre == buscar:
            return time.time()
        
        else:
            fin = buscarInOrden(raiz.der,buscar)
            if fin is not None:
                return fin
    

#Pila

def apilar(pila, info):
    nuevoNodo = nodoPila()
    nuevoNodo.info = info
    nuevoNodo.siguiente = pila.cima
    pila.cima = nuevoNodo
    pila.tamanio += 1

def desapilar(pila):
    info = pila.cima.info
    pila.cima = pila.cima.siguiente
    pila.tamanio -= 1
    return info

def esVacia_pila(pila):
    return pila.cima is None

def imprimir_p(pila):
    pilaAuxiliar = Pila()
    while not esVacia_pila(pila):
        info = desapilar(pila)
        print(info.info.nombre)
        apilar(pilaAuxiliar, info)
    while not esVacia_pila(pilaAuxiliar):
        info = desapilar(pilaAuxiliar)
        apilar(pila, info)

def enCima(pila):
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None

def crear_pila(lista,pila):
    contador = 0
    actual = lista.inicio
    while contador < 100:
        apilar(pila,actual)
        actual = actual.siguiente
        contador += 1

def dif_buscar(lista,raiz,dato):
    time1 = buscar_time_l(lista,dato)
    inicio = time.time()
    fin = buscarInOrden(raiz,dato)
    if fin is not None:
        print("lista:",time1, "arbol:",(fin-inicio))
    else:
        print("dato no encontrado")