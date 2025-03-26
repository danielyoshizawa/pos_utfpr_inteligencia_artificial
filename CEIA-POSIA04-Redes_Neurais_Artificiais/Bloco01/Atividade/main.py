from sklearn import preprocessing # biblioteca para suporte a pré-processamento de dados
from sklearn.model_selection import train_test_split # biblioteca para separação de amostras para treino e teste
from sklearn.linear_model import Perceptron # biblioteca coom funções para a execução da RNA Perceptron
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import metrics # biblioteca para obtençãa de metricas para avaliação dos modelos
import matplotlib.pyplot as plt # biblioteca parra plotar gráficos
import numpy as np
import pandas as pd

# Carregando o dataset
df = pd.read_csv("bancario.csv")
# print(df)

# Extraindo os valores de classificação entre bom e mau
y = df['Classe'].values
# print(y)

# Convertendo os valores de classificação de text para númericos, utilizando -1 para bom e 1 para mau
# Função Degrau Bipolar (Sinal)
y = np.where(y == 'bom', -1, 1)
# print(y)

# Extraindo colunas de dados para treinamento da RNA
X = df.iloc[:, [1,2]].values
# print(X)

# Verificando se o volume de dados é equivalente
print(y.shape)
print(X.shape)

# Instanciando um Scaler para normalizar os dados
scaler = preprocessing.MinMaxScaler()

# Normalizando os dados
X = scaler.fit_transform(X)

# Plotando o grafico para verificar se as amostras são linearmente separaveis
# plt.scatter(X[:,0], X[:,1], c=y)
# plt.title("Bom X Mau")
# plt.xlabel("Renda")
# plt.ylabel("Divida")
# plt.show()

# Separando os dados emm amostras de treino e testes, considerando 30% dos valores para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=12)

# Verificando o volume de dados de treino e teste
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Instanciando o modelo Perceptron
p = Perceptron(random_state=42, eta0=0.001, alpha=0.1)

# Treinando o modelo
p.fit(X_train, y_train)

predictions_train = p.predict(X_train) # Validação do conjunto de amostras treinadas
train_score = accuracy_score(predictions_train, y_train) # Validação de acurácia da classificação das amostras que foram apresentaadas no treinaamento
print("Acurácia com dados de treinamento: ", train_score) # O resultado esperado é 100%

print(classification_report(predictions_train, y_train))

predictions_test = p.predict(X_test) # Validação do conjunto de amostras de teste
test_score = accuracy_score(predictions_test, y_test) # Avaliação da acurácia da classificação das amostras que foram apresentadas no teste
print("Acurácia com dados de teste: ", test_score) # O resultado esperado é 100%

print(classification_report(predictions_test, y_test))

print("Numero de epocas de treinamento: ", p.n_iter_)
print("Lista de parametroos configurados na Perceptron: ", p.get_params())

# Apresentação gráfica da matriz de confusão dos testes classificados
# conf_matrix = confusion_matrix(y_test, predictions_test)
# cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=["Bom", "Mau"])
# cm_display.plot()
# plt.show()

# Normalizando os dados de teste
test_data = [[2000, 1800], [1500, 80], [450, 580],[580, 450],[5123, 1200],[1233, 1223]]
expected = [1, -1, 1, 1, -1, 1]

# Normalizando os dados de teste
test_data = scaler.transform(test_data)

print(test_data)

# Realizando o teste com os dados de teste
predictions = p.predict(test_data)
print(predictions)

# Calculando a acurácia do modelo
accuracy = accuracy_score(expected, predictions)
print(f"Acurácia do modelo: {accuracy:.2f}")