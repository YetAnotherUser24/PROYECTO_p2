import random

#def bubblesort(lista):
#    iter = 0
#    for tope in range(len(lista)-1,0,-1):
#        for i in range(tope):
#            if lista[i] > lista[i+1]:
#                lista[i], lista[i+1] = lista[i+1], lista[i]
#        iter += 1
#    return(lista,iter)
    

#lista = [random.randint(1,1000) for i in range(20)]
#print(bubblesort(lista))
#
#def bubblesort(lista):
#    for tope in range(len(lista)-1,0,-1):
#        for i in range(tope):
#            if len(lista[i]) > len(lista[i+1]):
#                lista[i], lista[i+1] = lista[i+1], lista[i]
#    return(lista)
#
#n = int(input("Número de palabras: "))
#palabras = []
#for i in range(n):
#    palabra = input("Palabra "+str(i+1)+":")
#    palabras.append(palabra)
#
#print(bubblesort(palabras))


"""def bubblesort(lista):
    vocales = "aeiou"
    for tope in range(len(lista)-1,0,-1):
        for i in range(tope):
            if len([v for v in lista[i] if v.lower() in vocales]) > len([v for v in lista[i+1] if v.lower() in vocales]):
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return(lista)


n = int(input("Número de palabras: "))
palabras = []
for i in range(n):
    palabra = input("Palabra "+str(i+1)+":")
    palabras.append(palabra)

print(bubblesort(palabras))"""

def bubble_sort_codigo(lista):
 for tope in range(len(lista)-1, 0, -1):
   for i in range(tope):
     if lista[i][1] > lista[i+1][1] :
       lista[i], lista[i+1] = lista[i+1], lista[i]

dic = {'Jose': 12349, 'Andrea': 12347, 'Mateo': 12343, 'Luciana': 12341, 'Julio': 12345}
lista = list(dic.items())
print(lista)
bubble_sort_codigo(lista)
print(lista)
