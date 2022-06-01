"""
Ejercicio1
Vamos a almacenar los artículos que has elegido:
camisa, pantalón, sombrero, chaqueta, bufanda, zapatos
Muestra cuántos artículos tienes
Cambia el sombrero por gorra
¿Qué has elegido?
"""
lista=["camisa", "pantalon","sombrero","chaqueta","bufanda", "zapatos"]
print(lista)
lista[2]="gorra"#lista es mutable, puede cambiar el valor de sus datos
print(lista)
"""
Ejercicio2
Vamos a almacenar los artículos que has elegido:
camisa, pantalón, sombrero, chaqueta, bufanda, zapatos
Muestra cuántos artículos tienes
¿Qué has elegido?
"""

diccionario={"1":'camisa',"2": 'pantalon',"3":'sombrero',"4":'chaqueta',"5":'bufanda',"5":'zapatos'}
print(diccionario)
print(diccionario.keys()) #return los items

"""
Ejercicio3
Vamos a almacenar los artículos que has elegido:
camisa, pantalón, sombrero, chaqueta, bufanda, zapatos
Muestra cuántos artículos tienes
la camisa cuesta 15.75, pantalón 8.95, sombrero 10, chaqueta 74.95, gufanda 9.98, zapatos 32.95
Muestra  el precio medio de los productos
Muestra el total del importe de todos los productos
¿Qué has elegido?
"""
lista=["camisa", "pantalon","sombrero","chaqueta","bufanda", "zapatos"]
print(lista)
numerolista = len(lista)
print("Numero de elementos: ",numerolista)

diccionario={"camisa":"","pantalon": "","sombrero":"","chaqueta":"","bufanda":"","zapatos":""}
print(diccionario)
print(len(diccionario))
diccionario["camisa"]=15.75
diccionario["pantalon"]=8.95
diccionario["sombrero"]=10
diccionario["chaqueta"]=74.95
diccionario["bufanda"]=9.98
diccionario["zapatos"]=32.95
print(diccionario)
total=sum(diccionario.values())
print(total/len(diccionario))
sum(diccionario.values())

print(sum(diccionario.values()))