from points import Render, color

imagen = Render(200,200)

imagen.glColor(color(0,0,255))

imagen.glVertex(10,100)
   

imagen.glFinish('punto.bmp')