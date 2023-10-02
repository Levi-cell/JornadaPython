import numpy as np
print(np.__version__)
# uma forma

lista = [1, 2, 3]
a = np.array(lista)
print(a)
print(type(a))

# outra forma
a = np.array([1, 2, 3])
print(a)
print(type(a))

# Criando arrays com tipos de dados diferentes

lista = [1, 2, "mentorama", 3, 4]
a = np.array(lista)
print(a)
print(type(a))

print(a.shape)