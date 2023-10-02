import time

inicio = time.time()
lista = []
listaNova = []

for x in range(10001):
    lista.append(x)

for x in lista:
    x = x*2
    listaNova.append(x)

print(listaNova)
fim = time.time()

print(f"tempo de execução: {fim-inicio}")
