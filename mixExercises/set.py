diccionario = {"tejidos SL":147.96,"compras SL":852.14,
               "pepe SA":852.45,"maria SL":123.74,"ventas SL":654.85}

print(diccionario)

total = sum(diccionario.values())
media = total/len(diccionario.values())
print(media)

del diccionario["tejidos SL"]
diccionario["telas SA"] = 35.96

print(diccionario)

diccionario_ordenado = sorted(diccionario)
print(diccionario_ordenado)
"""
la función sorted() sirve para ordenar alfabeticamente en orden ascendente,
creamos una varible nueva llamada diccionario_ordenado y pasamos la función
sorted() con el nuestro diccionario.

"""

