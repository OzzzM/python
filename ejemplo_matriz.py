cantidad_filas = int(input("Cantidad filas: "))
cantidad_columnas = int(input("Cantidad Columnas: "))

matrix = [] 

for indice_fila in range(cantidad_filas):
    fila = []
    for indice_columna in range(cantidad_columnas):
        componentes = int(input(f"Componente: fila:{indice_fila} columna: {indice_columna} = "))
        fila.append(componentes)
    matrix.append(fila)

for fila in matrix:
    print(fila)