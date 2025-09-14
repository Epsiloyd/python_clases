"""Condicionales si un dato cumple una serie de instrucciones se ejecutaran una serie de 
instrucciones y si no se cumplen se ejecutaran otra serie de instrucciones
"""

"""
#condiconal if
Si_se_cumple_esta_condicion:    
    Se ejecutaran un grupo de instrucciones
Si_no:
    Se ejecutaran otras instrucciones

if condicion:
    instrucciones:
else:
    otras instrucciones:

#Operadores de comparacion:

== igual que
!= diferente de 
<menor que
>mayor que
<=menor o igual que
>=mayor o igual que

#Operadores logicos
and = y
or = o
! = negacions
not = no 
"""

#Ejemplo 1
print("#####ejemplo 1 ####")

color = "morado"

#color = input("Escoje un color: ")

if color == "morado":
    print("Felicidades acertaste el color")
else:
    print("No es el color correcto...")

print("\n#####ejemplo 2 #####")

year = 2027
#year = int (input("Escribe el año en el que estamos: "))
if year <= 2027:
    print("Estamos antes antes de 2027")
else:
    print("Es un año posterior a 2027")

print("\n#####ejemplo 3 #####")

nombre = "Felipe Torres"
ciudad = "Guadalajara"
continente = "Europeo"
edad = 27
mayoria_de_edad = 18

if edad >= mayoria_de_edad:
    print(f"{nombre} es mayor de edad")
    
    if continente != "Americano":
        print("El usuario no es americano")
    else:
        print(f"El usuairio es {continente} y de {ciudad}")
else:
    print(f"{nombre} No es mayor de edad")

print("\n#####ejemplo 4 #####")

#dia =int(input("Introdice el numero dl dia de la semana: "))
dia = 2
"""
if dia == 1:
    print("Es lunes")
else:
    if dia == 2:
        print("Es martes")
    else:
        if dia == 3:
            print("Es miercoles")
        else:
            if dia == 4:
                print("Es jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    if dia == 6:
                        print("Es sabado")
                    else:
                        if dia == 7:
                            print("Es domingo")
                        else:
                            print("No es un numero permitido")
"""
if dia == 1:
    print("Es lunes")                          
elif dia == 2:
    print("Es martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")
else:
    print("No es un numero permitido")

print("\n##### ejemplo 5 #####")

edad_minima = 18
edad_maxima = 65
edad_oficial = 18
#edad_oficial = int(input("Tienes edad de trabajr?: ")) 

if edad_oficial >= 18 and edad_oficial <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

print("\n##### ejemplo 6 #####")

pais = "Rusia"

if pais == "Mexico" or pais == "España" or pais == "Colombia":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana")

print("\n##### ejemplo 7 #####")

pais = "España"

if not (pais == "Mexico" or pais == "España" or pais == "Colombia"):
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana")

print("\n##### ejemplo 8 #####")

pais = "USA"

if pais != "Mexico" and pais != "España" and pais != "Colombia":
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana")