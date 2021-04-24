menú = """ 
Bienvenido al conversor de monedas 

1- Pesos Colombianos.
2- Pesos argentinos.
3- Pesos mexicanos

Elige una opción: """

opción = int(input(menú))

if opción == 1:
    pesos = input("¿Cuántos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opción == 2:
    pesos = input("¿Cuántos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
elif opción == 3:
    pesos = input("¿Cuántos pesos Méxicamos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")
else:
    print('Ingresa una opción correcta por favor')
