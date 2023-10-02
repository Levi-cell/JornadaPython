from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import sklearn.metrics as metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import numpy as np

# Carregando o dataset que está disponível na biblioteca sklearn
dataset = load_breast_cancer()

# Criando um DataFrame a partir dos dados do dataset
df = pd.DataFrame(dataset.data, columns=dataset.feature_names)

# Adicionando a coluna de diagnóstico (target)
df['diagnostico'] = dataset.target
print(df)

# Dividindo o DataFrame em observações (X) e targets (Y)
X = df.drop('diagnostico', axis=1)
Y = df['diagnostico']
print(X)
print(Y)

# Dividindo os dados em conjuntos de treino, teste e validação
percentual_treino = 70
qtd_linhas = len(df)
print(qtd_linhas)

qtd_treino = round((percentual_treino * qtd_linhas / 100))
print(qtd_treino)
restante = round(qtd_linhas - qtd_treino)
print(restante)

Xtreino = X[:qtd_treino]
Ytreino = Y[:qtd_treino]
print("TESTEEE")
print(Xtreino)
print("TESTEEE")
print(Ytreino)

Xteste = X[qtd_treino:qtd_treino + round(restante / 2)]
Yteste = Y[qtd_treino:qtd_treino + round(restante / 2)]
print("TESTEEE")
print(Yteste)
print("TESTEEE")
print(Xteste)

Xval = X[qtd_treino + round(restante / 2):]
Yval = Y[qtd_treino + round(restante / 2):]
print("TESTEEE")
print(Xval)
print("TESTEEE")
print(Yval)

# Criando um modelo SVM com parâmetros C e gama
model = SVC(C=0.99, gamma=0.0000001)
print(model)
# Treinando o modelo com os dados de treino
print(model.fit(Xtreino, Ytreino))

# Fazendo previsões com os dados de teste
result = model.predict(Xteste)

# Mostrando os resultados preditos pelo modelo
print('Resultado:')
print(result)

print("Resultado esperado:")
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yteste.values)

# Calculando a acurácia do modelo usando os dados de teste
accuracy = accuracy_score(result, Yteste)
print("Acurácia SVM:", accuracy)

# Regressão Logística
# Criando um modelo de regressão logística
model_logreg = LogisticRegression(tol=0.99, max_iter=20)
model_logreg.fit(Xtreino, Ytreino)
result_logreg = model_logreg.predict(Xteste)
print("Acurácia Regressão Logística:", metrics.accuracy_score(result_logreg, Yteste))

# KNN
best_model = None
best_accuracy = 0

for nn in [5, 20, 30, 40, 50]:
    for ls in [10, 50, 100, 200]:
        model_knn = KNeighborsClassifier(n_neighbors=nn, leaf_size=ls)
        model_knn.fit(Xtreino, Ytreino)
        result_knn = model_knn.predict(Xteste)

        accuracy = metrics.accuracy_score(result_knn, Yteste)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_model = model_knn

print("Melhor Acurácia KNN:", best_accuracy)

# Avaliar o melhor modelo KNN usando a base de validação
result_best_knn = best_model.predict(Xval)
print("Acurácia KNN (validação):", metrics.accuracy_score(result_best_knn, Yval))