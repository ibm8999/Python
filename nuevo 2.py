
midiccionario={"Alemania":"Berín","Francia":"París","Reino Unido":"Londres","España":"Madrid"}
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)
midiccionario["Italia"]="Lisboa"
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)

tuplapais=["España", "Francia", "Reino Unido", "Alemania"]
newdiccionario={tuplapais[0]:"Madrid", tuplapais[1]:"París", tuplapais[2]:"Londres", tuplapais[3]:"Berlín"}
print(newdiccionario)

basket={23:"Jordan", "Nombre":"Michel", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1998]}
print(basket["anillos"])
print(basket.keys())
print(basket.values())