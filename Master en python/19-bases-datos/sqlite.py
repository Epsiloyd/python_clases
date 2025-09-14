#Importar modulo

import sqlite3

#Conexion
conexion = sqlite3.connect("./19-bases-datos/Pruebas.db")

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    Precio int(255)          
)""")

#Guardar cambios
conexion.commit()

#Insertar datos

cursor.execute("""INSERT INTO productos VALUES (null,"Segundo Producto"," Descripcion de mi procuto",550 )""")
conexion.commit()



#Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()
#Insertar mucos registros de golpe

productos = [
    ("Ordenador portatil", "Buen PC",700),
    ("Telefono Movil", "Buen Telefono",140),
    ("Placa base", "Buena Placa",80),
    ("Tableta 15", "Buena Tableta",300),
                     
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()

#update
cursor.execute("UPDATE productos SET precio = 678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >= 300;")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo:",producto[1])
    print("Descripcion:",producto[2])
    print("Precio:",producto[3])
    print("\n")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)
#Cerrar conexion
conexion.close()