# Andrea Abril Palencia Gutierrez, 18198
# SR1: Points --- Graficas por computadora, seccion 20
# 07/07/2020 -- 13/07/2020

# importar mis funciones de points.py
from points import Render, color

# 
ancho = int(input("Ingrese el ancho deseado de la imagen: "))
alto = int(input("Ingrese el alto deseado de la imagen: "))
x = int(input("Ingrese la posición en 'x' del punto: "))
y = int(input("Ingrese la posición en 'y' del punto: "))

# crear la imagen
imagen = Render(ancho, alto, color(0,255,0))
imagen.glColor(color(0,0,255))
imagen.glVertex(y,x)
imagen.glFinish('punto.bmp')