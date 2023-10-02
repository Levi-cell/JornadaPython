import matplotlib.pyplot as plt
import pandas as pd

path = r"C:\Users\levig\Desktop\Programação\Mentorama\Python\PythonZero\Module11\Exércicio\Projeto\1-dadosgovbr---2014.csv"
df = pd.read_csv(path, sep=';', encoding="latin-1")
# dt = df.DataFrame(path, columns = [])

plt.style.use('Solarize_Light2')

plt.rcParams['figure.figsize'] = (11, 7)

# Questao 1

# usando a pizza
print(df['Sexo'].value_counts())
plt.title('Frequência de reclamações por sexo usando pizza')
plt.xlabel('Sexo')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações por sexo usando pizza', transparent=True)
plt.pie(df['Sexo'].value_counts(), colors=['blue', 'red'], labels=['Homens', 'Mulheres'])
plt.show()
# usando as barras
plt.title('Frequência de reclamações por sexo usando barras')
plt.xlabel('Sexo')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações por sexo usando barras', transparent=True)
plt.bar(df['Sexo'].value_counts().index, df['Sexo'].value_counts().values)
plt.show()

# usando gráfico
# listaMasculino = []
# listaFeminino = []
# for x in df['Sexo']:
#     if x == "M":
#         listaMasculino.append(x)
#     else:
#         listaFeminino.append(x)
# data = {
#     'Sexo Masculino': listaMasculino,
#     'Sexo Feminino':listaFeminino
# }
# novo = pd.DataFrame(data, columns=['Sexo Masculino', 'Sexo Feminino'])
# plt.title('Frequência de reclamações por sexo usando barras')
# plt.xlabel('Quantidade de reclamações por sexo')
# plt.ylabel('Quantidade de reclamações')
# plt.savefig('Reclamações por sexo usando gráfico', transparent=True)
# novo.plot()
# plt.show()

# Questao 2

# usando a pizza
print(df['UF'].value_counts())
plt.title('Frequência de reclamações por Estado usando pizza')
plt.xlabel('Estado')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações por Estado usando pizza', transparent=True)
plt.pie(df['UF'].value_counts())
plt.show()
# usando as barras
plt.title('Frequência de reclamações por Estado usando barras')
plt.xlabel('Estado')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações por Estado usando barras', transparent=True)
plt.bar(df['UF'].value_counts().index, df['UF'].value_counts().values)
plt.show()


# Questao 3

# usando a pizza
print(df['Respondida'].value_counts())
plt.title('Frequência de reclamações Respondidas usando pizza')
plt.xlabel('Respondia ou Não')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações respondias usando pizza', transparent=True)
plt.pie(df['Respondida'].value_counts(), colors=['blue', 'red'], labels=['Sim', 'Não Respondida'])
plt.show()
# usando as barras
plt.title('Frequência de reclamações Respondidas usando barras')
plt.xlabel('Respondida ou não')
plt.ylabel('Quantidade de reclamações')
plt.savefig('Reclamações Respondidas usando barras', transparent=True)
plt.bar(df['Respondida'].value_counts().index, df['Respondida'].value_counts().values)
plt.show()
















