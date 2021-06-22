fav_alejandro = input("Ingrese las escuderias favoritas de almejandro: \n")
fav_carolina = input("Ingrese las escuderias favoritas de Carolina: \n")
ganadores_carrera = input("Ingrese las escuderias Ganadoras de la temporada: ")

  
  
  #SE DEBE RECORDAR QUE ESTE METODO ESTA HECHO SIN UTILIZAR LA FUNCIÓN POR ESO APARECEN TANTAS LINEAS DE CÓDIGO REPETIDAS PERO ESTE FUE EL 
  #MÁS APROXIMADO QUE PUDE HACER POR MI MISMO HASTA ESTE PUNTO. LO DE LA FUNCIÓN FUE VISTO EN LOS TEXTOS CONSULTADOS.
  
puntos_almejandro = 0
puntos_carolina = 0
lista = ""

for j in ganadores_carrera:
  if j in fav_alejandro and j not in fav_carolina:
    puntos_almejandro += 1
    if puntos_almejandro>puntos_carolina:
          print("A")
    elif puntos_almejandro== puntos_carolina: 
      print("E") 
    else: 
      print("C")
  elif j in fav_carolina and j not in fav_alejandro:
    puntos_carolina += 1
    if puntos_almejandro>puntos_carolina:
          print("A")
    elif puntos_almejandro== puntos_carolina: 
      print("E") 
    else: 
      print("C")
  elif j in fav_alejandro and j in fav_carolina:
    puntos_carolina += 1
    puntos_almejandro += 1
    if puntos_almejandro>puntos_carolina:
          print("A")
    elif puntos_almejandro== puntos_carolina: 
      print("E") 
    else: 
      print("C")
  elif j not in fav_alejandro and j not in fav_alejandro:
    if puntos_almejandro>puntos_carolina:
          print("A")
    elif puntos_almejandro== puntos_carolina: 
      print("E") 
    else: 
      print("C")




