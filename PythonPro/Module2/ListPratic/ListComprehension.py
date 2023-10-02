import time

inicio = time.time()

lista = []
listaNova = []

for x in range(10001):
    lista.append(x)

listaNova = [x*2 for x in lista]
print(listaNova)

fim = time.time()

print(f"tempo de execução: {fim-inicio}")
