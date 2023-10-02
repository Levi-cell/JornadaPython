import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


############ NUMPY
# Criação array com 6 notas de 1 aluno
# Array 1 dimensão

notasAluno = np.array([5, 4, 3.1, 2, 5, 8])
print("notasAluno")
print(" ")
# tamanho
print(notasAluno.shape)
print(" ")

notasPorAlunos = np.array([[10, 20, 3.5, 10, 5, 9], [10, 20, 30, 5, 10, 9], [20, 20, 40, 9, 1, 10]])
print(notasPorAlunos)
print(" ")
# tamanho
print(notasPorAlunos.shape)
print(" ")

notasPorAlunosPorAno = np.array([[[9, 3, 3, 10, 1, 9], [5, 20, 3.5, 10, 5, 8], [2, 5, 9, 10, 7, 9],
                                  [10, 7, 4, 10, 5, 9], [9, 20, 7, 10, 5, 9], [3, 8, 9, 10, 4, 1]]])
print(" ")
print(notasPorAlunosPorAno)
print(" ")
# tamanho
print(notasPorAlunosPorAno.shape)
print(" ")


################ PANDAS

notasAlunosSeries = pd.Series([5, 4, 3.1, 2, 5, 8])
print(notasAlunosSeries)
print(" ")

notasAlunosSeriesIndex = pd.Series([5, 4, 3.1, 2, 5, 8],
                                   index=["prova 1", "prova 2", "prova 3", "prova 4", "prova 5", "prova 6"])

print(notasAlunosSeriesIndex)
print(" ")
# Pega somente os valores
print(notasAlunosSeries.values)
print(" ")

# Analisa os índices. Começa em 0, tem 6 posições e as posições caminham de 1 em 1
print(notasAlunosSeries.index)
print(" ")

print(notasAlunosSeriesIndex.index)
print(" ")

# Recupera a nota relacionada ao indice prova 1
print(notasAlunosSeriesIndex["prova 1"])
print(" ")


####### CRIANDO DATAFRAME

dataFrame1 = pd.DataFrame({'Aluno': ["João", "Maria", "Pedro", "Julia", "José"],
                   'Faltas': [3, 4, 2, 1, 4],
                   'Nota Final': [80.0, 75.8, 50.1, 100.0, 60.5]})

print(dataFrame1)
print(" ")

print(dataFrame1.columns)
print(" ")

print(dataFrame1["Aluno"])
print(" ")

# Como ler um arquivo csv, e carregalo para m dataframe:

# df = pd.read_csv("NomeArquivo.csv") # NÂO APAGUE

# Fazento um matplot com o dataFrame1

df = pd.DataFrame(dataFrame1, columns=['Alunno', 'Faltas', 'Nota Final'])
print(df)
df.plot()
plt.show()

# Também é possivel utilizar diretamente o dataFrame1

dataFrame1.plot()
plt.show()