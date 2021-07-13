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
    
  
  contador1 = 0
  
  for laminas in laminas_persona_1:
    if laminas not in laminas_persona_2:
      contador1 = contador1 + 1
  
  contador2 = 0
  for laminass in laminas_persona_2:
    if laminass not in laminas_persona_1:
      contador2 = contador2 + 1
      
      
  if  contador1 < contador2:
        resultado = contador1
  else:
        resultado = contador2
            
  return resultado