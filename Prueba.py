# Andrea Abril Palencia Gutierrez, 18198
# SR1: Points --- Graficas por computadora, seccion 20
# 07/07/2020 -- 13/07/2020

# importar mis funciones de points.py
from points import Render, color

imagen = Render(200,200, color(0,255,0))

imagen.glColor(color(0,0,255))

imagen.glVertex(10,100)
   

imagen.glFinish('punto.bmp')