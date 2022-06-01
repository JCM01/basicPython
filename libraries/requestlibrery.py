import requests as requests

#datos = requests.get("http://www.bne.es/es/Inicio/index.html")
datos = requests.get("localhost: 3306")
print(datos)
print("-----------------------------------------")
print(datos.cookies)
print("-----------------------------------------")
print(datos.text)
