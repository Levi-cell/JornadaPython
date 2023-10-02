import asyncio
import time


def soma(a,b):
    print("Iniciando soma")
    print(f"{a} + {b} = {a + b}")
    print("Finalizando soma")


def multiplica(a,b):
    print("Iniciando multiplicacao")
    print(f"{a} * {b} = {a * b}")
    print("Finalizando multiplicacao")


inicio=time.time()
print("Iniciando programa")
task1 = soma(10,5)
task2 = multiplica(4,8)
print("Finalizando programa")
fim=time.time()
print(f"Tempo de execução {fim-inicio}")