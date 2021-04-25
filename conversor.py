def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuántos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")

menú = """ 
Bienvenido al conversor de monedas 

1- Pesos Colombianos.
2- Pesos argentinos.
3- Pesos mexicanos

Elige una opción: """

opción = int(input(menú))

if opción == 1:
    conversor("colombianos", 3875)
elif opción == 2:
    conversor("Argentinos", 65)
elif opción == 3:
    conversor("Mexicanos", 24)
else:
    print('Ingresa una opción correcta por favor')
