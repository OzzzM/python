def mostrar_matrix(matrix_a_mostrar):
  print("\n")
  print("-------------")
  for fila in matrix_a_mostrar:
    print(fila)
  print("-------------")

def create_matrix():
    cantidad_filas = int(input("Cantidad filas: "))
    cantidad_columnas = int(input("Cantidad Columnas: "))

    matrix = [] 

    for indice_fila in range(cantidad_filas):
        fila = []
        for indice_columna in range(cantidad_columnas):
            componentes = int(input(f"Componente: fila:{indice_fila} columna: {indice_columna} = "))
            fila.append(componentes)
        matrix.append(fila)
  
    return matrix

#la siguiente función verificará si se pueden sumar las dos matrices a insertar.

def pueden_sumarse(matrixA, matrixB):
    cantidad_filas_matrix_A = len(matrixA)
    cantidad_filas_matrix_B = len(matrixB)

    

    '''Esta sería una forma abreviada y práctica de escribir los 3 if de abajo:
    if (len(matrixA) <= 0) or (len(matrixB) <= 0) or (len(matrixA)) != (len(matrixB)): '''
    
    # se debe recordar que las matrices siempre deben ser del mismo tamaño, filas y columnas.
    if cantidad_filas_matrix_A != cantidad_filas_matrix_B:
        return False #Esto significa que no se pueden sumar.
    #La matriz A debe tener por lo menos 1 fila.    
    if cantidad_filas_matrix_A <= 0:
        return False
    #La matriz B debe tener por lo menos 1 fila.
    if cantidad_filas_matrix_B <= 0:
        return False
     # Esta parte que sigue, será más a modo de ejemplo sore: ¿cómo averiguar si todas las filas 
     # de las dos matrices tienen la misma cantidad de elementos
    for indice_fila in range(len(matrixA)): 
        matrixA_conteo_dentro_fila = len(matrixA[indice_fila])
        matrixB_conteo_dentro_fila = len(matrixB[indice_fila])

        if matrixA_conteo_dentro_fila != matrixB_conteo_dentro_fila:
            return False 
    #En este punto ya se deberia haber validado todo lo de atrás y entonces se podrian realizar
    #operaciones con esas matrices, por eso el: "return True".
    return True   

def sumar_matrices(matriz_A, matrizB):
    for indice_fila in range (len(matriz_A)):
        fila = matriz_A[0]
        for indice_columna in range (len(fila)):


matrix1 = create_matrix()
matrix2 = create_matrix()

mostrar_matrix(matrix1)
mostrar_matrix(matrix2)

'''Aquí luego de ingresar las dos matrices se realizarian las comprobaciones pertinentes anteriores
entonces para ello, se debe llamar a la función de: "pueden_sumarse. entonces para eso
creamo una variable e invocamos la función a la cuál le pasamos las dos matrices que ingresamos
a esto se le llamaria paso por valor."'''

validacion_suma = pueden_sumarse(matrix1, matrix2)
print()

#Una forma abreviada de realizar la orden anterior seria:

print(pueden_sumarse(matrix1, matrix2))

#En este punto se debe informar y retornar si las variable no se pueden sumar.
if validacion_suma == False:
    prin("Las Matrices no se pueden sumar debido a que son de distinto tamaño")
