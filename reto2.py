#Primero hacemos una lista de todas las escuderías, para poder así asignar las favoritas de x personas, además de poder asignarles su respectiva inicial
A = "Alfa Romero"
B = "BMW Sauber"
C = "Racing Point"
E = "Mercedes"
F = "Ferrari"
H = "Haas"
I = "Force India"
L = "Lotus"
M = "McLaren"
N = "Renault"
O = "Manor"
P = "Alpine"
R = "Red Bull"
S = "Aston Martin"
T = "Toro Rosso"
U = "Marussia"
W = "Williams"
Z = "AlphaTauri"

# Declarar las escuderias favoritas de Alejandro y Carolina Respectivamente.
escuderias_fav_alejandro = "RAIFZ"
escuderias_fav_carolina = "UZEOF"
posibles_ganadoras = "ABCEFHILMNOPRSTUWZ"

ingreso_esc_fav_alejandro = input("Ingrese la lista de escuderías favoritas de Alejandro:\n")  

ingreso_esc_fav_carolina = input("Ingrese la lista de escuderías favortias de Carolina: \n")

ingreso_ganadores_tempo = input("Ingrese los ganadores de la temporada: ")

for i in ingreso_esc_fav_alejandro:
    for j in ingreso_ganadores_tempo:
        if(i==j):
            print("A")
            break
for k in ingreso_esc_fav_carolina:
    for j in ingreso_ganadores_tempo:
        if(k==j) and i:
            print("C")
            break
    

