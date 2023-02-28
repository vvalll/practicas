# Método tradicional
'''
lista = []
for letra in 'casa':
    lista.append(letra)
print(lista)

#Comprehension 

listaa = [letra for letra in "casa"]
print(listaa)
'''
# Método tradicional
'''
lista = []
for numero in range(0,11):
    lista.append(numero**2)
print(lista)

#Comprehension 

listas = [numero ** 2 for numero in range (0,11)]
print(listas)
'''

# Método tradicional: Crear una lista con los todos los múltiples de 2 entre 0 y 10:
'''
lista = []
for numero in range(0,11):
    if numero % 2 == 0:
        lista.append(numero)
print(lista)

#Comprehension 

listas = [i for i in range(0, 11) if i%2 ==0]
print(listas)

'''

# Método tradicional
'''
lista = []
for numero in range(0,11):
    lista.append(numero**2)

pares = []   
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#Comprehension

listas = [i**2 for i in range(0,11) if i % 2 == 0]
print(listas)
'''

#Cree una lista idéntica a partir de la primera lista mediante la comprensión de listas.

'''
lista1 = ['a', 1, 'b', 2, 'c', 3]
lista2 = [lista2 for lista2 in lista1]
print(lista2)
'''

#construir una nueva lista, pero agregue 6 a cada elemento.

'''
lista = [22, 9, 6, 11, 3]
listas = [i+6 for i in lista]
print(listas)
'''

#construya una lista a partir de los cuadrados de cada elemento de la lista, si el cuadrado es mayor que 50.
'''
lista = [2, 4, 6, 8, 10, 12, 14]
listas = [i**2 for i in lista if (i ** 2) > 50]
print(listas)
'''

#Elaborar una lista de los nombres de los vehículos con un peso inferior a 2000 kilogramos. En la misma lista, la comprensión hace que los nombres clave estén todos en mayúsculas.

'''
dicc={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

listas = [i.upper() for i in dicc if dicc[i] < 2000]
print(listas)
'''

#Cree una lista idéntica a partir de la primera lista mediante la comprensión de listas

'''
lista1 = [1,2,3,4,5]
lista2 = [i for i in lista1]
print(lista2)
'''

#construya una lista a partir de los cuadrados de cada elemento de la lista.
'''
lista1 = [2,4,6,8,10]
lista2 = [i**2 for i in lista1]
print(lista2)
'''
v = "a"

print(v.islower())