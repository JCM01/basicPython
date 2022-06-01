class Jugador:

    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

    def saludar(self):
        print("Hola "+self.nombre)

class Futbolista(Jugador):

    def __init__(self, equipo):
        self.equipo = equipo

    def jugar(self):
        print("jugando en el "+ self.equipo)

    def saludar(self):
        print("saludando en el "+self.equipo)
"""
Esto se le denomina sobreescritura, pero en Python es diferente al que sabemos 
"""

futbolista_ = Futbolista("Madrid")

futbolista_.saludar()
futbolista_.jugar()