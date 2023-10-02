"""Criando fila de execução para os processosq"""
from multiprocessing import Queue

queue = Queue()

[queue.put(n) for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]]

while not queue.empty():
    print(queue.get())
    

