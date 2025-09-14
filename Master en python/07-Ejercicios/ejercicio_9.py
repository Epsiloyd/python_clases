"""
Ejercicio 9: Hacer u nprograma que pida numerosa al usuario 
indefinidamente hasta meter el numero 111
"""
contador = 1
while contador < 100:
    numero = int(input("Instroduce un numero: "))

    if numero == 111: 
        print("Numero correcto!!!!")
        break
    else:
        print(f"Has introducido el numero: {numero}")