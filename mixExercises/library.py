"""
Para instalar una nueva librería en nuestro entorno Python,
la ejecutamos desde nuestra terminal de Windows los siguientes comandos.
py -m pip install --upgrade pip
py -m pip install --upgrade Pillow
Una vez instalada abrimos Pycharm y usamos "from PIL import Image" para
usar nuestra librería
"""

#py -m pip install --upgrade pip
#py -m pip install --upgrade Pillow


from PIL import Image

im = Image.open('img/imagen1.jpg')
print(im.size)
imnuevo = (500, 400)
im = im.resize(imnuevo)
print(im.size)
im.show()

im = Image.open('img/imagen2.png')
print(im.size)
imnuevo = (400, 300)
im = im.resize(imnuevo)
print(im.size)
im.show()

"""
Unas de las librerías para usar webscraping

Scrapy

Instalación con Scrapy: 

Aunque es posible instalar Scrapy en Windows usando pip, 
le recomendamos que instale Anaconda o Miniconda y 
use el paquete del canal conda-forge, 
lo que evitará la mayoría de los problemas de instalación.

Una vez que haya instalado Anaconda o Miniconda, instale Scrapy con:

#conda install -c conda-forge scrapy
o
#pip install scrapy -> en anaconda prompt


Para instalar Scrapy en Windows usando pip:

Advertencia

Este método de instalación requiere 
"Microsoft Visual C ++" para instalar algunas dependencias de Scrapy, 
lo que exige mucho más espacio en disco que Anaconda.
Descargue y ejecute Microsoft C ++ Build Tools para instalar Visual Studio Installer.



"""
#Aqui mismo está el método de la librería Scrapy
#En la carpeta Scrapy se encuentra unos recortes de pantalla de como se ha
# ejecutado Scrapy
#print(response.text)
#imagen adjuntas 


