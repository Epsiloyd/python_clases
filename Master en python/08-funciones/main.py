"""
Funciones:
Una funcion es un conjunto de instrucciones 
agrupadas bajo un mismo nombre o nombre completo 
que pueden reutilizar convocando 
a la funcion tantas veces como sea necesario


def nombredemifuncion (Paramatros):
    #Bloque  conjunto de instrucciones instrucciones

nombredemifuncion(mi_parametro)
"""

#Ejemplo 1

print("\n#### Ejemplo 1 ####")

#Definir la funcion
def muestra_nombres():
    print("Felipe")
    print("Maffer")
    print("Leticia")
    print("Meliton")
    print("Luis")
    print("Hector")
    print("\n")

#Invicar a la funcion

muestra_nombres()

#Ejemplo 2:parametros

print("\n#### Ejemplo 2 ####")

#nombre = "Felipe Torres"
"""
def mostrartunombre(nombre,edad):
    print(f"\nTu nombre es: {nombre}")

    if edad >= 18:
        print("Eres nayor de edad..")
    else:
        print("No eres mayor de edad")
        
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrartunombre(nombre,edad)

"""
#Ejemplo 3:Tabla de multiplicar

print("\n#### Ejemplo 3 ####")

def tabla(numero):
    print(f"Tabla de multiplicar del numero: {numero}")

    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} x {contador} = {operacion}")
        
    print("\n")

tabla(3)

#Ejemplo 3.1
print("_______________________________")

for numero_tabla in range (1,11):
    tabla(numero_tabla)


    #Ejemplo 5:Paramaetros opcionales 

print("\n#### Ejemplo 5 ####")

def get_empleado (nombre,id = None):
    print("\nEMPLEADO")
    print(f"\nNombre del Empleado: {nombre}")

    if id != None:
        print(f"\nID del empleado: {id}")

get_empleado("Felipe Torres", 8998488)



    #Ejemplo 6:return o devolver datos

print("\n#### Ejemplo 6 ####")

def calculadora(numero1, numero2, basicas = False):
    
    suma = numero1+numero2
    resta = numero1-numero2
    multi = numero1*numero2
    divicion = numero1/numero2


    cadena = " "
    if basicas != False:

        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(multi)
        cadena += "\n"
        cadena += "Divicion: " + str(divicion)
        cadena += "\n"

    return cadena
#Ya solo se denomina si es true o false y cambia lo que retorna a pantalla #
print(calculadora(5,5,True))


 #Ejemplo 7:Funciones dentro de otras funciones

print("\n#### Ejemplo 7 ####")

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

    cadena += "\n"

def getapellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def devuelvetodo (nombre,apellidos):
    texto = getNombre(nombre) + "\n" + getapellidos(apellidos)
    return texto 
print(devuelvetodo("Felipe", "Torres"))

 #Ejemplo 8:Funciones lambda

print("\n#### Ejemplo 8 ####")

dime_el_year = lambda year: f"El año es: {year * 5}"

print(dime_el_year(2024))

