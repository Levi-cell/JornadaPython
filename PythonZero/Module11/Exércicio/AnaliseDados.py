# importa a biblioteca pandas
import pandas as pd
import numpy as np
# armazena os dados da tabela em uma estrutura tipo data frame
path = r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Exércicio\Projeto\1-dadosgovbr---2014.csv"
df = pd.read_csv(path,sep = ';', encoding="latin-1")
# visualizar alguns dados da tabela carregada
print(df.head())



# Questao 1)
print(df.value_counts()) #Conferindo as tabelas
print(df['Canal de Origem'].count()) # qtd de reclamações

#Questão 2)

print(df["Tempo Resposta"].mean()) # Tempo de resposta é 8
# outra forma
print(df["Tempo Resposta"].sum()/df["Tempo Resposta"].count()) # tempo resposta é 6.66

#Questao 3)

print(df['Nota do Consumidor'].mean())
print(df['Nota do Consumidor'].max())
print(df['Nota do Consumidor'].min())

#Questao 4)

# Tenho em mente duas formas de fazer isso....

# A primeira forma é criar um banco de dados, pode ser no Pycharm usando SQLite ou até no MySQL a forma de criar depende
# Pode ser diretamente pela interface gráfico de um banco de dados, assim gerando o script ou codar o script na própria
#ferramente ou fazer o script pelo próprio Pycharm, após isso podemos inserir os dados usando o Arquivo fornecdio com
# um Insert

#A segunda é forma é por meio de um gráfico usando o matplotlib aqui mesmo após ler o arquivo de dados, os eixos seriam a
# nota do consumidor e o tempo de resposta

#Questao 5)

print(df['Sexo'].value_counts()) # Interessante ele já separa quem é Homem e Mulher

# Questao 6)

print(df['UF'].value_counts())

# Questao 7)
print(df['Canal de Origem'].count())
print(df['Respondida'].value_counts())
totalReclam = df['Canal de Origem'].count()
porcentagemNaoRespondidas = 2026*100/totalReclam
print("De %s de todas as reclamações apenas %.2f%s não foram respondidas" % ("100.00%", porcentagemNaoRespondidas, "%"))
