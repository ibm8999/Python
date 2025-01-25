class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        if (self.enmarcha):
            return("El coche esta en marcha")
        else:

            return("El coche esta parado")
    
  

    def estado(self):
        print("El coche tiene ", self.ruedas, " ruedas. Un ancho de ", self.anchoChasis, " y un largo de ",
            self.largoChasis)
            
        
miCoche=Coche()

print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

print(miCoche.arrancar(True))
miCoche.estado()
    
print(" -------A continuacion creamos el objeto ----------------")

miCoche2=Coche()
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche2.estado()
print(miCoche2.arrancar(False))


