import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import openpyxl as xl
from collections import Counter

df = pd.read_excel(r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Slides\DADOS ALUNOS.xlsx")
print(df)

# a) quantos alunos tiraram nota acima da média da classe

media = np.mean(df['Nota Prova 1'])+np.mean(df['Nota Prova 2'])+np.mean(df['Nota Prova 3'])+np.mean(df['Nota Seminario'])

maiorMedidaDF=df[(df['Nota Prova 1'])+np.mean(df['Nota Prova 2'])+np.mean(df['Nota Prova 3'])+np.mean(df['Nota Seminario'])>media]

print("Quantidade de alunos que tiraram nota acima de média da classe:", maiorMedidaDF['Aluno(a)'].count())
print(" ")

# b)

p = df[df['Participativo nas aulas'] == 'S']

x = np.mean(p['Nota Prova 1'])+np.mean(p['Nota Prova 2'])+np.mean(p['Nota Prova 3'])+np.mean(p['Nota Seminario'])

print("Média dos alunos que participam das aulas:", x)
print(" ")

# c)

b = df[df['Participativo nas aulas'] == 'N']

y = np.mean(b['Nota Prova 1'])+np.mean(b['Nota Prova 2'])+np.mean(b['Nota Prova 3'])+np.mean(b['Nota Seminario'])
print("Média dos alunos que  não participam das aulas:", y)
print(" ")

# d)
x = df[df['Uso de celular durante as aulas'] == 'Pouco']

y = np.mean(x['Nota Prova 1'])+np.mean(x['Nota Prova 2'])+np.mean(x['Nota Prova 3'])+np.mean(x['Nota Seminario'])
print(" A Média dos alunos que usam pouco o celular é:", y)
print(" ")
# e)

x = df[df['Uso de celular durante as aulas'] == 'Muito']

y = np.mean(x['Nota Prova 1'])+np.mean(x['Nota Prova 2'])+np.mean(x['Nota Prova 3'])+np.mean(x['Nota Seminario'])
print(" A Média dos alunos que usam muito o celular é:", y)
print(" ")

# f)

y = df[(df['Horas estudo por semana']) > 5]

print(y['Aluno(a)'].count(), "Alunos estudam 5 horas por semana")
x = np.mean(y['Nota Prova 1'])+np.mean(y['Nota Prova 2'])+np.mean(y['Nota Prova 3'])+np.mean(y['Nota Seminario'])
print(" A média de nota dos alunos que estudam 5 horas por semana é:", x)
print(" ")

# g)

print("A média de faltas é: %.2f" % np.mean(df['Faltas']))

# EXTRA:

# df.corr()
#
# print(df.dtypes)
# 
# df['Participativo nas aulas']=df['Participativo nas aulas'].astype('category').cat.codes
#
# df['Uso de celular durante as aulas']=df['Uso de celular durante as aulas'].astype('category').cat.codes
#
# df['Sexo'] = df['Sexo'].astype('category').cat.codes
#
# print(df.corr())

