"""
Ejercicio 3: Escribir un programa que muestre los cuadrados
(numero multiplicado por si mismo)  de los 60 primeros numeros
naturales. Resolver con for y con while
"""
print("\n### Bucle while ###")
contador = 0
while contador <= 60:
    
    cuadrado = contador * contador
    print(f"\n El cuadrado de { contador} es {cuadrado} ")

    contador += 1

print("\n### Bucle for ###")

for contador_1 in range(1,61):
    cuadrado_1 = contador_1 * contador_1
    print(f"\nEl cuadrado de {contador_1} es {cuadrado_1} ")
