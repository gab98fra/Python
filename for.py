# ----------------------------------------------------------------------------
# Nombre:       for.py
# Autor:        Gabriel F
# Creado:       12 de Septiembre 2020
# Modificado:   12 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Diferentes maneras de implementar FOR

"""

#--------------Ejemplo 1:  FOR-----------------------
list1=[1,3,4,9,"Hello world"]

print("Forma 1: recorrer elementos de la list1\n")
for elem in range(len(list1)):
    print(list1[elem])


print("\nForma 2: recorrer elementos de la list1 \n")
for elem in list1:
    print(elem)


#--------------Ejemplo 2:  FOR-----------------------

tuple1=("Louis", "John", "Chary", "Andrew")

print("\nEnumera cada uno de los elementos de la tuple1 \n")
for elem in enumerate(tuple1, start=0):
    print(elem)


#--------------Ejemplo 3:  FOR-----------------------
print("\nRegistro del acumulador en cada iteración \n")
total = 0
for number in range(1, 10):
    total += number
    print (total)


#--------------Ejemplo 4:  FOR-----------------------
list2=[1,3,4,9,10,2, 3, 22, 48, 21]
print("\nCada elemento de la list2 es elevado a la 2 \n")

list2= [elem**2 for elem in list2]
print (list2)

print("\nLos elementos de la list2 mayores a 7 son elevados a la potecia 2 \n")
list2= [elem**2 for elem in list2 if elem>=7]
print(list2)

#--------------Ejemplo 5:  FOR-----------------------
print("\nCombinación de elem1 y elem2 solo si son diferentes \n")
list3=[(elem1, elem2) for elem1 in [1,2,3] for elem2 in [3,1,4] if elem1 != elem2]
print(list3)


#--------------Ejemplo 6:  FOR-----------------------
qs = ['name', 'quest', 'favorite color']
ans = ['lancelot', 'the holy grail', 'blue']
print("\nConcatenar elementos de dos listas \n")
for q, a in zip(qs, ans):
    print('What is your {0}?  It is {1}.'.format(q, a))

print ("\nFinalizado!!!!")
