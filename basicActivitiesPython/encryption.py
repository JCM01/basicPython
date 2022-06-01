"""
Cifrado de cesar en Python

1. crea un funcion con dos parametros
primer parametro es un texto
segundo parametro es el salto
bucle for in muestra por consola el texto encriptado

2. crea otra función para desencriptar con dos parámetros
primer parámetro es el texto encriptado
segundo parámetro es el salto
bucle y muestra el texto desencriptado
"""

def encriptar(texto,salto):
    mensaje_encriptado=""
    for c in texto:
        mensaje_encriptado+=chr((ord(c)+salto))
    print(mensaje_encriptado)

def desencriptar(texto,salto):
    mensaje_final=""
    for c in texto:
        mensaje_final+=(chr(ord(c)-salto))
    print(mensaje_final)

encriptar("hola",3)
desencriptar("krod",3)











