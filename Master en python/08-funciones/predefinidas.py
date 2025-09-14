nombre = "Felipe Torres"

#funciones generales
print(type(nombre))


# detectar el tipado 
comprobar = isinstance(nombre, str)
if comprobar:
    print("Esa variables es un string")

else: 
    print("No es una cadena")

if not isinstance(nombre, float):
    print("La variables no es un numero con decinales")

#Limpiar espacios
frase = "  Mi contenido  "
print(frase)
print(frase.strip())

#Eliminar variables

year = 2024

print(year)

del year

#print(year)

#Comprobar variables vacia
texto = "  ff  "

if len(texto) <= 0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenico: ",len(texto))

#ENCONTRAR CARACTERES
    frase = "La vida es bella"

    print(frase.find("vida"))

#Reemplazar palabras en un string
nueva_frase = frase.replace("vida","moto")
print(nueva_frase)

#Procesar mayusculas y minusculas
print(nombre)
print(nombre.lower())
print(nombre.upper())