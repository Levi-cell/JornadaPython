import matplotlib.pyplot as plt
import pandas as pd

# criando e imprimindo um dataframe

data = {
    'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'y': [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
}

df = pd.DataFrame(data, columns=['x', 'y'])
print(df)
# para plotar todas as colunas  ou variaveis numéricas do dataframe
df.plot()
plt.title('Seu título legal') #adicionando o título
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')
plt.show()

# selecionando um tipo de gráfico
# gráfico de barras

# Perceba que pra cada tipo de gráfico você pdoe personalizar
plt.bar(df['x'], df['y'])
plt.title('Seu título legal')
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')
plt.show()

# nem todos os gráficos cabem para todos os tipos de dados
plt.pie(df['x'], df['y'])
plt.title('Seu título legal')
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')
plt.show()

plt.scatter(df['x'], df['y'])
plt.title('Seu título legal')
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')
plt.show()

# Criando uma legenda e definindo a cor das barras com valor hexadecimal
plt.bar(df['x'], df['y'], color='crimson', label='Minha Lengenda')
plt.legend()
plt.show()

# Mudando a localização de uma legenda
plt.bar(df['x'], df['y'], color='crimson', label='Minha Lengenda')
plt.legend(loc='best')
plt.show()

# Mudando a localização de uma legenda
plt.bar(df['x'], df['y'], color='crimson', label='Minha Lengenda')
plt.legend(loc=6)
plt.show()

# Colocando dois gráficos em um só
plt.plot(df['x'], df['y'], color='green')
plt.scatter(df['x'], df['y'], color='red')
plt.show()

# Mudando linhas e marcadores

plt.plot(df['x'], df['y'], 'b--')
plt.scatter(df['x'], df['y'], marker="o", color='red')
plt.show()

# Criando uma anotação no gráfico

fig, ax = plt.subplots()
ax.bar(df['x'], df['y'])
ax.annotate("Maior valor",
            xy=(10, 12),
            xycoords='data',
            xytext=(11,10),
            textcoords='data',
            arrowprops= dict(arrowstyle="->", connectionstyle="arc3"))

plt.show()