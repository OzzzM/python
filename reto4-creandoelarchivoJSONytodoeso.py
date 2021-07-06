#ESTE EJERCICIO QUEDO A MEDIAS, POR QUE NO ERA NECESARIO EL WITH OPEN sim embargo se puede complementar con el reto4.py
import json
#Recibir "diccionario en json" pero como el input lo recibe en str lo convertirmos a un dict
diccionario = input("Ingrese el diccionario: ")

diccionario_convertido = json.loads(diccionario)

# print(type(diccionario_convertido))
# convertir json a diccionario de python.

with open("diccionario_convertido.json", "w") as f:
    json.dump(diccionario_convertido, f, indent=4)
    
# with open("diccionario_convertido.json", "r") as file:
#     diccionario_convertido = file.readlines()

# print(diccionario_convertido)

lista_faltantes = input("Ingrese las laminas que le faltan: ").split(" ")

# print(lista_faltantes)
contador = 0
for tarjeta in diccionario_convertido:
    
    if tarjeta in lista_faltantes:
        print(f"{tarjeta}")
        # contador += diccionario_convertido