def busqueda_filtrar_distrito(n,departamentos):
  departamentos_distrito=[]
  for i in range(len(departamentos)):
    if departamentos[i][1] == n :     
      departamentos_distrito.append(departamentos[i])
  if len(departamentos_distrito)!=0:
    return departamentos_distrito
  else:
    return "No hay departamentos disponibles en ese distrito"
    
def busqueda_filtrar_habitaciones(n,departamentos):
  departamentos_habitaciones=[]
  for i in range(len(departamentos)):
    if departamentos[i][3] == n :
      departamentos_habitaciones.append(departamentos[i])
  if len(departamentos_habitaciones)!=0:
    return departamentos_habitaciones
  else:
    return "No hay departamentos con ese número de habitaciones"

def busqueda_filtrar_preciomax(n,departamentos):
  departamentos_preciomax=[]
  for i in range(len(departamentos)):
    if departamentos[i][5] <= n :
      departamentos_preciomax.append(departamentos[i])
  if len(departamentos_preciomax) != 0:
    return departamentos_preciomax
  else:
    return "No hay departamentos con un precio menor a S/."+n
  
def busqueda_filtrar_piso(n,departamentos):
  departamentos_piso=[]
  for i in range(len(departamentos)):
    if departamentos[i][2] >= n :
      departamentos_piso.append(departamentos[i])
  if len(departamentos_piso)!=0:
    return departamentos_piso
  else:
    return "No hay departamentos disponibles con ese numero de piso máximo"

def busqueda_filtrar_area(n,departamentos):
  departamentos_area=[]
  for i in range(len(departamentos)):
    if departamentos[i][4] >= n :
      departamentos_area.append(departamentos[i])
  if len(departamentos_area)!=0:
    return departamentos_area
  else:
    return "No hay departamentos disponibles con esa area minima"

def ordenamiento_distrito(departamentos_vendidos):
  for tope in range(len(departamentos_vendidos)-1,0,-1):
    for i in range(tope):
      if departamentos_vendidos[i][1] > departamentos_vendidos[i+1][1]:
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i]

def ordenamiento_fecha(departamentos_vendidos):
  for tope in range(len(departamentos_vendidos)-1,0,-1):
    for i in range(tope):
      if departamentos_vendidos[i][-1] < departamentos_vendidos[i+1][-1]:
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i]

