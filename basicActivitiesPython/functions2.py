def saludar(nombre,apellidos="Lopez"):
    return f'hola\nque tal {nombre}'

def ciudades(ciudad,todas=[]):
    print(ciudad)
    todas.append((ciudad))
    print(todas)

#llamda a la funcion
mensaje=saludar("juan", "garcia")
print(mensaje)

ciudades("madrid")
ciudades("sevilla")