"""Aqui é a mesas ideia, porém com uma sintaxe mais simples
"""

from concurrent import futures
from time import time
from Quadrado import quadrado_do_numero

inicio = time()

with futures.ProcessPoolExecutor() as executor:
   [e for e in executor.map(quadrado_do_numero, (2, 5, 3), (4, 1, 2))]

termino = time()

print(f"Tempo total para execução:{abs(int(inicio-termino))} segundos")