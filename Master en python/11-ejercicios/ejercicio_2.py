"""
Ejercicio 2 :
Escribir un programa que añada valores a una lista 
mmiestras que su longitud sea mejor a 120 y luego mostrar la lista 
Plus: Usa while y for

"""
coleccion = []
x = 0
while x < 120:
    coleccion.append(f"Elemento - {x}")
    print("MOstrando el elemento: " + coleccion[x])
    x += 1

print(coleccion)


"""
coleccion = []

for contador in range (0, 116):
    coleccion.append(f"elemento - {contador}")
    print("Mostrar el:  " + coleccion[contador])

print(coleccion)

"""