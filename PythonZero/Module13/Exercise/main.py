from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt


"""EXERCICIO 1"""
digts = datasets.load_digits()

# Achatamento da imagem e transofrmando a matriz em vetor

n_sample = len(digts.images)
data = digts.images.reshape(n_sample, -1)

# classificador

clf = svm.SVC(gamma=0.001)

# dividindo a data em 80/20 treino e teste

X_train, X_test, y_train, y_test = train_test_split(data, digts.target, test_size=0.2, shuffle=False)

# Treinamento do modelo

clf.fit(X_train, y_train)

# prever o  valor do digito no teste

predicted = clf.predict(X_test)

# prever a taxa de porcentagem de acerto

print(f"Relatorio de classifcacao para o classificador {clf}:\n"
      f'{metrics.classification_report(y_test, predicted)}\n')

# Usando o random search para aprimorar o resultado do modelo


param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_sample_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

clf = RandomForestClassifier()
random_search = RandomizedSearchCV(clf, param_distributions=param_grid, n_iter=10)

random_search.fit(X_train, y_train)

print(random_search.best_params_)

# Usando o grid search para escolher os melhores parametros

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4]
}

clf = RandomForestClassifier()
grid_search = GridSearchCV(clf, param_grid=param_grid)

grid_search.fit(X_train, y_train)

print(grid_search.best_params_)

# Avaliando o modelo e calculando a matriz de confusãao

y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)

# Plotando a matriz de confusão usando seaborn
sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
plt.title('Matriz de Confusão')
plt.xlabel('Valor Previsto')
plt.ylabel('Valor Real')
plt.show()

# Usando Cross Validation

# Criando o classificador

clf = RandomForestClassifier()

# Definindo os dados de entrada X e os rótulos y

# Criando o objeto KFold para k = 5
kfold = KFold(n_splits=5)

# Realizando a validação cruzada

scores = cross_val_score(clf, X_train, y_train, cv=kfold)

# Imprimindo os resultados

print("Acurácia média:", scores.mean())
print("Desvio padrão:", scores.std())

"""EXERCICIO 2"""

# Calculando a acuracia

accuracy = accuracy_score(y_test, predicted)
print(f'Acurácia: {accuracy}')

"""RESPOSTAS :
"""


"EXERCICIO 3"
