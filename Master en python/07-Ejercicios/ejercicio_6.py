"""
Ejercicio 6: MOstrar todas las tablas de multiplicar del 1 al 10.
Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10 
"""

for cabecera in range(1,11):
    print("\n###############")
    print(f"\n#### Tabla del { cabecera } ####") 
    print("\n###############")

    for numero in range (1,11):
        print(f"\n {numero} x {cabecera}: {numero*cabecera}")
else:
    print("\nFin del ejercicio...")