#Crea un programa que pida dos números por teclado.
#El programa tendrá una función llamada “DevuelveMax” encargada de devolver el número más alto de los dos introducidos.

num1=int(input("Dame un número: "))
num2=int(input("Dame otro:      "))

def DevuelveMax(a, b):
	if a>b:
		print(a)
	elif a<b:
		print(b)
	else:
		print(" son iguales")

print("El numero mayor es " )
DevuelveMax(num1, num2)
