def busqueda_binaria(list, item):
  menor = 0
  mayor =len(list) - 1

  while menor <= mayor:
    medio = (menor+mayor) // 2
    estimado = list[medio]
    if estimado == item:
      return medio
    if estimado > item:
      mayor = medio-1
    else:
       menor=medio+1
  return None
#se intentó definir el nombre de la lista en español pero al momento de imprimirla por consola salia un error se 
#probó con inglés y funcionó perfectamente O.o
mi_list = [1, 3, 5, 7, 9]

print(busqueda_binaria(mi_list, 3))
print(busqueda_binaria(mi_list, -1))