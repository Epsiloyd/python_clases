"""
Ejercicio 3:

programa que prueba si una variable esta vacia y si esta vacia, 
rellenarla con texto en minusculas y mostrarlo en mayusculas
"""

texto = " "

if len(texto.strip()) <= 0:
    #Mostrar el texto 
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else: 
    print(f"Lariable tiene contenido {texto} ")