"""
Variables locales: se definen dentro de la funcion y no 
se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return

Variables Globales: Don las que se declaran fuera de una funcion 
y estan disponibles dentro y fuera de ellas.
"""

#Variables Globales

frase = "Mientras tu me recuerdes, no me importa que el resto del mundo me olvide"

print(frase)


def holamundo():
    frase = "Hola Mundo"
    print("Dentro de la funcion:")
    print(frase)
    year = int(2024)
    print(year)

    global website
    website = "Epsiloyd.net" 
    print("Dentro", website)

    return "Dato devuelto " + str (year)

print(holamundo())
print("Fuera: ", website)

