from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

numeroPantalla=StringVar()

operacion=""

anterior=""

resultado=0.0
acumulador=0.0


#-------------------pulsaciones del teclado----------------------

def accionCE():

	global operacion, anterior

	operacion=""
	numeroPantalla.set("0")

#-------------------pulsaciones del teclado----------------------

def numeroPulsado(num):

	global operacion, anterior

	if operacion!="":
		anterior=operacion
		operacion=""
		numeroPantalla.set(num)
	else:
		if numeroPantalla.get()=="0" and num=="0":

			numeroPantalla.set(numeroPantalla.get())
		else:
			numeroPantalla.set(numeroPantalla.get() + num)


	#--------------- funcion suma ----------------------------------

def operar(ope, num):

	global operacion, resultado, acumulador

	print("entro operar   acumulador  resultado  ope   numero parntalla")
	print("                 ", acumulador, "    ", resultado, "       ", ope, "         ", float(num))
	
	#acumulador = float(numeroPantalla.get())
	if acumulador==0.0:
		acumulador=float(num)
		operacion= ope
	else:
 
		if ope=="+":
			operacion= ope
			resultado= acumulador + float(num)
	
		if ope=="-":
			operacion = ope
			resultado = acumulador - float(num)
	
		if ope=="x":
			operacion = ope
			resultado = acumulador * float(num)

		if ope=="/":
			operacion = ope
			resultado = acumulador / float(num)

		numeroPantalla.set(resultado)
		acumulador=resultado

	print("salgo operar   acumulador  resultado  ope   numero parntalla")
	print("                 ", acumulador, "    ", resultado, "       ", ope, "         ", float(num))


#----- hacemos la última operación y llevamos el resultado a numeroPantalla

def el_resultado():

	global resultado, anterior, acumulador
	
	print("en igual", anterior, "resultado", resultado, "num pantalla=", float(numeroPantalla.get()))
	
	operar(anterior, numeroPantalla.get())
	
	acumulador=0
	resultado=0

#------- validar comas, revisar el texto para que solo haya una coma

def validaComa(dig):

	hayComa=False
	texto=numeroPantalla.get()

	for j in range(len(texto)):

 		if texto[j]== ".":

 			hayComa=True

	if hayComa==False:
 		numeroPantalla.set(numeroPantalla.get() + dig) 	   

#------- eliminar ceros a la izquierda

def validaCero(dig):

 	hayCero=False
 	texto=numeroPantalla.get()

 	for j in range(len(texto)-1):

 		if texto[j]=="0" and texto[j+1]!=",":

 			hayCero=True

 	if hayCero==False:

 		numeroPantalla.set(numeroPantalla.get() + dig)

#-------   fila 0 pantalla o display -------------------------------

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=0, column=1, padx=10,pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943",justify="right")

#-------   fila 1 botones de borrado -------------------------------

botonCE=Button(miFrame, text="CE", width=3,command=lambda:accionCE())
botonCE.grid(row=1, column=1)
botonC=Button(miFrame, text="C", width=3,command=lambda:accionCE())
botonC.grid(row=1, column=2)
botonDel=Button(miFrame, text="D",width=3,command=lambda:numeroPulsado("D"))
botonDel.grid(row=1, column=3)
botonDivi=Button(miFrame, text="/", width=3,command=lambda:operar("/", numeroPantalla.get()))
botonDivi.grid(row=1, column=4)

#-------------fila 2 --------------------------------

boton7=Button(miFrame, text=7, width=3,command=lambda:numeroPulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text=8, width=3,command=lambda:numeroPulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text=9,width=3,command=lambda:numeroPulsado("9"))
boton9.grid(row=2, column=3)
botonMult=Button(miFrame, text="x", width=3, command=lambda:operar("x", numeroPantalla.get()))
botonMult.grid(row=2, column=4)

#-------------fila 3 --------------------------------

boton4=Button(miFrame, text=4, width=3,command=lambda:numeroPulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text=5, width=3,command=lambda:numeroPulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text=6, width=3,command=lambda:numeroPulsado("6"))
boton6.grid(row=3, column=3)
botonRest=Button(miFrame, text="-", width=3, command=lambda:operar("-", numeroPantalla.get()))
botonRest.grid(row=3, column=4)

#-------------fila 4 --------------------------------

boton1=Button(miFrame, text=1, width=3,command=lambda:numeroPulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text=2, width=3,command=lambda:numeroPulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text=3, width=3,command=lambda:numeroPulsado("3"))
boton3.grid(row=4, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:operar("+", numeroPantalla.get()))
botonSuma.grid(row=4, column=4)

#-------------fila 5 --------------------------------

boton0=Button(miFrame, text=0, width=3,command=lambda:numeroPulsado("0"))
boton0.grid(row=5, column=2)
botonComa=Button(miFrame, text=",", width=3,command=lambda:validaComa("."))
botonComa.grid(row=5, column=3)
botonIgual=Button(miFrame, text="=",width=3,command=lambda:el_resultado())
botonIgual.grid(row=5, column=4)

#for i in range(4):
numeros="7894561230"

#for j in range(len(numeros)):
#	print(f"estamos en ", numeros[j])

#i=1 

#while i< 10:
#	print(f"while en ", numeros[i])
#	i = i + 1



root.mainloop()