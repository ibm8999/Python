print("Programa de evaluacion de notas")
nota_alumno=int(input("Dame la nota "))

def evaluacion(nota):
	
	if nota < 3: 
		valoracion="muy deficiente"
	elif nota < 5:
		valoracion="suspenso"
	elif nota <6:
	   valoracion="aprobado"
	else:
		valoracion="sobresaliente"

	return valoracion

print(evaluacion(nota_alumno))





