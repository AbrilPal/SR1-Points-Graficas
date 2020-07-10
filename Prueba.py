# Andrea Abril Palencia Gutierrez, 18198
# SR1: Points --- Graficas por computadora, seccion 20
# 07/07/2020 -- 13/07/2020

# importar mis funciones de points.py
from points import Render, color, convertir

# ancho y alto de la imagen
ancho = int(input("Ingrese el ancho deseado de la imagen: "))
alto = int(input("Ingrese el alto deseado de la imagen: "))
# ancho y alto de ViewPort
print("****************** ViewPort ******************")
ancho_v = int(input("Ingrese el ancho del ViewPort: "))
alto_v = int(input("Ingrese el alto del ViewPort: "))
# posicion del ViewPort
x_v = int(input("Ingrese la posicion en 'x' del ViewPort: "))
y_v = int(input("Ingrese la posicion en 'y' del ViewPort: "))
# posicion del punto
print("****************** Punto ******************")
x = float(input("Ingrese la posición en 'x' del punto: "))
y = float(input("Ingrese la posición en 'y' del punto: "))

# color de fondo
print("****************** Color de fondo ******************")
print("Los parámetros deben ser números en el rango de 0 a 1.")
rojo = float(input("Rojo: "))
verde = float(input("Verde: "))
azul = float(input("Azul: "))

# convertir color de fondo
rojo_f = convertir(rojo)
verde_f = convertir(verde)
azul_f = convertir(azul)

# color del punto
print("****************** Color del punto ******************")
print("Los parámetros deben ser números en el rango de 0 a 1.")
rojo = float(input("Rojo: "))
verde = float(input("Verde: "))
azul = float(input("Azul: "))

# convertir color del punto
rojo_p = convertir(rojo)
verde_p = convertir(verde)
azul_p = convertir(azul)

# crear la imagen
imagen = Render(ancho, alto, color(rojo_f,verde_f,azul_f))
imagen.glViewPort(x_v, y_v, ancho_v, alto_v)
imagen.glColor(color(rojo_p,verde_p,azul_p))
imagen.glVertex(y,x)
imagen.glFinish('punto.bmp')
print("¡Listo! La imagen esta creada con el nombre de 'punto.bmp'.")