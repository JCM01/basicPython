"""
Metodos en las listas

"""


def listas():
    elementos = ["madrid", 100, True, 9.95, 'juan', "valencia", "juan"]
    print(elementos)
    print(elementos.count("juan"))
    print(elementos.index("juan"))
    # elementos.reverse()
    print(elementos)
    print(elementos.index("juan"))
    elementos.append("zaragoza")
    print(elementos)
    elementos.pop()
    print(elementos)
    elementos.pop(2)
    print(elementos)
    elementos.remove("maddid")
    print(elementos)


# listas()

"""
pilas LIFO
colas FIFO : menos eficiente : append/pop colocarlos al inicio es mas lento
"""

from collections import deque  # por defecto, Python no trae las queues cargadas


def colas():
    datos = deque(["rojo", "verde", "azul"])
    print(datos)
    datos.append("amarillo")
    print(datos)
    datos.popleft()  # elimina FIFO
    print(datos)


# colas()

import time


def manipular_for():
    inicio = time.time_ns()
    cubo = []
    for i in range(0, 1000):
        cubo.append(i ** 3)
    print(cubo)
    fin = time.time_ns()
    print(fin - inicio)


#manipular_for()

def manipular_map():
    inicio = time.time_ns()
    cubo = list(map(lambda i: i**3, range(0,1000))) #programacion funcional
    print(cubo)
    fin = time.time_ns()
    print(fin - inicio)


#manipular_map()

"""
Crea un funcion para calcular el iva 21% de los importes 500, 1000, 1500, 2000...
asi hasta 1000000 
Suma de todos los importes
Promedio de los importes
mediante pop eliminar el primer importe

"""
def calcular():
    importes=[]
    for i in range(0,1000000,500):
        importes.append(importes)
        print(importes)



calcular()
