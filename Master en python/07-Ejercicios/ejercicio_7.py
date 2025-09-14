"""
Ejercicio 7:Hacer un programa que muestre todos los numeros impares 
entre dos numeros que decida el uduario.
"""


numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))

if numero1 < numero2:

    for x in range (numero1,(numero2+1)):

        if x %2 ==0:
            print(f"\n{x} es par ")
        else:
            print(f"\n{x} es impar ")
  
else:
    print("\nEl numero 1 debe ser menor al numero 2")

    