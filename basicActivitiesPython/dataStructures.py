"""
Lista - tuplas - sets (conjutos) - dictionarios

https://www.educative.io/edpresso/list-vs-tuple-vs-set-vs-dictionary-in-python

"""
"""
listas
"""
lista=["madrid", True,10,9.54,'sevilla']
print(lista)
lista[2]="dato modificado"#lista es mutable, puede cambiar el valor de sus datos
print(lista)

"""
tuplas

"""
tupla=("madrid", True,10,9.54,'sevilla')
print(tupla)
#tupla(2)="dato modificado"#tupla es inmutable y NO puede cambiar el valor
print(tupla)

"""
sets - conjuntos
"""
conjunto={"madrid", True,10,9.54,'sevilla'}
print(conjunto)
#conjunto[2]="dato modificado"#cuidado, es mutable pero el error viene porque no puede identificarle
#set es un conjunto de datos desordenados
print(conjunto)
conjunto.add("dato añadido")#conjunto de mutable pero no tiene orden
print(conjunto)

"""
dictionary
"""
diccionario={"item1":"madrid","item2": True,"item3":10,"item4":9.54,"item5":'sevilla'}
print(diccionario)
print(diccionario.keys()) #return los items
print(diccionario.values()) #return los valores
print(diccionario.items())
diccionario["item2"]="dato modificado"# es mutable para valores por keys ***
print(diccionario)