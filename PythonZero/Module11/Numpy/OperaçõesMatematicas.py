import numpy as np

# criando um conjunto de numeros aleatórios
print("criando um conjunto de numeros aleatórios ")
print(np.random.seed(42))
print(" ")

# criando arrays usando o módulo randomico do numpy
print("criando arrays usando o módulo randomico do numpy ")

a = np.random.randint(1, 3, 5)
b = np.random.randint(0, 10, 5)

print(a)
print(b)
print(" ")

# subtração

print("subtração:")
print(np.subtract(b,a))
print(" ")

# adição
print("adição:")
print(np.add(b, a))
print(" ")

# divisão
print("divisão:")
print(np.divide(a,b))
print(" ")

# multiplicação
print("multiplicação:")
print(np.multiply(a, b))
print(" ")

# exponencial
print("exponencial:")
print(np.exp(a))
print(" ")

# raiz quadrada
print("raiz quadrada:")
print(np.sqrt(a))
print(" ")

# computar o seno
print("computar o seno:")
print(np.sin(a))
print(" ")

# Logartimo
print("Logartimo:")
print(np.log(a))
print(np.log2(a))
print(" ")

# como arredonda uma matriz
print("como arredonda uma matriz:")
np.random.seed(42)
a = np.random.rand(5)
print(a)
print(np.around(a))
