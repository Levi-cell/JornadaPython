# importa o mnist dataset
# Import necessary libraries
import matplotlib.pyplot as plt
import pickle
from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay

digits = datasets.load_digits()

_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))

for ax, image, label in zip(axes, digits.images, digits.target):
    ax.set_axis_off()
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')

    ax.set_title('Training: %i' % label)

plt.show()


"""
Classificação SVM

- Neste exemplo, definimos o valor da gama manualmente
- É possível encontrar aumtomaticamente bbons valores para o parâmetros usando ferramentas cmo grid search 
e cross validation

"""

# Flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

# Create a classifier: a support vector classifier
clf = svm.SVC(gamma=0.001)

# Split data into 50% train and 50% test subsets
X_train, X_test, y_train, y_test = train_test_split(
    data, digits.target, test_size=0.5, shuffle=False
)

# Learn the digits on the train subset
clf.fit(X_train, y_train)

# Predict the value of the digit on the test subset
predicted = clf.predict(X_test)

# Print classification report
print(f"Classification report for classifier {clf}: \n"
      f"{metrics.classification_report(y_test, predicted)}\n")

# Saving and loading the trained model
modelo_treinado = pickle.dumps(clf)
modelo_carregado = pickle.loads(modelo_treinado)

# Visualization of the first 4 test samples with predicted values
_, axes = plt.subplots(nrows=1, ncols=4, figsize=(10, 3))
for ax, image, prediction in zip(axes, X_test, predicted):
    ax.set_axis_off()
    image = image.reshape(8, 8)
    ax.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    ax.set_title(f'Prediction: {prediction}')
plt.show()

# Evaluating the model and displaying confusion matrix
disp = ConfusionMatrixDisplay.from_estimator(modelo_carregado, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")
plt.show()