
milista=["Marematicas","Fisica","Quimica","Historia","Lengua"]

print(milista)
notas=[]
dupla=()

for asignatura in milista:
	nota = input("Que nota has sacado en " + asignatura + "?")
	notas.append(nota)

for i in range(len(asignaturas)):

	print("En " + milista[i] + " has sacado " + notas[i])
 