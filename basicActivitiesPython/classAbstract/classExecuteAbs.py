#usar las clases
from classAbstract import PlatosPreparados, Vegano

#bebidas=PlatosPreparados() #instanciar clase abstracta pero NO da error porque todos sus métodos NO son abstractos
#bebidas.bebidas()
#bebidas.ensaldas() #no se puede usar directamente porque es un método abstracto
vegano=Vegano()
vegano.ensaldas()