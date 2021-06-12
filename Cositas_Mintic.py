licencia_conduccion = bool(int(input("¿Tiene licencia de conducción? Valor : Si=1  No=0: "))) 
cantidad_de_multas = int(input("Ingrese la cantidad de multas.: "))
grados_alcohol = float(input("Ingrese la cantidad de grados de alcohol en la sangre detectada: "))
velocidad = float(input("Ingrese la velocidad a la que se desplazaba el vehiculo: "))
papeles_regla = bool(int(input("¿Tiene los papeles en regla? Valor: Si=1  No=0: ")))
vidrios_polarizados = bool(int(input("¿tiene vidrios polarizados? Valor: Si=1  No=0: ")))
edad = int(input("Ingrese la edad: "))
puede_conducir = ((licencia_conduccion == True) and (cantidad_de_multas == 0) and (grados_alcohol == 0) and (papeles_regla == True) and (velocidad < 80) and (vidrios_polarizados == False) and (edad > 16))
if puede_conducir == True:
    print("True: Puede Seguir Conduciendo")
else:
    pass
    print("False: No Puede Conducir")