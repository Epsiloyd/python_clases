from io import open
import pathlib
import shutil
#Abrir archivo
ruta = str (pathlib.Path().absolute()) +"/fichero_texto.txt"
print(ruta)
archivo = open(ruta , "a+")

#Escribir

archivo.write("#### Soy un texto metido desde paython ###\n")

#Cerrar archivo

archivo.close()

#Abrir archivo
ruta = str (pathlib.Path().absolute()) +"/fichero_texto.txt"
#print(ruta)
archivo_lectura = open(ruta , "r")

#Leer contenido 
#contenido = archivo_lectura.read()
#print(contenido)

"""
for elemento in contenido:
    print(elemento)
"""    


#Leer contenido y guardarlo en lista 
lista = archivo_lectura.readline()

archivo_lectura.close()

for frase in lista:
     #lista_frase = frase.split()
     #print(lista)
        print("_ " +str(frase.center(100)))

"""
#copiar
ruta_original = str (pathlib.Path().absolute()) +"/fichero_texto.txt"
ruta_nueva = str (pathlib.Path().absolute()) +"/fichero_texto.txt"
ruta_alternativa = "./07-Ejercicios/fichero_copiado77.txt"
shutil.copyfile(ruta_original,ruta_alternativa)
"""
#Mover

ruta_original = str (pathlib.Path().absolute()) +"/fichero_copiado.txt"
ruta_nueva = str (pathlib.Path().absolute()) +"/fichero_copiado_NUEVO.txt"

shutil.move(ruta_original,ruta_nueva)