from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import sklearn.metrics as metrics
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# carregando o dataset que está disponivel na biblioteca sklearn
dataset = load_breast_cancer()

# Veja tudo que temos na base de dados

print(dataset)
print(" ")

# agora vamos organizar a base de dados em um dataframe usando a biblioteca pandas.

df = pd.DataFrame(dataset.data, columns=[dataset.feature_names])

# add (adicionando) o target

df['diagnostico'] = dataset.target

print(df)
print(" ")

"""1) A partir do dataframe acima, que chamamos de df, identifique e divida as observações
e o target. As observações devem ser referenciadas como X e os targets como Y.
Por exemplo:

X = observacoes
Y = targets"""

X = df[dataset.feature_names]
Y = df['diagnostico']
print(X)
print(Y)

"""Agora divida X e Y em treino, teste e validação
"""

# 70% para treino

percentual_treino = 70
qtd_linhas = len(df)

qtd_treino = round((percentual_treino*qtd_linhas/100))
restante = round(qtd_linhas-qtd_treino)

Xtreino = X[:qtd_treino]
Ytreino = Y[:qtd_treino]

Xteste = X[qtd_treino:qtd_treino+round(restante/2)]
Yteste = Y[qtd_treino:qtd_treino+round(restante/2)]

Xval = X[qtd_treino+round(restante/2):]
Yval = Y[qtd_treino+round(restante/2):]

"""
3) A base de dados está pronta, então vamos utilizar agora o algoritmo SVM para treinar o modelo.
Para isso, observe o código a seguir e faça as devidas modificações. Em seguida observe a acurácia deste modelo.
"""

# Criando um modelo SVM variando os parâmetros C e gama
model = SVC(C=0.99, gamma=0.0000001)

# Treinando o modelo. Use aqui as suas observações de treino e os targets de treino

model.fit(Xtreino, Ytreino)

# Fazendo predições. Use aqui a sua base de teste

result = model.predict(Xteste)

# Mostrando os resultados preditos pelo modelo

print('Resultado:')
print(result)

print("Resultado esperado:")
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yteste)

# Agora vamos calcular a acurácia do modelo usando a base de testes
print("Acurácia:", metrics.accuracy_score(result, Yteste))

"""4)Agora vamos utilizar regressão logística no lugar do algoritimo SVM para treinar o modelo
"""

# Criando um modelo de regressão logística variando os parâmetros tol e max_iter
model = LogisticRegression(tol=0.99, max_iter=20)

# Treinando o modelo. Use aqui as suas observações de treino e os targets de treino

model.fit(Xtreino, Ytreino)

# Fazendo predições. Use aqui a sua base teste

result = model.predict(Xteste)

# Mostrando os resultados preditos pelo modelo
print('Resultado:')
print(result)

print('Resultado Esperado:')
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yteste)

# Agora vamos calcular a acurácia do modelo usando a base de testes

print("Acurácia:", metrics.accuracy_score(result, Yteste))

""" 5) Fazendo predições. Use aqui sua base de teste """
result = model.predict(Xval)

# Mostrando os resultados preditos pelo modelo
print("Resultado:")
print(result)

print("Resultado Esperado:")
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yval)

# agora vamos calcular a acurácia do modelo usando a base de testes
print("Acurácia:", metrics.accuracy_score(result, Yval))

"""6) Agora vamos utilizar o algoritimo KNN no lugar de regressão logística e SVM para treinar o modelo
 """
bestmodel = KNeighborsClassifier(n_neighbors=10, leaf_size=10)
acuracia = 0

for nn in [5, 20, 30, 40, 50]:
    for ls in [10, 50, 100, 200]:
        # Criando um modelo de regressão logística variando os parâmetros n_neighbors e leaf_size
        model = KNeighborsClassifier(n_neighbors=nn, leaf_size=ls)
        # Treinando o modelo. Use aqui observações de treino e os targets de treino
        model.fit(Xtreino, Ytreino)
        # Fazendo predições. Use aqui a sua base de teste
        result = model.predict(Xteste)
        # Mostrando os resultados preditos pelo modelo
        print('Resultado:')
        print(result)

        print('Resultado Esperado:')
        # Os resultados esperados são os targets de teste, mostre-os a seguir
        print('targets de teste aqui')

        # Agora vamos calcular a acurácia do modelo usando a base de testes

        if acuracia < metrics.accuracy_score(result, Yteste):
            bestmodel = model
            acuracia = metrics.accuracy_score(result, Yteste)
        print("Acurácia:", metrics.accuracy_score(result, Yteste))


result = bestmodel.predict(Xval)
print("Acurácia:", metrics.accuracy_score(result, Yval))

print(acuracia)