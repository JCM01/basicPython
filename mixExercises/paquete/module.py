
import time

print(time.strftime("%Y-%m-%d %H:%M:%S"))


def funcion1(inicio, fin):
    for i in range(inicio, fin):
        if i % 2 != 0:
            print(i)
            if i == 55:
                break
def funcion2(n):
    if (n%7 ==0):
        print("true")
    else:
        print("false")

def funcion3(t):
    lista = []
    lista.append(t.count("a"))
    lista.append(t.count("e"))
    lista.append(t.count("i"))
    lista.append(t.count("o"))
    lista.append(t.count("u"))
    print("El numero de vocales del texto es: "+ (str)(sum(lista)))

funcion1(3, 14)
funcion2(3)
funcion3("uno dos tres")