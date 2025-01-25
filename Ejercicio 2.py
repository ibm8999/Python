#Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”.
#Esos tres datos deberán ser almacenados en una lista y mostrar en consola el mensaje: 
#“Los datos personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por teclado).
nombre=input("Dame nombre")
apellido=input("Dame apellido")
telefono=input("Dame teléfono")

listin=[nombre,apellido,telefono]

print("Los datos personales son: " + listin[0] + " apellido " + listin[1] + " y teléfono  " + listin[2])

