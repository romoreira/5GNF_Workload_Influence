import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carregar o dataset e os rótulos
data = np.load('dataset/mixed.npy',  allow_pickle=True)
labels = np.load('dataset/mixed_labels.npy',  allow_pickle=True)

print("Original Data Shape: "+str(data.shape))
data = data.reshape(data.shape[0], -1)
print("Reshaped Data Shape: "+str(data.shape))
print("Labels Shape: "+str(labels.shape))


# Dividir o dataset em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

print(X_test)

# Inicializar o classificador KNN
knn = KNeighborsClassifier(n_neighbors=3)

# Treinar o classificador
knn.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred = knn.predict(X_test)

# Avaliar a precisão do classificador
accuracy = accuracy_score(y_test, y_pred)
print(f'Acurácia do KNN: {accuracy:.2f}')