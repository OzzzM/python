def winner(puntos_a,puntos_c):
    if puntos_a>puntos_c: 
        return "A" 
    elif puntos_a==puntos_c: 
        return "E" 
    else: 
        return "C" 

participantes = {"Alejandro":{"fav":input("Ingrese las escuderias favoritas de alejandro: \n"), "puntos":0}, 
"Carolina":{"fav":input("Ingrese las escuderias favoritas de Carolina: \n"),"puntos":0}}

ganadores_carrera = input("Ingrese los ganadores de la Temporada: ")

alejandro = participantes["Alejandro"] 
carolina = participantes["Carolina"]

for g in ganadores_carrera:
    if g in alejandro["fav"] and g not in carolina["fav"]:
        alejandro["puntos"]+=1
        print(winner(alejandro["puntos"],carolina["puntos"]), end="") 
    elif g in carolina["fav"] and g not in alejandro["fav"]:
        carolina["puntos"]+=1 
        print(winner(alejandro["puntos"],carolina["puntos"]), end="")
    elif g in alejandro["fav"] and g in carolina["fav"]:
        carolina["puntos"]+=1 
        alejandro["puntos"]+=1
        print(winner(alejandro["puntos"],carolina["puntos"]), end="")
    elif g not in alejandro["fav"] and g not in carolina["fav"]:
        print(winner(alejandro["puntos"],carolina["puntos"]), end="")
