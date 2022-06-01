"""
Gestión de librerías
a. El alumno utiliza una librería de Python para gestionar imágenes. Indica al menos tres librerías para gestionar imágenes (5 puntos)
NumPy
PIL
Scikit -image

b. Muestra en consola una imagen de formato gif. controla la excepción si no encuentra la imagen (5 puntos)
c. Redimensiona la imagen anterior a 50*50 (5 puntos)

"""

from PIL import Image

im = Image.open('img/hola.gif')

im.show()