import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error, r2_score

df = pd.read_csv("ressonanciaMLP.csv")

# Informações gerais sobre o dataframe
print(df.head())
print(df.info())
print(df.describe())
# Todos os dados estão normalizados, sem nulos e no formato correto

# Pré processamento de dados
X_train = df.drop(columns=["d"])
y_train = df["d"]

# Função geradora de parâmetros para o MLPRegressor
def setup_generator(activation : list, neurons_per_layer : list, learning_rate : int, max_epochs : int):
    for act in activation:
        for neurons in neurons_per_layer:
            yield {"activation": act, "neurons": neurons, "learning_rate": learning_rate, "max_epochs": max_epochs}

setup = setup_generator(
    ["tanh", "relu", "logistic"], 
    [5, 10, 15], 
    0.01, 
    1000
)

results = []

for stp in setup:
    # Aplicação do MLPRegressor
    mlp_reg = MLPRegressor(
        activation=stp["activation"], 
        hidden_layer_sizes=(stp["neurons"]), 
        max_iter=stp["max_epochs"], 
        learning_rate_init=stp["learning_rate"], 
        random_state=42
    )

    mlp_reg.fit(X_train, y_train)
    
    num_epochs = mlp_reg.n_iter_
    final_loss = mlp_reg.loss_
    
    results.append({
        'Neuronios': stp["neurons"],
        "Função de Ativação": stp["activation"],
        "Numero de Épocas": num_epochs,
        "Perda Final": final_loss
    })

# Classificando os resultados
# Adicionando indices para melhor visualização
results = [{"Posição Original": i + 1, **result} for i, result in enumerate(results)]

# Ordenar por perda final (menor perda é melhor)
results = sorted(results, key=lambda x: x['Perda Final'])
# Ranking
results = [{"Ranking da Melhor Configuração": i + 1, **result, } for i, result in enumerate(results)]

print(tabulate(results, headers="keys", tablefmt="grid"))

# Treinando apenas o melhor modelo
mlp_reg = MLPRegressor(
    activation=results[0]["Função de Ativação"],
    hidden_layer_sizes=results[0]["Neuronios"],
    max_iter=1000,
    learning_rate_init=0.01,
    random_state=42
)

mlp_reg.fit(X_train, y_train)

plt.plot(mlp_reg.loss_curve_) # Plotando o gráfico de erros no processo de treinamento
plt.title("Curva de Perda no Treinamento", fontsize=14)
plt.xlabel('Épocas')
plt.ylabel('Custo')
plt.show()

# Carregando dados de teste
df = pd.read_csv("ressonanciaMLPTest.csv")
# Separando os dados de teste em X e y
X_test = df.drop(columns=["d"])
y_test = df["d"]

# Predição
y_pred = mlp_reg.predict(X_test)

# Gráfico de comparação entre os valores desejados e os estimados
df_temp = pd.DataFrame({'Desejado': y_test, 'Estimado': y_pred}) # Criação de um dataframe com os dados desejados e os estimados na predição
df_temp = df_temp.head(40) # Armazena a quantidade de elementos a serem apresentados no gráfico, pois pode ser visualmente difícil de abstrair caso tenham muitas informações
df_temp.plot(kind='bar',figsize=(10,6)) # Configuração do tipo de gráfico 'bar' e tamanho da figura
plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray') # Configuração do grid do gráfico
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='blue') # Configuração do grid do gráfico
plt.show() # Apresenta o gráfico comparando o desejado e o estimado pelo modelo neural

print('Mean Absolute Error (MAE):', mean_absolute_error(y_test, y_pred)) # Variação de 0 ao infinito. Quanto menor, melhor.
print('Mean Squared Error (MSE):', mean_squared_error(y_test, y_pred)) # Variação de 0 ao infinito. Quanto menor, melhor.
print('Root Mean Squared Error (RMSE):', np.sqrt(mean_squared_error(y_test, y_pred))) # Variação de 0 ao infinito. Quanto menor, melhor.
print('Mean Absolute Percentage Error (MAPE):', mean_absolute_percentage_error(y_test, y_pred)) # Apresenta em porcentagem de erros em relação ao desejado.
print('R2: ', r2_score(y_test, y_pred)) # Apresenta o R2 Score - Representa quanto o modelo está prevendo corretamente, tem uma variação de 0 a 1. Caso seja obtido pelo modelo o R2 = 1, pode ser afirmado que os dados tem relação linear de 100%.