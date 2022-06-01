from PIL import Image
#py -m pip install --upgrade pip
#py -m pip install --upgrade pillow


tamaño=(100,50)
ubicacion = "C:\\Users\\Campus FP\\Downloads\\logo.png" #sirve tanto esta barra
imagen = Image.open(ubicacion)
imagen.thumbnail(tamaño)
imagen.save("C:\\Users\\Campus FP\\Downloads\\logo2.png") #como con doble barra
imagen.show()