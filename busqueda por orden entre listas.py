lista1 = [2, 3, 1, 5, 7]
lista2 = [3, 3, 8, 5, 0]

for indice, (item1, item2) in enumerate(zip(lista1, lista2)):
    if item1 == item2:
        print(f"{item1} se encuentra en ambas listas en el índice {indice}")