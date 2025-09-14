"""
Una variables es un contenedor de informacion, que dentro guarda un dato,
se pueden crear muchas variables y que cada una tenga un dato distinto
"""

#crear variables y asignarles un valor#
texto = "Master en python"
#texto = 2
texto2 = "Con Felipe Torres" 
numero = 27
decimal = 9.9
#mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------")
#reasignado el valor 
numero = 72 
decimal = 10.0
print(numero)
print(decimal)

print("----------------------")

#concatenacion
"""
es el poder unir dos variables o strings
"""

nombre = "Felipe de Jesus"
apellidos = "Torres Tavera"
web = "Epsiloyd.com"

print(nombre +" "+ apellidos + " - "+ web)
print(f"hola mi nombre es:{nombre} {apellidos} y mi sitio web es- {web}")#esta es la mejor opcion
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))
"""
Esta forma no es la correcto
print(nombre,apellidos,web)
"""