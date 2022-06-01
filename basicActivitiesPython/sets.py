"""
https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""
#Lista anidada / matrix
import operator
from itertools import count

ciudades=[
    ["madrid","sevilla"],
    ["roma","milan"],
    ["moscú","kiev"]
]

ciudades.append(["berlin"])
print(ciudades)
for pais in ciudades:
    for i in pais:
        print(i)
#tupla
datos=10,"madrid",True,14.95
print(datos)

#sets no ordenado y sin duplicados
equipos={"rm","barcelona","atleti","betis",15}
print(equipos)

#diccionario
liga={
    "madrid":30,
    "barcelona":25,
    "atleti":50,
    "betis":42,
    "mallorca":15
}
print(liga)
liga["betis"]=45 #update value
print(liga)
for k,v in liga.items():
    print(k,"--",v)

#reto1 ordena la liga por puntos
liga_sorted=sorted(liga.items(),key=operator.itemgetter(1),reverse=True)

for k,v in enumerate(liga_sorted):
    print(k,"--",v)

#tuplas con inmutables
tupla1=(2,"madrid",True,95)
#tupla1[0]=3 #tupla es inmutable
print(tupla1[0])
#tupla1.__add__()

#sets NO pueden tener valores duplicados
set={10,"madrid",False,19.54,10,False}
#no soporta duplicados, pero NO te da error
set.add("otra")
set.pop()
print(set)

#almacenar 5 alumnos con 4 asignaturas : notas del 0 al 10
#media de nota por alumno
#media de nota de la clase
#alumnos son : juan, maria, pedro, laura, manuel
#asignaturas son programacion. bases de datos, diseño de interfaces, despliegue de aplicaciones
#listas / tuplas / set / dictionary

alumnos={
    "juan": [45,75,80,55],
    "maria": [65,40,71,82],
    "pedro": [80,53,84,90],
    "laura": [76,90,32,83],
    "manuel": [84,65,12,50]
}

print(alumnos)