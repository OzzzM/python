En caso lo quieras hacer con contadores, tendríamos que declara un contador para cada participante, para este caso hare el código sin usar un diccionario

#delcaramos las variables
fav_alejandro = "RAIFZ"
fav_carolina = "UZEOF"
ganadores_carrera = "IHZOWFEI"

#con inputs
# fav_alejandro = input("Ingrese las favoritas de alejandro: ")
# fav_carolina = input("Ingrese las favoritas de carolina: ")
# ganadores_carrera = input("Ingrese los ganadores")

def winner(puntos_a,puntos_c):
    if puntos_a>puntos_c: 
        return "A" 
    elif puntos_a==puntos_c: 
        return "E" 
    else: 
        return "C" 

La función para determinar al ganador se quedará igual. Ahora en vez de sumar 1 al valor del diccionario lo haremos al contador del participante, lo mismo para obtener el valor.

#iniciamos los puntos con 0
points_alejandro = 0
points_carolina = 0

for g in ganadores_carrera:
    #si la letra solo esta en alejandro
    if g in fav_alejandro and g not in fav_carolina:
        points_alejandro+=1
        #verifiacmos al ganador
        print(winner(points_alejandro,points_carolina),end="") #end="" para que se muestre horizontal
    #si la letra solo esta en carolina
    elif g in fav_carolina and g not in fav_alejandro:
        points_carolina+=1
        print(winner(points_alejandro,points_carolina),end="")
    #si esta en ambos
    elif g in fav_alejandro and g in fav_carolina:
        #sumamos el punto a ambos
        points_carolina+=1
        points_alejandro+=1
        #verifiacmos al ganador
        print(winner(points_alejandro,points_carolina),end="")
    #si no esta en ninguno
    elif g not in fav_alejandro and g not in fav_carolina:
        #verifiacmos al ganador
        print(winner(points_alejandro,points_carolina),end="")

utilicé contadores tal y como me pediste en los comentarios, si no deseas utilizar diccionarios y prefieres hacerlo de esta forma no hay problema, solo que esto también se puede resumir usando otra estructura de dato como listas [] o tuplas () o una mezcla de ambos, una lista de tuplas [(participante1,point),(participante2,points)]. Te dejo eso para que juegues y aprendas más :D