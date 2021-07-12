def lista_clases():
    lista_de_laminas_daniel = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76']
    for i in range(len(lista_de_laminas_daniel)):
        lista_de_laminas_daniel[i] = int(lista_de_laminas_daniel[i])
        
    lista_ingresada = list(input("Ingrese la lista de faltantes: "))
    for j in range(len(lista_ingresada)):
        lista_ingresada[j] = int(lista_ingresada[j])
    
    print(lista_ingresada)
    print(lista_de_laminas_daniel)
    print(type(lista_de_laminas_daniel))
    print(type(lista_ingresada))
    
    cadena_contador = ""
    for tarjeta in range(len(lista_de_laminas_daniel)-1):
        if lista_de_laminas_daniel[tarjeta] == lista_de_laminas_daniel[tarjeta+1]:
            cadena_contador = cadena_contador + lista_de_laminas_daniel(tarjeta)
            
    print(cadena_contador)        


lista_clases()

def lista_clases():
    lista_de_laminas_daniel = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76']
    lista_ingresada_str = input("Ingrese la lista de faltantes: ")
    lista_ingresada = lista_ingresada_str.split(",")
        
    cadena_contador = ""
    for tarjeta in lista_de_laminas_daniel:
        if tarjeta in lista_ingresada:
            cadena_contador = cadena_contador + str(tarjeta)
    print(cadena_contador)

lista_clases()
    