# FORMA COMUM
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listaNova = []
for x in lista:
    listaNova.append(x*2)

print(listaNova)

# List comprehension

listaNova = [x*2 for x in lista]

print(listaNova)
