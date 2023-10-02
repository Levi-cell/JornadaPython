lista = list(range(1, 11))

for x in lista:
    print(x)

print("-----------")
lista = iter(lista)

for x in range(1, 11):
    print(next(lista))