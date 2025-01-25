import os
import json

pokemones=[]

def menu():
	if os.name == "posix":
		os.system("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
		os.system("cls")

	print("Bienvenido al pokedex")
	print("a - Agragar pokemon")
	print("m - Modificar pokemon")
	print("v - Ver pokemones")
	print("x - Salir")

continuar = True

while(continuar):
	menu()
	opt = input("Digite su opcion: ")

	if opt == 'a':
		print("Vamos a agregar un POKEMON")
		pmk = []
		pmk.append(input("Digite el nombre del pokemon"))
		pmk.append(input("Digite el tipo del pokemon"))
		pmk.append(input("Digite el color de pokemon"))
		pokemones.append(pmk)
		datos = json.dumps(pokemones)
		f = open('cosa.txt','w')
		f.write(datos)
		input("POKEMON agregado, presione enter para continuar")

	elif opt == 'v':
		print("Aqui estan los pokemones que hemos atrapado")
		for pkm in pokemones:
			print(pkm[0], "\t", pkm[1], "\t", pkm[2])

	elif opt == 'x':
		continuar=False
	else:
		print("Opcion no valida, amigo digite una de las letras ")
		input("Presione enter para continuar")



