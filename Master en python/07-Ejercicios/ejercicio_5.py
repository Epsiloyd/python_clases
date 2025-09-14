"""
Ejercicio 5:
Hacer un programa que muestre todos los numeros entro 
dos numero que diga el usuario
"""

numero1 = int(input("\nEscribe el primer numero: "))
numero2 = int(input("\nEscribe el segundo numero: "))

if numero1 < numero2:
    for contador in range (numero1,numero2 + 1):
        print(contador)

else:
    print("\nEl número 1 debe ser menor al numero 2 ")