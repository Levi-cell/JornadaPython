from sklearn.datasets import load_boston
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
import numpy as np


housingPrices = load_boston()
print(housingPrices)

# Agora vamos organizar a base de dados em um dataframe usando a biblioteca pandas.

"""Organizando os dados em um dataframe: No dataframe temos os dados de cada tumor
 e também o target de cada um deles. Preste atenção na quantidade de observação que
  a base possui bem como todos os atributos"""

df = pd.DataFrame(housingPrices.data, columns=[housingPrices.feature_names])
#add o target
df['valor']=housingPrices.target
print(df)

"""
1) A partir do dataframe acima, que chamamos de df,
identifique e divida as observações e o target. As observações devem ser
 referenciadas como X e os targets como Y. Por exemplo:

X = observações

Y = targets"""

X = df[housingPrices.feature_names]
Y = df['valor']
""" 2) Agora, divida X e Y em treino, teste e validação
"""
# divide em treino e teste sendo 30%para teste

Xtreino, Xteste, Ytreino, Yteste = train_test_split(X,Y,
    test_size=0.3, shuffle = True, random_state = 8)

# pega a base de teste e divide em teste e validação
Xteste, Xval, Yteste, Yval = train_test_split(Xteste, Yteste,
    test_size=0.5, random_state= 8)

"""Vamos utilizar um algorítmo de regressão linear para criar o modelo:
"""

# Criando um modelo de regressão linear variando os parâmetros tol e max_iter
model=LinearRegression(n_jobs=100)

# Treinando o modelo. Use aqui suas observações de treino e os targets de treino
model.fit(Xtreino, Ytreino)

# Fazendo predições. Use aqui sua base de teste
result = model.predict(Xteste)

# mostrando os resultados preditos pelo modelo
print('Resultado:')
print(result)

print('Resultado Esperado:')
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yteste)


# agora vamos calcular o erro do modelo usando a base de testes
print("Erro:", metrics.mean_squared_error(result,Yteste))

# Fazendo predições. Use aqui sua base de teste
result = model.predict(Xval)

# mostrando os resultados preditos pelo modelo
print('Resultado:')
print(result)

print('Resultado Esperado:')
# Os resultados esperados são os targets de teste, mostre-os a seguir
print(Yval)


# agora vamos calcular o erro do modelo usando a base de testes
print("Erro:", metrics.mean_squared_error(result,Yval))

"""visualizar o resultado
"""

plt.figure(figsize=(12,10))
plt.scatter(Yval,result,color='Red',marker='*')

regline = lambda S : 0.7466*Yval + 6.0860359
S = np.array([Yval.min(),Yval.max()])
plt.plot(Yval, regline(S),lw=2.5, c="BLUE")

plt.xlabel("Prices", {'size':20})
plt.ylabel("Predictions", {'size':20})
plt.title("Predicted Prices vs Prices,{'size':20}")