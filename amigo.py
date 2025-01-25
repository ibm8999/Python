#  calcula numero amigos
import sys

def amigos(num): 
    suma = 0 
    lista_divisor=[]

    for i in range(1,num): 
        if num % i == 0: 
            suma = suma + i 
            lista_divisor.append(suma)
#            print(i," es divisor de ", num)
#    print("Divisores de ", num+1," son ",lista_divisor," que suman=", suma)            
    return suma
     
n = int(input("limite inferior: "))
m = int(input("limite superior: "))
divisores=[]

for j in range(n,m):
#    print("En for ", j)
    a1 = amigos(j)
#    print(f"voy por {j} y su suma de divisores es {a1}")
#    print(f"los div de {a1} es {amigos(a1)}")
#    print("En if ", a1)
    if j==amigos(a1) and j != a1: 
       print(f'los numeros {j}  y {a1} son amigos y sus divisores son: ')
        ## print(f'los numeros {j}  y {a1} son amigos y sus divisores son: ', amigos(divisores))


#   este print imprime sin avanzar línea
  #  print("Voy por ",j, " hasta -> ", m, end="\r")  
print("")
# ff

