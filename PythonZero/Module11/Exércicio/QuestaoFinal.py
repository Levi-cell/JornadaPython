import pandas as pd
import matplotlib.pyplot as plt

path = r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Exércicio\Projeto\1-dadosgovbr---2014.csv"
df = pd.read_csv(path, sep=';', encoding="latin-1")

plt.style.use('Solarize_Light2')

plt.rcParams['figure.figsize'] = (11, 7)

a = df['Nota do Consumidor'].isnull().sum()
b = df[df['Nota do Consumidor'] == 1].shape[0]
c = df[df['Nota do Consumidor'] == 2].shape[0]
d = df[df['Nota do Consumidor'] == 3].shape[0]
e = df[df['Nota do Consumidor'] == 4].shape[0]
f = df[df['Nota do Consumidor'] == 5].shape[0]

print(f' Nota 1: {b} \n Nota 2: {c} \n Nota 3: {d} \n Nota 4: {e} \n Nota 5: {f} \n Nao Avaliada: {a}')


# Criar listas com as categorias e os valores correspondentes
categorias = ['Nota 1', 'Nota 2', 'Nota 3', 'Nota 4', 'Nota 5', 'Nao Avaliada']
valores = [b,c,d,e,f,a ]

# Criar o gráfico de barras
plt.bar(categorias, valores)

# Adicionar rótulos e título ao gráfico
plt.xlabel('Nota')
plt.ylabel('Frequência de Reclamações')
plt.title('Notas Reclamações')

# Exibir o gráfico
plt.show()

''' O grafico abaixo mostra a relacao de notas e reclamacoes nao respondidas'''

setor_counts = df['Segmento de Mercado'].value_counts()

# Criar o gráfico de barras
plt.bar(setor_counts.index, setor_counts.values)

# Adicionar rótulos e título ao gráfico
plt.xlabel('Segmento de Mercado')
plt.ylabel('Contagem')
plt.title('Contagem de reclamações por Setor')

# Rotacionar rótulos do eixo x para melhor visualização
plt.xticks(rotation=90)

# Exibir o gráfico
plt.show()

"""O grafico acima mostra o numero de reclamacoes por setor da industria"""