"""
Listas (arrays)

Son colecciones o conjuntos de datos / valores, bajo un unico nombre.
Para acceder a esos valores podemos usar un indice numerico.
"""

pelicula = "Batman"

#Definir lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
cantantes = list(("2pac", "Drake", "Rammstein"))
year = list(range(2020,2030 + 1))
variada = ["Felipe", 27,20.3,True,"Texto"]

print(peliculas)
print(cantantes)
print(year)
print(variada)


#Indices
peliculas[1] = "Wall-e"
peliculas[2] = "Kun-fu panda"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[0:3])
print(peliculas[0:])
print(peliculas)

#Añadir elementos a listas 

cantantes.append("Kendrik Lamar")
cantantes.append("Eminem")

print(cantantes)

#Recorrer una lista

nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")

    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

   
    
print("\n####Listado de peliculas####")

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+ 1}. {pelicula}")


#Listas multidimencionales
    
print("\n#### Listas de contactos ####")
contactos = [
    [
        "Felipe",
        "Felipe.com"
    ],
    [
        "Mafer",
        "Mafer.com"
    ],
    [
        "Leticia",
        "Leticia.com"
    ]

]

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre:" + elemento)
        else:
            print("Pagina:" + elemento)
    print("\n")

#print(Contactos[1][1])

