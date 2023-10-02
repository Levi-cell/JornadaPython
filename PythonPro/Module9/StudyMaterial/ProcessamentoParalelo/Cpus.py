"""Vamos verificar quantas CPUs o computador
possui para processar algoritmos"""

from multiprocessing import cpu_count

print(cpu_count())