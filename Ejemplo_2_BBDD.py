import sqlite3

miConexion=sqlite3.connect("PrimeraBase.dbf")

miCursor=miConexion.cursor()

miCursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
     ("Camiseta", 10, "Deportes"),
     ("Jarrón", 90, "Cerémica"),
     ("Camión", 10, "Juguete"),
     ("Destornillador", 10, "Ferretería")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos=miCursor.fetchall()

for producto in variosProductos:
	print("Nombre artículo: ", producto[0], " precio=", producto[1])

miConexion.commit()



miConexion.close()