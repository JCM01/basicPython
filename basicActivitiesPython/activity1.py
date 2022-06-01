import time

"""
Actividad 1
Pide un número por consola.
Si es un 9 o superior muestra el texto Sobresaliente
si es mayor o igual de 5 y menor de 9, muestra el texto aprobado
si es menor de 5, muestra suspenso

"""


def Numero1():
    n = int(input("Dime un numero"))
    print(n)

    if n >= 9 and n <= 10:
        print("sobresaliente")

    elif n >= 5 and n < 9:
        print("aprobado")

    elif n < 5:
        print("suspenso")
    else:
        print("no valido")


# Numero1()

"""
Actividad 2
bucle for "clasico" NO existe en Python
i++ funciona? por qué?
mostrar los números impares que hay en los 100 primeros números
muestra cuánto tiempo ha tardado en ejecutarse ese programa
"""
"""
numero = 0
t = time.time_ns()

while numero < 100:
    numero += 1
    if numero % 2 != 0:
        print(numero, "---%s segundos ---" % (time.time_ns() - t))
"""
"""
Actividad 3
gauss - video : puedes buscar el vídeo en internet
programa una función que realiza la suma de los 100 primeros números
"""
"""
resultado = 0
i = 0
while i <= 100:
    print(i)
    resultado += i
    i += 1
    print("Es la suma acumulada del 1 a 100 =% d" % resultado)
    
    print(sum
"""
"""
Actividad 4
Por consola te pide las unidades y luego el precio
si las unidades son mayor de 10 tienes un descuento del 20%
Muestra por consola el total y el total con el iva (21% por defecto).
Programa la función para permitir modificar el tipo de descuento y el tipo de iva
"""
def producto(descuento=0.20, iva=1.21):
    unidades=int(input("Dime las unidades "))
    precio=float(input("Dime el precio "))
    
    if unidades>10:
        total=(unidades*precio)-(unidades*precio*descuento)
    else:
        total=unidades*precio
    print("Precio sin iva:",total)
    totalIva=total*iva
    print("Precio con iva:",totalIva)
#producto()

"""
Actividad 5
Por consola realizas una pregunta en donde el usuario debe responder
Sigue mostrando la pregunta hasta que el usuario responde
*(complicado) : si han pasado 10 segundos, aparece time over y se cierra la consola
"""
import time
def tiempo():
    numero = 0
    while numero != 2:
        inicio = time.time()
        print("Dime la suma de 1+1")
        numero = int(input())
        end = time.time()
        total = end - inicio
        if(total>10):
            print("se acabo el tiempo")
            break
        if (numero==2):
            print("respuesta correcta")
#tiempo()
