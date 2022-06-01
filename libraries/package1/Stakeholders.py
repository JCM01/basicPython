from package1.Persona import Persona


class Clientes(Persona):#herencia Clientes es una clase derivada de la clase padre Persona

    def __init__(self,nombre,facturacion):
        self.nombre=nombre
        self.facturacion=facturacion


class Proveedores(Persona):
    def __init__(self,nombre):
        self.nombre=nombre


