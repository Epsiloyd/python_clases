cantantes = ["2pac", "Drake", "Bad Bunny", "Jose Alfredo Jimenez"]
numeros = [1,2,8,9,3,4]

#ordenar
#print(numeros)
numeros.sort()
#print(numeros)

#Añadir elemento

cantantes.append("Natos y Waor")
cantantes.insert(1,"David Bisbal")

#print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove("Bad Bunny")

#print(cantantes)

#Dar la vuelta

#print(numeros)
numeros.reverse()
#print(numeros)


#Buscar dentro de una lista
print("Drake" in cantantes)

#Contar elementos
print(cantantes)
print(len(cantantes))

#Cuantas veces aparece un elemento
numeros.append(8)
print(numeros.count(8))

#Conseguir indice
print(cantantes.index("Drake"))

#Unir listas
cantantes.extend(numeros)
print(cantantes)