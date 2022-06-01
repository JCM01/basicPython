"""
actividad 1
a. Almacena en un "lista" las temperaturas de las siguientes ciudades
madrid 12,5
sevilla 24,9
lugo 8,75
valencia 25,8
córdoba 31,8

"""
import operator

diccionario= {
    "madrid" : 12.5,
    "sevilla" : 24.9,
    "lugo": 8.75,
    "valencia" : 25.8,
    "cordoba" : 31.8
}
print(diccionario.items())

total= sum(diccionario.values())
print(total/len(diccionario))

diccionario['zaragoza']= 20.7
print(diccionario.items())

del diccionario['lugo']
print(diccionario.items())

total= sum(diccionario.values())
print(total/len(diccionario))

temperaturas_sort = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
for name in enumerate(temperaturas_sort):
    print(name[1][0], 'tiene', diccionario[name[1][0]])

