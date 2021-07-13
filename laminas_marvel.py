def lista_clases(clases):
     
  contador = []
  for tarjeta in clases:
       if tarjeta not in contador:
           contador.append(tarjeta)

  return contador

def laminas_faltantes_por_clase(indices, clases, clase_a_verificar):
  
  resultado = []
  for indice in indices:
    if clases[indice] == clase_a_verificar:
      resultado.append(indice)
    
  return resultado

def laminas_faltantes(laminas_persona_1, laminas_persona_2):
  resultado2 = []
  
  for lamina in laminas_persona_1:
    if lamina not in laminas_persona_2:
      resultado2.append(lamina)

  return resultado2

def cantidad_laminas_cambiables(laminas_persona_1, laminas_persona_2):
  resultado3 = 0
  
  for laminas in laminas_persona_1:
    if laminas not in laminas_persona_2:
      resultado3 = resultado3 + laminas
  return resultado3