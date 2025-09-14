"""
Diccionario:
Un tipo de dato que alamacena un conjunto de datos.
En formato > valor
Es parecido a un array asociativo o un conjunto json.

"""

persona = {
    "nombre": "Felipe",
    "Apellido": "Torres",
    "Web": "Epsiloyd.com"
}

print(type(persona))
print(persona["Web"])
print(persona)


#Lista con diccionarios

contactos = [ 
    {
        "nombre": "Antonio",
        "Web": "Antonio.com" 
    },
    {
        "nombre": "Carmen",
        "Web": "Carmen.com" 
    },
    {
        "nombre": "Maffer",
        "Web": "Maffer.com" 
    },
    
    
]

contactos[2]["nombre"] = "Amor de amores"
print(type(contactos))
print(contactos[2]["nombre"])

print("\n Lista de contactos: ")
print("____________________________________")

for contacto in contactos:
    print(f"Nombre del contacto: {contacto ["nombre"]}")
    print(f"Web del contacto: {contacto ["Web"]}")
    print("____________________________________")