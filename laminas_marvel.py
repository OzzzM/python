def lista_clases(clases):
     
  contador = []
  for tarjeta in clases:
       if tarjeta not in contador:
           contador.append(tarjeta)

  return contador

def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  #resultado = []
  
  lista_indices = indices[len(indices.index)]
  
  return resultado