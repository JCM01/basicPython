from datetime import datetime


def saludar(nombre):
    numero:int = 15
    precio:decimal = 5.95
    total:decimal

    if(numero>10):
        total=numero*precio*0.9
    else:
        total=numero*precio


    print(f'hola {nombre}') #binding
    print(f'el total es {numero*precio}')

saludar('juanito')
#ejercicio1

for i in range(1,11):
    print(i)
#ejercicio2

print('Dime la ciudad')
ciudad =input()
if(ciudad=='madrid'or'servilla'):
    print("es madrid")
else:
    print("es sevilla")
#ejercicio3

asignaturas=[ 'ingles','mates','geografia', 'ciencias']

print(sorted(asignaturas))

#ejercicio4

print('Dime un numero con 5 decimales')
n=float(input())
print(round(n,2))

#ejercicio5

ahora= datetime.now()
formato=ahora.strftime('%d/%m/%y')
print(formato)
