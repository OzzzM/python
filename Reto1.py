distancia_estimada = int(input("ingrese la distancia estimada en unidades astronómicas: "))
peso_base = 4
carga_util = (distancia_estimada*2) + peso_base
cantidad_combustible = (carga_util + distancia_estimada)//5

print(f"{distancia_estimada} {carga_util} {cantidad_combustible} ")

if cantidad_combustible <= 20:
    print("uno")
elif cantidad_combustible > 20 and cantidad_combustible <=30:
    print("dos")
elif cantidad_combustible > 30 and cantidad_combustible <=50:
    print("tres")
elif cantidad_combustible > 50:
    print("cuatro")
else:
    print("escribe un número entero")
