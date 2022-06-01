class Persona:
    sexo="mujer"
    origen="italia"
#no es necesario declarar la propiedad que pasamos como parámetro en el constructor

#constructor
    def __init__(self,nombre):
        print("construyendo")
        self.nombre=nombre



#getters / setters - encapsulamiento

#methods
    def saludar(self):
        print("la persona saluda")