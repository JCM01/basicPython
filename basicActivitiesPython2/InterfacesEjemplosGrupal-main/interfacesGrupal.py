"""
Interfaz define al conjunto de métodos que tiene que tener un objeto para que pueda cumplir una determinada función en nuestro sistema.

Piensa en el mando a distancia del televisor. Todos los mandos nos ofrecen el mismo interfaz con las mismas funcionalidades o métodos.
Es importante notar que los interfaces no poseen una implementación per se, es decir, no llevan código asociado.
El interfaz se centra en el qué y no en el cómo.
Se dice entonces que una determinada clase implementa una interfaz, cuando añade código a los métodos que no lo tenían (denominados abstractos).
Es decir, implementar un interfaz consiste en pasar del qué se hace al cómo se hace.
"""
"""
Informales
"""
class Mando:
    def siguiente_canal(self):
        pass
    def canal_anterior(self):
        pass
    def subir_volumen(self):
        pass
    def bajar_volumen(self):
        pass

class MandoSamsung(Mando):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")

class MandoLG(Mando):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")

from abc import ABC
from abc import abstractmethod
class MandoFormal(ABC):
    @abstractmethod
    def siguiente_canal(self):
        pass

    @abstractmethod
    def canal_anterior(self):
        pass

    @abstractmethod
    def subir_volumen(self):
        pass

    @abstractmethod
    def bajar_volumen(self):
        pass
class MandoSamsungFormal(MandoFormal):
    def siguiente_canal(self):
        print("Samsung->Siguiente")
    def canal_anterior(self):
        print("Samsung->Anterior")
    def subir_volumen(self):
        print("Samsung->Subir")
    def bajar_volumen(self):
        print("Samsung->Bajar")
class MandoLGFormal(MandoFormal):
    def siguiente_canal(self):
        print("LG->Siguiente")
    def canal_anterior(self):
        print("LG->Anterior")
    def subir_volumen(self):
        print("LG->Subir")
    def bajar_volumen(self):
        print("LG->Bajar")

mando_lg_formal = MandoLGFormal()
mando_lg_formal.bajar_volumen()

mando_samsung_formal = MandoSamsungFormal()
mando_samsung_formal.bajar_volumen()

