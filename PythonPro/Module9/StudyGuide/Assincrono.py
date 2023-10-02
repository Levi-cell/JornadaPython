import asyncio
import time

async def soma(a,b):
    print("Iniciando soma")
    print(f"{a} + {b} = {a + b}")
    print("Finalizando soma")

async def multiplica(a,b):
    print("Iniciando multiplicacao")
    print(f"{a} * {b} = {a * b}")
    print("Finalizando multiplicacao")


inicio=time.time()
print("Iniciando programa")

await soma(3, 4)
await multiplica(5, 5)

print("Finalizando programa")
fim=time.time()
