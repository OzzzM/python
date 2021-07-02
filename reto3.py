
entradas_user = input()
lista = entradas_user.split(" ")
contador = 1
cadena_contador = ""
cadena_palabras = ""


for indice in range((len(lista)-1)):
    
    if lista[indice] == lista[indice+1]:     
        contador += 1 
    else:
        cadena_contador = cadena_contador + str(contador) + " "
        cadena_palabras = cadena_palabras + lista[indice] + " " 
        contador = 1     

cadena_contador = cadena_contador + str(contador)
cadena_palabras = cadena_palabras + lista[indice]

print(cadena_palabras)
print(cadena_contador)



