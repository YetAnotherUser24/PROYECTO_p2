import time
import datetime
def menu():
    print("""
        INMOBILIARIA
    1. Registro de Departamentos
    2. Departamentos Disponibles
    3. Departamentos Vendidos
    4. Guardar en archivo
    5. Leer archivo
    0. Terminar el programa
    """)
    return([1,2,3,4,5,0])
#Esta función imprime el menú principal en la consola
#devuelve una lista de opciones válidas del menú

def menu_registro():
    print("""
        REGISTRAR DEPARTAMENTO
    """)
    direccion = str(input("Dirección: "))
    distrito = str(input("Distrito: "))
    piso = input("Piso: ")
    while True:
        try:
            piso = int(piso)
            if piso > 0:
                break
            else:
                print("ERROR - el piso debe ser un número entero positivo")
                piso = input("Piso: ")
        except ValueError:
            print("ERROR - el piso debe ser un número entero positivo")
            piso = input("Piso: ")
        
    nhabitaciones = input("Numero de habitaciones: ")
    while True:
        
        try:
            nhabitaciones = int(nhabitaciones)
            if nhabitaciones > 0:
                break
            else:
                print("ERROR - el numero de habitaciones debe ser un número entero positivo")
                nhabitaciones = input("Numero de habitaciones: ")
        except ValueError:
            print("ERROR - el numero de habitaciones debe ser un número entero positivo")
            nhabitaciones = input("Numero de habitaciones: ")
        
    area = input("Area en m2: ")
    while True:
        
        try:
            area = float(area)
            if area > 0:
                break
            else:
                print("ERROR - el área debe ser un numero positivo")
                area = input("Area en m2: ")
        except ValueError:
            print("ERROR - el área debe ser un numero positivo")
            area = input("Area en m2: ")
        
    precio = input("Precio S/: ")
    while True:
        
        try:
            precio = float(precio)
            if precio > 0:
                break
            else:
                print("ERROR - el precio debe ser un numero positivo")
                precio = input("Precio S/: ")
        except ValueError:
            print("ERROR - el precio debe ser un numero positivo")
            precio = input("Precio S/: ")
    
    return([direccion,distrito,piso,nhabitaciones,area,precio,(datetime.datetime.now()).strftime('%d/%m/%Y %H:%M')])
#Esta función imprime el menú de registro en la consola
#pide los datos da un departamentos 
#pide confirmación de los datos ingresados
#devuelve una lista con todos los datos obtenidos
  
def menu_registro_confirmado(departamentos,datos):
    departamentos.append(datos)
    print("""
---------------DEPARTAMENTO REGISTRADO CON ÉXITO---------------

0. Regresar al menu principal""")
    return([0])
#Esta función agrega un nuevo departamento a la matriz departamentos con los datos antes ingresados
#devuelve una lista con las opciones validas

def menu_disponibilidad(departamentos):
    print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format("n°","Distrito","Piso","n° hab","Área","Precio","Hora de registro"))
    for i in range(len(departamentos)):
      print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format(str(i+1),departamentos[i][1],departamentos[i][2],departamentos[i][3],str(departamentos[i][4])+" m2","S/. "+str(departamentos[i][5]),departamentos[i][6]))

    print("""
0. Regresar al menú principal
1. Comprar departamento
2. Filtrar por distrito
3. Filtrar por numero de habitaciones
4. Filtrar por precio maximo
5. Filtrar por piso maximo
6. Filtrar por area minima
""")
    return([0,1,2,3,4,5,6])
#Esta función imprime los departamentos disponibles organizados según su número de serie
#devuelve una lista con las opciones validas

def menu_compra(departamentos, choice_value):
    print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format("n°","Distrito","Piso","n° hab","Área","Precio","Hora de registro"))
    print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format(str(choice_value),departamentos[choice_value-1][1],departamentos[choice_value-1][2],departamentos[choice_value-1][3],str(departamentos[choice_value-1][4])+" m2","S/. "+str(departamentos[choice_value-1][5]),departamentos[choice_value-1][6]))
    nombre = input("Nombre: ")
    DNI = input("DNI: ")
    while True:
        if len(str(DNI)) == 8:
            try:
                DNI = int(DNI)
                break
            except ValueError:
                print("ERROR - el DNI debe tener 8 dígitos")
                continue
        else:
            print("ERROR - el DNI debe tener 8 dígitos")
            DNI = input("DNI: ")
        
        
    email_ = "-1"
    while "@" not in str(email_):
        email_ = input("email: ")
        if "@" not in str(email_):
            print("ERROR - el email debe contener un '@")
    print("""Medios de pago:
    1. VISA
    2. Trasferencia
    3. Credito hipotecario
    """)
    
    return[1,2,3]
#Esta función pide elegir un departamento disponible para comprar
#pide los datos personales del usuario
#valida los datos del usuario
#pregunta por confirmación sobre las entradas al usuario
#devuelve una lista de opciones válidas del menú

def menu_salida(departamentos,departamentos_vendidos,choice_value):
    departamentos_vendidos.append(departamentos[choice_value-1][:-1])
    departamentos_vendidos[len(departamentos_vendidos)-1].append((datetime.datetime.now()).strftime('%d/%m/%Y %H:%M'))
    del departamentos[choice_value - 1]
    print("""
---------------COMPRA REALIZADA CON ÉXITO---------------
0. Regresar al menú principal""")
    return[0]
#Esta función agrega el departamento comprado por el usuario a la matriz de departamentos vendidos
#elimina el departamento comprado de la matriz de departamentos disponibles
#devuelve una lista de opciones válidas del menú

def menu_venta(departamentos_vendidos):
    print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format("n°","Distrito","Piso","n° hab","Área","Precio","Hora de registro"))
    for i in range(len(departamentos_vendidos)):
      print("{:<4} {:<20} {:<6} {:<10} {:<15} {:<15} {:<10}".format(str(i+1),departamentos_vendidos[i][1],departamentos_vendidos[i][2],departamentos_vendidos[i][3],str(departamentos_vendidos[i][4])+" m2","S/. "+str(departamentos_vendidos[i][5]),departamentos_vendidos[i][6]))
    #print(departamentos_vendidos)
    #for i in range(len(departamentos_vendidos)):
    #    print(i+1, departamentos_vendidos[i])
    print("Total: S/. ", sum([float(departamentos_vendidos[i][5]) for i in range(len(departamentos_vendidos))]))
    print("")
    print("0. Regresar al menú principal")
    print("1. Ordenar por distritos")
    print("2. Ordenar por fecha")
    return[0,1,2]
#Esta función imprime los departamentos vendidos ordenados por número de serie
#devuelve una lista de opciones válidas del menú

def guardar(departamentos,departamentos_vendidos):
  fileR = open("archivo_registrados.txt","w")
  fileV = open("archivo_vendidos.txt","w")
  for listas in departamentos:
    for e in listas:
      fileR.write(str(e)+",")
    fileR.write("\n")
  fileR.close()
  for listas in departamentos_vendidos:
    for e in listas:
      fileV.write(str(e)+",")
    fileV.write("\n")
  fileV.close()

def leer(departamentos,departamentos_vendidos):
  n=open("archivo_registrados.txt","r")
  lineas1 = n.readlines()

  m=open("archivo_vendidos.txt","r")
  lineas2 = m.readlines()

  for i in range(len(lineas1)):
    depa = lineas1[i].split(",")[:-1]
    if depa not in departamentos:
      departamentos.append(depa)
  n.close()
  for i in range(len(lineas2)):
    depa = lineas2[i].split(",")[:-1]
    if depa not in departamentos:
      departamentos_vendidos.append(depa)
  m.close()















