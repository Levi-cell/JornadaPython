import pandas as pd
import openpyxl

# Iniciando e imprimindo uma série
print("iniciando e imprimindo uma série:")

s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd'])
print(s)
print(" ")

# Recuperar um elemento através do seu indexador
print("Recuperar um elemento através do seu indexador: ")
print(s['b'])
print(" ")

# iniciando um DataFrame
print("Iniciando um DataFrame: ")
data = {
    'País': ['Bélgica', 'Índia', 'Brasil'],
    'Capital': ['Bruxelas', 'Nova Delhi', 'Brasília'],
    'População': [123465, 456789, 987654]
}
df = pd.DataFrame(data, columns= ['País', 'Capital', 'População'])

# Buscando ajuda
help(pd.Series)

print(df)
# ver o começo do conteúdo de um DataFrame
print(" ")
print("ver o começo do conteúdo de um DataFrame:")
print(df.head())
print(" ")

# recuperar um subconjunto de um DataFrame
print("recuperar um subconjunto de um DataFrame:")
print(df[1:])
print(" ")

# recuperar um unico valor pela linha e coluna
print("Recuperar um unico valor pela linha e coluna:")
print(df.loc[[0], ['País']])
print(" ")

#removendo linhas e colunas

#podemos remover linhas pelo index
print("podemos remover linhas pelo index:")
print(s.drop('a'))
print(" ")

#podemos remover colunas usando o argumento axis = 1
print("podemos remover colunas usando o argumento axis = 1:")
print(df.drop('País', axis=1))
print(" ")

#Lendo um arquivo cvs e definindo o iso que é uma convenção de escrita que nos permite trabalhar com
print("Arquivo CSV")

path = r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Modulo 11 - Analise e Visualização de Dados\meu_arquivo.csv"
dd = pd.read_csv(path, encoding='ISO-8859-1')
print(dd)
print(" ")

print(" Escrevendo e salvando um arquivo do tipo csv:")
dd.to_csv()
print(dd.to_csv())

##ledo arquivo Excel
print("Excel:")
path = r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Modulo 11 - Analise e Visualização de Dados\meu_arquivo_excel.xlsx"
xlsx = pd.ExcelFile(path)
dfs = pd.read_excel(xlsx, sheet_name='Planilha1')
print(dfs)
print(" ")

# Coletando informações sobre o DataFrame

print("Quantidade de linhas e colunas do DataFram:")
print(df.shape)
print(" ")

print("Descrição do index:")
print(df.index)
print(" ")

print("Colunas presentes no DataFrame:")
print(df.columns)
print(" ")

print("Contagem de dados não-nulos:")
print(df.count())
print(" ")

print("Criando uma nova coluna em um DataFrame:")
df['Nova Coluna'] = 0
print(df)
print(" ")


print("Renomenado colunas de um data frame:")
df.columns = ['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4']
print(df)
print(" ")

df.rename({'País': 'Coluna 1', 'Capital': 'Coluna 2', 'População': 'Coluna 3', 'Nova Coluna': 'Coluna 4'}, axis='columns')
print(df)
print(" ")

# Operações com data frames
print("Mais operações sobre os DataFrames:")
print(" ")

# Soma
print(" Soma dos valores de um DataFrame:")
print(df.sum())
print(" ")

# Menor valor de um DataFrame
print("Menor valor de um DataFrame:")
print(df.min())
print(" ")

# Maior valor
print("Maior valor:")
print(df.max())
print(" ")

# Index do menor valor
print("Index do menor valor:")
print(df['Coluna 3'].idxmin())
print(" ")

# Index do maior valor
print("Index do maior valor:")
print(df['Coluna 3'].idxmax())
print(" ")

# Resumo estatístico do DataFrame, com quartis, mediana, etc
print("Resumo estatístico do DataFrame, com quartis, mediana, etc:")
print(df.describe())
print(" ")

# Média dos valores
print("Média dos valores:")
print(df['Coluna 3'].mean())
print(" ")

# Mediana dos valores
print("Mediana dos valores:")
print(df['Coluna 3'].median())
print(" ")

# ORDENANDO VALORES
print("ORDENANDO VALORES:")

data = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David', 'Emily'],
    'Nota': [85, 92, 78, 65, 95]
}

print("ORDENANDO DE FORMA DESCRESCENTE:")


df = pd.DataFrame(data)

# Ordenar o DataFrame com base na coluna 'Nota'
df = df.sort_values(by='Nota', ascending=False)

print(df)
print("  ")

print("ORDENANDO EM ORDEM CRESCENTE")

df = pd.DataFrame(data)

# Ordenar o DataFrame com base na coluna 'Nota'
df = df.sort_values(by='Nota', ascending=True)

print(df)
print("  ")
