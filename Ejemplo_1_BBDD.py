import sqlite3

miConexion=sqlite3.connect("PrimeraBase")

miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")

#variosProductos=[
#     ("Camiseta", 10, "Deportes"),
#     ("Jarrón", 90, "Cerémica"),
#     ("Camión", 10, "Juguete")


#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
	print("Nombre artículo: ", producto[0], " precio=", producto[1])

miConexion.commit()



miConexion.close()