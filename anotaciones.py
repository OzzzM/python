A or B or C or E or F or H or I or L or M or N or O or P or R or S or T or U or W or Z

for counter in range(1, 6):
    
  ganadores_carrera_temporada = input("Ingrese los ganadores de las carreras de la temporada: ")
    
  cantidad_escuderias = len(ganadores_carrera_temporada)
    
  while cantidad_escuderias != 1:
    
    if cantidad_escuderias == 0:
        print("Usted no ha ingresado ninguna escudería, por favor intente de nuevo.\n")
    elif cantidad_escuderias >= 2:
        print("Usted ha ingresado más de una escuderia, por favor intentelo de nuevo.\n")
        
    cantidad_escuderias = input("Ingrese solo una escuderia: ")
    
  escuderias = "ABCEFHILMNOPRSTUWZ"
  
  if ganadores_carrera_temporada.isalpha():
    
    caracter_es_escuderia = escuderias.count(ganadores_carrera_temporada)
    
    if caracter_es_escuderia == 1:
        print (f"La escuderia ingresada Fue: {posibles_ganadoras}\n")
    else:
        print(f"La escuderia ingresada {posibles_ganadoras} no existe.")
if ingreso_ganadores_tempo in escuderias_fav_alejandro:
      print("A")
elif ingreso_ganadores_tempo[0] in escuderias_fav_carolina:
  print("C")
elif ingreso_ganadores_tempo[0] not in escuderias_fav_alejandro and escuderias_fav_carolina:
  print("E")
  