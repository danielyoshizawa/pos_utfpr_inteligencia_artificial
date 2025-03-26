import tensorflow as tf
import matplotlib.pyplot as plt

# Data set mnist - 60 mil figuras de 28x28 pixels
mnist = tf.keras.datasets.mnist

# Carrega os dados de treinamento e teste
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normaliza os dados para o intervalo 0-1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Criar rede neural sequencial (Modelo da rede neural que será usada no tensorflow)
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)), # Entrada tem que ser transformada de figuras 28x28 em um vetor.
    tf.keras.layers.Dense(32, activation=tf.nn.relu), # Camada oculta com N=64 neurônios e função de ativação ReLU. (Retificador linear unitario)
    tf.keras.layers.Dropout(0.1), # Dropout para evitar overfitting (Camada ocultta tem X% dos neurônios ativados aleatoriamente)
    tf.keras.layers.Dense(10, activation=tf.nn.softmax) # Camada de saída com 10 neurônios (0-9) e função de ativação softmax.
])

# Definir algoritimo de treinamento, função de perda e a metrica de treinamento
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Treinar o modelo (Necessario gravar o historico do treinamento para utilizar no grafico)
history = model.fit(x_train, y_train, epochs=200)

# Avaliar o modelo (Avaliando a acuracia do modelo)
model.evaluate(x_test, y_test, verbose=2)

# Plotar o grafico da acuracia do modelo
plt.plot(history.history['accuracy'], label='Acurácia do modelo')
plt.title('Acurácia do modelo')
plt.xlabel('Época')
plt.ylabel('Acurácia')
plt.legend(["Treinamento"],loc='upper left')
plt.show()

# Plotar o grafico da perda do modelo
plt.plot(history.history['loss'], label='Perda do modelo')
plt.title('Perda do modelo')
plt.xlabel('Época')
plt.ylabel('Perda')
plt.legend(["Treinamento"],loc='upper left')
plt.show()