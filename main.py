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
        opciones_validas = PrintingModule.menu_disponibilidad(departamentos)
        choice_value = choice_sin_limpieza()
        if choice_value == 0:
            clear()
            continue
        elif choice_value == 1:
            opciones_validas = [x for x in range(0, len(departamentos)+1)]
            print("""
Seleccione el n° de serie del departamento que desea comprar
0. Regresar al menú principal""")
            print("")
            choice_value = choice()
            if choice_value == 0:       #Devuelve al menú principal
                continue
            elif choice_value == 1:       #Activa el menú de compra
                while True:
                    opciones_validas = PrintingModule.menu_compra(departamentos, choice_value)
                    choice_value_sin_limpieza = choice_sin_limpieza()
                    confirmacion_value = confirmacion()
                    if confirmacion_value == "n":
                        break

                    elif confirmacion_value == "y":
                        opciones_validas = PrintingModule.menu_salida(departamentos, departamentos_vendidos, choice_value)
                        choice()
                        break
        elif choice_value == 2:
            n = input("input: ")
            print(SearchandSortingModule.busqueda_filtrar_distrito(n,departamentos))
            time.sleep(2)
            continue
        elif choice_value == 3:
            n = input("input: ")
            print(SearchandSortingModule.busqueda_filtrar_habitaciones(n,departamentos))
            time.sleep(2)
            continue
        elif choice_value == 4:
            n = input("input: ")
            print(SearchandSortingModule.busqueda_filtrar_piso(n,departamentos))
            time.sleep(2)
            continue
        elif choice_value == 5:
            n = input("input: ")
            print(SearchandSortingModule.busqueda_filtrar_preciomax(n,departamentos))
            time.sleep(2)
            continue
        elif choice_value == 6:
            n = input("input: ")
            print(SearchandSortingModule.busqueda_filtrar_area(n,departamentos))
            time.sleep(2)
            continue
    #Activa el menú de departamentos disponibles          

    elif choice_value == 3:
        while True:
            opciones_validas = PrintingModule.menu_venta(departamentos_vendidos)
            choice_value = choice()
            if choice_value == 0:
                break
            elif choice_value == 1:
                SearchandSortingModule.ordenamiento_distrito(departamentos_vendidos)
                continue
            elif choice_value == 2:
                SearchandSortingModule.ordenamiento_fecha(departamentos_vendidos)
                continue
    elif choice_value == 4:
        c = confirmacion()
        if c == "y":    
            PrintingModule.guardar(departamentos,departamentos_vendidos)
            time.sleep(1.2)
            clear()
            continue
        elif c == "n":
            continue
    elif choice_value == 5:
        c = confirmacion()
        if c == "y":
            PrintingModule.leer(departamentos,departamentos_vendidos)
            time.sleep(1.2)
            clear()
            continue
        elif c == "n":
            continue
    elif choice_value == 0:     
        break
    #Termina el programa
