def busqueda_filtrar_distrito(n,departamentos): 
  departamentos_distrito=[] #Nueva matriz de departamentos que cumplan con la condicion
  for i in range(len(departamentos)): 
    if departamentos[i][1] == n :  #Compara el dato con el dato solicitado
      departamentos_distrito.append(departamentos[i]) #Agrega el depa a la nueva matriz
  if len(departamentos_distrito)!=0: #Si la nueva matriz no esta vacia retorna la matriz
    return departamentos_distrito
  else: #Si la nueva matriz esta vacia, devuelve un mensaje indicado
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
    return "No hay departamentos con un precio menor a S/."+str(n)
  
def busqueda_filtrar_piso(n,departamentos):
  departamentos_piso=[]
  for i in range(len(departamentos)):
    if departamentos[i][2] <= n :
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

def ordenamiento_distrito(departamentos_vendidos): #Ordenar por orden alfabetico el nombre de los distritos
  for tope in range(len(departamentos_vendidos)-1,0,-1): #Para evitar list out of ranger, se tiene un tope
    for i in range(tope): 
      if departamentos_vendidos[i][1] > departamentos_vendidos[i+1][1]: #Compara un elemento con el elemento siguiente a el
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i] #Si se verifica que estan desordenados, cambian su posicion

def ordenamiento_fecha(departamentos_vendidos):
  for tope in range(len(departamentos_vendidos)-1,0,-1):
    for i in range(tope):
      if departamentos_vendidos[i][-1] < departamentos_vendidos[i+1][-1]:
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i]

def ordenamiento_precio(departamentos_vendidos):
  for tope in range(len(departamentos_vendidos)-1,0,-1):
    for i in range(tope):
      if departamentos_vendidos[i][-2] < departamentos_vendidos[i+1][-2]:
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i]

def ordenamiento_area(departamentos_vendidos):
  for tope in range(len(departamentos_vendidos)-1,0,-1):
    for i in range(tope):
      if departamentos_vendidos[i][-3] < departamentos_vendidos[i+1][-3]:
        departamentos_vendidos[i],departamentos_vendidos[i+1] = departamentos_vendidos[i+1],departamentos_vendidos[i]