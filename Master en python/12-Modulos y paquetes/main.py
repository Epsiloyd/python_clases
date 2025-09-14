"""
Modulos: son funcionalidades ya hechas para reutilizar.

En python hay muchos modulos, que los puedes consultar aqui:
https://docs.python.org/3/py-modindex.html

Podemos conseguir modulos que ya vienen en el lenguaje, modulos de internet y tambien podemos 
crear nuestros modulos
"""

#importar modulo propio
#import mimodulo
#from mimodulo import holaMundo
from mimodulo import *

#print(mimodulo.holaMundo("Felipe Torres"))
#print(mimodulo.calculadora(3,5,True))

print(holaMundo("Felipe Torres"))
print(calculadora(3,5,True))


#Modulo de Fechas

import datetime 

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)

print(fecha_completa.year)

print(fecha_completa.month)

print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y,%H/%M/%S")

print("Mi fecha peronalizada", fecha_personalizada)

print(datetime.datetime.now().timestamp())

#Modulo matematicas

import math

print("Raiz cuadrada de 10", math.sqrt(10))

print("Numero Pi", float(math.pi))

print("Redondear", math.ceil(6.1851))
print("Redondear", math.floor(6.1851))


#Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))


