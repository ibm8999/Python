from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

etiNombre=Label(miFrame, text="Nombre")
etiNombre.grid(row=0, column=0, padx=10,pady=10)
cuaNombre=Entry(miFrame)
cuaNombre.grid(row=0, column=1, padx=10,pady=10)

etiApellido=Label(miFrame, text="Apellido")
etiApellido.grid(row=1, column=0, padx=10,pady=10)
cuaApellido=Entry(miFrame)
cuaApellido.grid(row=1, column=1, padx=10,pady=10)

etiDireccion=Label(miFrame, text="Dirección")
etiDireccion.grid(row=2, column=0, padx=10,pady=10)
cuaDireccion=Entry(miFrame)
cuaDireccion.grid(row=2, column=1, padx=10,pady=10)

#pintamos los botones de los numeros

for i in range(3):
	Button(miFrame, text=i).grid(row=1, column=i)
	





root.mainloop()