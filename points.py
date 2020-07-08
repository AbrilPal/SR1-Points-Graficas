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
    
