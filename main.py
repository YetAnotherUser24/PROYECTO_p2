import os
import time
import PrintingModule       #Módulo creado para imprimir menús
import SearchandSortingModule
import datetime
def clear():        
    os.system("clear")
#Esta función limpia la consola mediante la libreria os

def choice(opcion=-1):      #Esta función valida la entrada del usuario, se usa un -1 como defecto para entrar al bucle
    while opcion not in opciones_validas:       #comprueba que la entrada este en la lista de opciones validas
        opcion = (input("Opción: "))
        try:
            opcion = int(opcion)        
        except ValueError:
            opcion = str(opcion)
        if opcion not in opciones_validas:
            print("ERROR - seleccione una opción válida")       #Se intenta convertir la entrada en entero y en caso no se pueda la vuelve a pedir
    clear()     #limpia la consola
    return(opcion)      #Nos permite guardar la entrada válida del usuario

def choice_sin_limpieza(opcion=-1):     
    while opcion not in opciones_validas:
        opcion = (input("Opción: "))
        try:
            opcion = int(opcion)
        except ValueError:
            opcion = str(opcion)
        if opcion not in opciones_validas:
            print("ERROR - seleccione una opción válida")
    return(opcion)
#Esta función es igual a la funcion choice(), sin embargo esta no limpia la consola al final

def confirmacion(respuesta="1"):        #Esta función pregunta al usuario si esta seguro de sus entradas
    respuesta = input("""
¿Desea confirmar el registro?
Escriba 'y' para sí y 'n' para no
""").lower()
    while respuesta != "y" and respuesta != "n": 
        respuesta = input("""
ERROR - vuelva a intentarlo
Escriba 'y' para confirmar y 'n' para cancelar
""")
    if respuesta == "y":        #Si coloca y, el programa sigue normalmente
        print("")
    elif respuesta == "n":      #Si coloca n, se cancela la operación y se regresa al menú principal
        print("REGRESANDO AL MENU...")
        time.sleep(2)
        clear()
    return(respuesta)       #Nos permite saber la respuesta del usuario a la pregunta de confirmación

departamentos = []      #Matriz de departamentos, crece mediante el registro de departamentos y decrece mediante la venta de uno
departamentos_vendidos = []     #Matriz de departamentos vendidos, crece mediante la compra de departamentos por parte del usuario


while True:     #Permite correr al programa todo el tiempo hasta que el usuario lo decida
    opciones_validas = PrintingModule.menu()
    choice_value = choice()
    if choice_value == 1:
        while True:
            datos = PrintingModule.menu_registro()
            confirmacion_value = confirmacion()
            if confirmacion_value == "n":
                break
            elif confirmacion_value == "y":
                opciones_validas = PrintingModule.menu_registro_confirmado(departamentos,datos)
                choice()
                break
    #Activa el menú de registro

    elif choice_value == 2:
        d = departamentos
        while True:
            if isinstance(d,str):
                print(d)
                print("0. Regresar al menú principal")
                opciones_validas = [0]
                choice()
                break
            else:
                opciones_validas = PrintingModule.menu_disponibilidad(d)
                choice_value = choice_sin_limpieza()
                if choice_value == 0:
                    clear()
                    break
                elif choice_value == 1:
                    opciones_validas = [x for x in range(0, len(d)+1)]
                    print("""
Seleccione el n° de serie del departamento que desea comprar
0. Regresar al menú principal""")
                    print("")
                    choice_value = choice()
                    if choice_value == 0:       #Devuelve al menú principal
                        continue
                    else:       #Activa el menú de compra
                        while True:
                            opciones_validas = PrintingModule.menu_compra(d, choice_value)
                            choice_sin_limpieza()
                            confirmacion_value = confirmacion()
                            if confirmacion_value == "n":
                                break

                            elif confirmacion_value == "y":
                                opciones_validas = PrintingModule.menu_salida(departamentos, departamentos_vendidos, choice_value)
                                choice()
                                break
                        break
                elif choice_value == 2: #Filtrar por distrito
                    n = input("Distrito: ")
                    d = SearchandSortingModule.busqueda_filtrar_distrito(n,d)#devuelve una matriz con los departamentos que estan en el distrito buscado
                    clear()
                    continue
                elif choice_value == 3:#Filtrar por n° habitacion
                    n = int(input("n° de habitaciones: "))
                    d = SearchandSortingModule.busqueda_filtrar_habitaciones(n,d)#devuelve una matriz con los departamentos que tienen el n° de habitaciones buscado
                    clear()
                    continue
                elif choice_value == 4: #Filtrar numero de pisos max
                    n = int(input("Número de pisos máximo: "))
                    d = SearchandSortingModule.busqueda_filtrar_piso(n,d)#devuelve una matriz con los departamentos que estan en el piso 1 hasta n piso
                    clear()
                    continue
                elif choice_value == 5:#Filtrar por precio maximo
                    n = float(input("Precio máximo: "))
                    d = SearchandSortingModule.busqueda_filtrar_preciomax(n,d)#devuelve una matriz con los departamentos que tienen un precio $0 hasta n precio
                    clear()
                    continue
                elif choice_value == 6:#Filtrar por area minima
                    n = float(input("Área mínima: "))
                    d = SearchandSortingModule.busqueda_filtrar_area(n,d)#devuelve una matriz con los departamentos que tienen un area n a mas 
                    clear()
                    continue
    #Activa el menú de departamentos disponibles          

    elif choice_value == 3:
        while True:
            opciones_validas = PrintingModule.menu_venta(departamentos_vendidos)
            choice_value = choice()
            if choice_value == 0:
                break
            elif choice_value == 1: #Ordenar por distrito
                SearchandSortingModule.ordenamiento_distrito(departamentos_vendidos)#Ordena la matriz o tabla de depas vendidos por orden alfabetico
                continue
            elif choice_value == 2: #Ordenar por fecha de compra
                SearchandSortingModule.ordenamiento_fecha(departamentos_vendidos)#Ordena la matriz o tabla de depas vendidos por numero de fecha de manera descendente
                continue
            elif choice_value == 3:
                SearchandSortingModule.ordenamiento_precio(departamentos_vendidos)
            elif choice_value == 4:
                SearchandSortingModule.ordenamiento_area(departamentos_vendidos)
    elif choice_value == 4: #Guarda las matrices departamentos y departamentos_vendidos en su archivo correspondiente
        print("Recuerda leer el archivo antes de guardar :D")
        c = confirmacion()
        if c == "y":    
            PrintingModule.guardar(departamentos,departamentos_vendidos)
            time.sleep(1.2)
            clear()
            continue
        elif c == "n":
            continue
    elif choice_value == 5: #Agregar los elementos de los archivos a cada matriz
        c = confirmacion()
        if c == "y":
            PrintingModule.leer(departamentos,departamentos_vendidos)
            time.sleep(1.2)
            clear()
            continue
        elif c == "n":
            continue
    elif choice_value == 6:     
        break
    #Termina el programa
