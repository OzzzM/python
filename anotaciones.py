fav_alejandro = input("Ingrese las escuderias favoritas de almejandro: \n")
fav_carolina = input("Ingrese las escuderias favoritas de Carolina: \n")
ganadores_carrera = input("Ingrese las escuderias Ganadoras de la temporada: ")

puntos_almejandro = 0
puntos_carolina = 0

for j in ganadores_carrera:
  if j in fav_alejandro and j not in fav_carolina:
    puntos_almejandro += 1
    print("A")
  elif j in fav_carolina and j not in fav_alejandro:
    puntos_carolina += 1
    print("C")
  elif j in fav_alejandro and j in fav_carolina:
    puntos_carolina += 1
    puntos_almejandro += 1
    print("E")

if puntos_almejandro>puntos_carolina:
    print("A")
elif puntos_almejandro== puntos_carolina: 
    print("E") 
else: 
    print("C")


