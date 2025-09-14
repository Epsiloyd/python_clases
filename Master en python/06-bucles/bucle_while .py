"""
#Bucle While
Es una estructura de control que itera o repite una ejecucion de una serie de instrucciones 
tantas veces como sea necesario,
hasta que deje de cumplir las condiciones


while condicion:
    bloque de instrucciones
    actualizacion de contador

"""

contador = 1

while contador <= 100:
    print(f"Estoy en el nimero: {contador}")
    contador += 1

print("#################################################")

contador = 1
muestra = str(0)

while contador <= 100:
    muestra = muestra  + " , " + str(contador) 
    contador += 1

print(muestra)



#Ejemplo
print("\n######## Ejemplo ##########")

numero_usuario =int(input("\nDe que numero quieres la tabla: "))

if numero_usuario <1:
    numero_usuario =1

print(f"\n### Tabla del: {numero_usuario} ###")

contador = 1
while contador <= 10:
    print(f"\n {numero_usuario} x {contador} = {numero_usuario * contador}")
    contador += 1
else:
    print("\nTabla terminada")