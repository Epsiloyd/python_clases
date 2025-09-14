"""
Ejercicio 1 Hacer un programa que tenga una lista

-Recorrer la lista y mostrarla 
-Hacer una funcion que recorra listas de numeros y devuelva string al mostrarla 
-Ordenarla y mostrarla
-Mostrar su longitud 
-Buscar algun elemento (Que el usuario pida por teclado)
"""

#Crear lista

numeros = [13,56,28,19,34,95,108]

#Crear funcion que recorra lista y devuelva string
def mostrarlista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado


#Recorrer y mostrar
print("#### Recorrer lista y mostrar ####")
"""
for numero in numeros:
    print(numero)
"""
print(mostrarlista(numeros))
print(mostrarlista(["Maffer","Felipe","4ever"]))

print("### Ordenar y mostrar ###")
numeros.sort()
print(mostrarlista(numeros))

print("### Mostrar la longitud ###")

print(len(numeros))
"""
print("### Busqueda en la lista ###")
try:
    busqueda = int(input("Introduce el numero: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))
    else:
        print(f"Has instroducido el {busqueda}")
    print(f"### Buscar en la lista el numero {busqueda} ### ")


    search = numeros.index(busqueda)
    print(f"El numero nuscado existe en la lista, es el indice: {search}")
except:
    print("El numero no esta en la lista, lo siento!!")
"""

#Multiples excepciones

