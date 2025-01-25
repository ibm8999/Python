mitupla=("Juan",13,1,1995)
milista=list(mitupla)
otratupla=tuple(milista)
tuplaunit=("Juan",)
print(milista)
print("Juan" in mitupla)
print(mitupla.count(13))
print(len(otratupla))
print(len(tuplaunit))
# empaquetado de datos
nombre, dia, mes, agno=mitupla
print(nombre, agno, dia)

