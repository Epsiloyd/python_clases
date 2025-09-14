#Capturar excepciones y manejar errores en codigo 
#susceptible a fallos / errores

"""
try:

    nombre = input("Cual es tu nombre?:  ")

    if len(nombre) >1:
        nombre_usuario ="El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce un nombre")

else:
    print("Todo a funcionado correctamente")

finally:
    print("Fin de la iteracion !!")


print("### Busqueda en la lista ###")
try:
    busqueda = int(input("Introduce el numero: "))

    comprobar = isinstance(busqueda, int)
    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))
    else:
        print(f"Has instroducido el {busqueda}")
    print(f"### Buscar en la lista el numero {busqueda} ### ")


    search = numeros.index(busqueda)
    print(f"El numero nuscado existe en la lista, es el indice: {search}")
except:
    print("El numero no esta en la lista, lo siento!!")
"""

#Multiples excepciones 
"""
try:
    numero = int(input("Dime un numero para elevarlo al cuadrado: "))

    print("El cuadrado es: " + str (numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros!!")
#except ValueError:
    #print("Introduce un numero!!")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error: ", type(e) .__name__)
"""

#Excepciones personalizadas o lamzar excepcion 
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introcude la edad: "))

    if edad < 5 or edad >110:
        raise ValueError("La edad introducida no es real")

    elif len(nombre)<=1:
        raise ValueError("El nombre bi esta completo")
    else:
        print(f"Bienbenido al master en phyton {nombre}!!")
except ValueError:
    print("Introduce los fatos correctamente!!")
except Exception as e:
    print("Eciste un error", e)
