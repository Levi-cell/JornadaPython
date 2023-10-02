"""Asyncio é outra biblioteca"""
from asyncio import get_event_loop, wait, sleep as sleep_async
from time import time


async def quadrado_do_numero(valor, delay):
    await sleep_async(delay)
    print(valor**2)

loop = get_event_loop()
inicio = time()
resultado1 = loop.create_task(quadrado_do_numero(2, 4))
resultado2 = loop.create_task(quadrado_do_numero(5, 1))
resultado3 = loop.create_task(quadrado_do_numero(3, 2))
loop.run_until_complete(wait([resultado1, resultado2, resultado3]))
loop.close()
termino = time()
print(f"Tempo total para execução: {abs(int(inicio-termino))} segundos")