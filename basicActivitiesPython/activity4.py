"""
alumnos son: juan, maria, pedro, laura, manuel
asignaturas son programacion, bases de datos, diseño de interfaces, despliegue de aplicaciones

"""
import statistics

import notas as notas

matrix = [
    {"juan": {"programacion": 7, "bases de datos": 8.5, "di": 9, "despliegue": 8}},
    {"maria": {"programacion": 5, "bases de datos": 5.5, "di": 9, "despliegue": 8}},
    {"pedro": {"programacion": 7, "bases de datos": 8.5, "di": 9, "despliegue": 4}},
    {"laura": {"programacion": 6, "bases de datos": 8.5, "di": 3, "despliegue": 4}},
    {"manuel": {"programacion": 7, "bases de datos": 6.5, "di": 6, "despliegue": 6}}

]
# nota media del alumno
for alumno in matrix:
    for alumno, notas in alumno.items():
            print(alumno)
            print(notas)

            total = (sum(notas.values()))
            print(total)

            media = total / len(notas)
            print(media)

# nora media por asignatura
"""
prog, bbdd,di, desp = 0, 0, 0,0
print("----Media por alumno----")
for alumno in matrix:
    for alumno, notas in alumno.items():
        print("Media de", alumno.capitalize(), sum(notas.values()) / len(notas))
        prog = prog + notas["programacion"]
        bbdd = bbdd + notas["base de datos"]
        di = di + notas["di"]
        desp = desp + notas["despliegue"]
print("----Media por asignatura----")
print("Media Programación:", prog / len(matrix))
print("Media Base de datos:", bbdd / len(matrix)*4))
prog, bbdd,di, desp = 0, 0, 0,0
print("----Media por alumno----")
for alumno in matrix:
    for alumno, notas in alumno.items():
        print("Media de", alumno.capitalize(), sum(notas.values()) / len(notas))
        prog = prog + notas["programacion"]
        bbdd = bbdd + notas["base de datos"]
        di = di + notas["di"]
        desp = desp + notas["despliegue"]
print("----Media por asignatura----")
print("Media Programación:", prog / len(matrix))
print("Media Base de datos:", bbdd / len(matrix))
print("Media Despliegue:", desp / len(matrix))
print("Media Desarrollo de interfaces:", di / len(matrix))
print("----------------------------")
print("Media total del curso", (prog + bbdd + desp + di) / (len(matrix) * 4))
"""
# nota media del curso

media = 0
for alumno in matrix:
    for alumno, notas in alumno.items():
        print(alumno)
        print(sum(notas.values())/len(notas))
        media += sum(notas.values())/len(notas)
print (f"Media total {media/5}")




"""
for alumno in matrix:
   for alumno,notas in alumno.items():
       print(alumno)
       print(notas)
"""
