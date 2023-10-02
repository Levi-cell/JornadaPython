"""Aqui vamos utilizar a função do módulo quadrado de forma
assincrona"""
from threading import Thread
from time import time
from Quadrado import quadrado_do_numero

inicio = time()

resultado1 = Thread(target=quadrado_do_numero(2, 4))
resultado2 = Thread(target=quadrado_do_numero(5, 1))
resultado3 = Thread(target=quadrado_do_numero(3, 2))

resultado1.start()
resultado2.start()
resultado3.start()

resultado1.join()
resultado2.join()
resultado3.join()

termino = time()
print(f"Tempo total para execução:{abs(int(inicio-termino))} segundos")