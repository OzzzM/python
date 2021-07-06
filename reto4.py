import json

diccionario = input("Ingrese el diccionario: ")
lista_faltantes = input("Ingrese las laminas que le faltan: ").split(" ")
diccionario_convertido = json.loads(diccionario)

total = 0 
cadena_contador = ""
for tarjeta in lista_faltantes:
    
    if tarjeta in diccionario_convertido:
        total += diccionario_convertido[tarjeta] 
        cadena_contador = cadena_contador + str(tarjeta) + " "
print(f"{total}, {cadena_contador}", end="")