def encuentraMenor(arreglo):
    menor=arreglo[0]
    menor_indice=0
    for i in range(1, len(arreglo)):
        if arreglo[i] < menor:
         menor=arreglo[i]
         menor_indice=i
    return menor_indice
def ordenacionPorSeleccion(arreglo):
 nuevoArreglo=[]
 for i in range(len(arreglo)):
     menor=encuentraMenor(arreglo)
     nuevoArreglo.append(arreglo.pop(menor))
 return nuevoArreglo

print(ordenacionPorSeleccion([5, 3, 6, 2, 10]))