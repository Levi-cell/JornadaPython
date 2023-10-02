import numpy as np

# criando arrays multidimensionais de numeros inteiros
print("criando arrays multidimensionais de numeros inteiros")


b = np.array([[1, 2, 3], [3, 4, 5]])
print(b)
print(type(b))

print(" ")

# o comando shape retorna uma tupla com as dimensões do objeto b
print("o comando shape retorna uma tupla com as dimensões do objeto b")
print(b.shape)
print(" ")

# o comando ndim retorna um número indicando a quantidade de dimensões do objeto b
print("o comando ndim retorna um número indicando a quantidade de dimensões do objeto b")
print(b.ndim)
print(" ")

# criando arrays multidimensionais de numeros floats
print("criando arrays multidimensionais de numeros floats ")
c = np.array([[1.1, 2, 3], [3, 4, 5]])
print(c)
print(type(b), type(c))
print(" ")

# criando arrays apenas com os numeros zeros automaticamente
print("criando arrays apenas com os numeros zeros automaticamente ")

zeros_array = np.zeros((2, 3))
print(zeros_array)
print("As dimensões do array são:", zeros_array.shape)
print("Quantidade de dimensões do array", zeros_array.ndim)
print(" ")

# criando arrays apenas com os numeros uns automaticamente
print("criando arrays apenas com os numeros zeros automaticamente ")
ones_array = np.ones((1, 5), dtype=np.int32) #especificando dtype
print(ones_array)
print(" ")

# criando uma matriz identidade (Numeros 1 na diagonal e zero no restante da matriz)
print("criando uma matriz identidade (Numeros 1 na diagonal e zero no restante da matriz) ")
print(np.eye(4))
print(" ")

# cria um array no intervalo definido, com números uniformemente espaçados
print("cria um array no intervalo definido, com números uniformemente espaçados ")
print(np.linspace(0, 10, 10))
print(" ")

# crie uma matriz / array no formato fornecedio, preenchido com amostras aleatórias de uma distruibução
print("crie uma matriz / array no formato fornecedio, preenchido com amostras aleatórias de uma distruibução  ")
a = np.random.rand(5)
# a = np.random.rand(5)*100
# a = np.random.rand(5, 2, 3) # cubo
print(a)
print(" ")

# cira um array com 18 elementos
print("cira um array com 18 elementos ")
a = np.arange(18)
print(a)
print(" ")

# cria um array no intervalo de 0 a 30 com elementos incrementados de 3
print("cria um array no intervalo de 0 a 30 com elementos incrementados de 3 ")
b = np.arange(0, 30, 3)
print(b)
print(" ")

# acessando um elemento na posição zero do array criado
print("acessando um elemento na posição zero do array criado")
print(b[0])
print(" ")

# acessando um intervalo definido de valores do array
print(" acessando um intervalo definido de valores do array ")
print(b[2:6])
print(" ")

# acessando todos os valores a partir do indice estipulado
print("acessando todos os valores a partir do indice estipulado ")
print(b[2:])
print(b[:5])
print(" ")

# atribuindo valores em uma determinada posição do array
print("atribuindo valores em uma determinada posição do array ")
b[2] = 100
print(b)
print(" ")

# atribuindo novos valores no intervalo de 0 a 50 no formato de matriz com 5 linhas e 10 colunas
print("atribuindo novos valores no intervalo de 0 a 50 no formato de matriz com 5 linhas e 10 colunas ")
b = np.arange(50).reshape(5,10)
print(b)
print(" ")

# verificando a forma criada
print("verificando a forma criada")
print(b.shape)
print(" ")

# extrando dados de um intervalo especifico ( primeiro colchete) - > linhas e segundo colchete -> coluna
print("extrando dados de um intervalo especifico ( primeiro colchete) - > linhas e segundo colchete -> coluna ")
print(b[:4][:])
print(" ")