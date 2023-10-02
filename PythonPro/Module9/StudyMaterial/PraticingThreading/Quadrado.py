"""Nesse módulo vamos declarar a função e fazer testes"""
from time import time, sleep


def quadrado_do_numero(valor, delay):
    sleep(delay)
    print(valor ** 2)


"""Apenas descomente a linha de baixo em diantes caso vá
executa este módulo, caso não comente ela novamente ou deixe comentada"""
# inicio = time()
#
# quadrado_do_numero(2, 4)
# quadrado_do_numero(5, 1)
# quadrado_do_numero(3, 2)
# termino = time()
# print(f"Tempo total para execução:{abs(int(inicio-termino))} segundos")
