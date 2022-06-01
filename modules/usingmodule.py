import modulo1

#import tienda.comprar
from Coche import Coche
from tienda import comprar
#from calendar import comprar



modulo1.saludar("juan")
print(modulo1.__name__)

comprar.pagar()

coche1 = Coche()
print(coche1.nombre)
coche1.aparcar()