from Polimorfismo.Padre import Animal


class Perro(Animal):
    def andar(self):
        print("Estoy andando a 4 patas")

class Pato(Animal):
    def andar(self):
        print("Estoy andando a 2 patas")


for Animal in Perro(), Pato():
    Animal.andar()
