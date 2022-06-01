"""
Ejercicio 1 - Crear una clase llamada Alumno
En su constructor indicas el nombre y el grado que estudia el alumno.
Los alumnos tienen métodos como comer y dormir. Estos métodos vienen de la clase Persona.
Los alumnos tienen métodos como correr y saltar. Estos métodos vienen de la clase Jugador.
¿qué característica estás utilizando?

"""
from modules import Persona, Jugador


class Alumno(Persona, Jugador):

    def __init__(self, nombre, grado):
        self.nombre = nombre
        self.grado = grado
