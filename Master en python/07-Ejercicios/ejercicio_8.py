"""
Ejercicio 8:Cuanto es el x % de x numero
como el 20% de 150 
"""

numero = int(input("Introduce un numero: "))
porcentaje = int(input(f"Escribe el % que quieres sacar de {numero}: "))


operacion = (numero * (porcentaje / 100))

print(f"El {porcentaje}% de el {numero} es: {operacion}")