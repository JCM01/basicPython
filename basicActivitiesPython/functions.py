"""
python. control de flujo y bucles
https://docs.python.org/es/3/tutorial/controlflow.html

"""
import time
import datetime
print(time.time())
print(datetime.date.today())

def condicionalIf():
    numero = int(input("dime un número"))
    print(numero)
    if numero < 0:
        print("número negativo")
    elif numero == 10:
        print("numero 10")
    else:
        print("numero positivo")


#condicionalIf()


#buclesfor

def bucleFor():
    datos = ["madrid", 15, 9.95, True]
    print(datos)
    for item in datos:
        print(str(item).upper())


#bucleFor()

def bucle10():
    for i in range(0, 100, 2):
        print(i)


#bucle10()

def bucleBreak():
    for i in range(20):
        if (i==8):
            print("es el 8")
            break  # sale del bucle en donde esté anidado
        print(i)


#bucleBreak()

def calcular(unidades, precio,iva=1.21):
    return  unidades*precio*iva

#total=calcular(100,9.85)
#print(total)

print(time.time())