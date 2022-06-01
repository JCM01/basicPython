"""
similar "main" de java
"""
import moduleb
from package1 import Persona,Stakeholders

print(modulob.sumar(5,8))
#Persona persona1= new Persona() #instanciar una clase con notación de funcion
persona1 = Persona.Persona("maria") #constructor pasando un parámetro
persona1.saludar()
print(persona1.origen) #get de una propiedad. lectura
persona1.origen="francia" #set de una propiedad. escritura
print(persona1.origen)
#el acceso de lectura/escritura de las propiedades /fields recomendable con encapsulamiento
#getters / setters
print(persona1.nombre)

cliente1=Stakeholders.Clientes("indra",1500)
proveedor1=Stakeholders.Proveedores("telefonica")
proveedor1.saludar()