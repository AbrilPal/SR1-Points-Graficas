# Andrea Abril Palencia Gutierrez, 18198
# SR1: Points --- Graficas por computadora, seccion 20
# 07/07/2020 -- 13/07/2020

# libreria
import struct

# para especificar cuanto tamaño quiero guardar en bytes de cada uno
def char(c):
    # solo un byte
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    # solo 2 bytes
    return struct.pack('=h', w)

def dword(d):
    # solo 4 bytes
    return struct.pack('=l', d)
    
def color(r, g, b):
    return bytes([b, g, r])

# colores predeterminados
rosado = color(250,229,251)
negro = color(0,0,0)
blanco = color(255,255,255)

# clase principal
class Render(object):
    # inicializa cualquier objeto dentro de la clase Render
    def __init__(self, ancho, alto):
        # ancho de la imagen
        self.ancho = ancho
        # alto de la imagen
        self.alto = alto
        # color predeterminado del punto en la pantalla
        self.punto_color = negro
        # color de fondo de la imagen
        self.glClear()

    # fondo de toda la imagen
    def glClear(self):
        # el color predeterminado es rosado
        self.pixels = [[rosado for x in range(self.ancho)] for y in range(self.alto)]

    # crear un punto en cualquier lugar de la pantalla 
    def glVertex(self, x, y):
        self.pixels[x][y] = self.punto_color

    # permite cambiar el color del punto
    def glColor(self, color_p):
        self.punto_color = color_p

    # escribe el archivo
    def glFinish(self, name):
        archivo = open(name, 'wb')

        archivo.write(bytes('B'.encode('ascii')))
        archivo.write(bytes('M'.encode('ascii')))

        archivo.write(dword(14 + 40 + self.ancho * self.alto * 3))
        archivo.write(dword(0))
        archivo.write(dword(14 + 40))
        archivo.write(dword(40))
        archivo.write(dword(self.ancho))
        archivo.write(dword(self.alto))
        archivo.write(word(1))
        archivo.write(word(24))
        archivo.write(dword(0))
        archivo.write(dword(self.ancho * self.alto * 3))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))
        archivo.write(dword(0))

        for x in range(self.alto):
            for y in range(self.ancho):
                archivo.write(self.pixels[x][y])


        archivo.close()

