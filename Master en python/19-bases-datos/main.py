import mysql.connector

#Conexion 
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    #port = 3306
    database = "master_python"

)

#La conexion ha sido correcta ?
#print(database)
#Cursos que nos permite ver las consultas
cursor = database.cursor(buffered= True)

#Crear base de datos
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")


for bd in cursor:
    print(bd)
"""
##Crear tabla 
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar (40) not null,
    modelo varchar (40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
) 
""")

cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

#cursor.execute("INSERT INTO vehiculos VALUES(null, \"Opel\", \"Astra\", 18500)")
coches = [
    ('Seat', 'Ibiza', 5000),
    ('Renault', 'Clio', 15000),
    ('Citroen', 'Saxo', 2000),
    ('Mercedes', 'Clase C', 35000)

]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s,%s,%s)",coches)

database.commit()

#Listar
cursor.execute("SELECT * FROM vehiculos")

result = cursor.fetchall() 
print("-----TODOS MIS COCHES-----")
for coche in result:
    print(coche[1],coche[2], coche[3])

cursor.execute("SELECT * FROM vehiculos")
coche = cursor.fetchone()
print(coche)

#BORRAR
cursor.execute("DELETE FROM vehiculos WHERE marca = 'Mercedes'")
database.commit()


print(cursor.rowcount, "borrados!!")

#Actualizar 
cursor.execute("UPDATE vehiculos SET modelo = 'LEON' WHERE marca ='Seat'")
database.commit()

print(cursor.rowcount, "Actualizado!!")