from abc import ABC, abstractmethod


class PlatosPreparados(ABC):
    def bebidas(self): #se puede usar directamente NO es abstracta
        print("sirviendo bebidas")

    @abstractmethod
    def ensaldas(self):
        print("preparar ensalada")
        #falta aliñar ensalada

class Vegano(PlatosPreparados):
    def ensaldas(self):
        #super().ensaldas()
        print("meto ingredientes veganos")
        print("aliñar la ensalada y servir")