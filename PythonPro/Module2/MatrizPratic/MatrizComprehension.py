import time
matriz = [[25.0,20.0,19.3,15.9],[18.7, 24.5, 17.8, 19.9], [22.4, 19.2, 15.9, 23.8]]


inicio = time.time()

novaMatriz = [[elemento*2 for elemento in linha]for linha in matriz]

print(novaMatriz)

fim = time.time()

print(f"Tempo de execução: {fim-inicio}")