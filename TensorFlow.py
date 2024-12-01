import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import itertools

# Carregar dados
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Pré-processamento dos dados
train_images = train_images / 255.0
test_images = test_images / 255.0

# Função para criar o modelo com parâmetros configuráveis
def create_model(activation, optimizer, loss):
    model = keras.Sequential([
        layers.Flatten(input_shape=(28, 28)),
        layers.Dense(128, activation='relu'),
        layers.Dense(10, activation=activation)  # última camada
    ])
    model.compile(optimizer=optimizer,
                  loss=loss,
                  metrics=['accuracy'])
    return model

# Parâmetros a serem testados
ativacoes = ['softmax', 'sigmoid', 'softplus', 'softsign', 'linear', 'tanh']
otimizadores = ['adam', 'adadelta', 'adagrad', 'adamax', 'rmsprop', 'ftrl']
perdas = ['sparse_categorical_crossentropy', 'kl_divergence', 'poisson']

# Avaliação das combinações
resultados = []

for ativacao, otimizador, perda in itertools.product(ativacoes, otimizadores, perdas):
    print(f"\nTestando configuração: Ativação={ativacao}, Otimizador={otimizador}, Perda={perda}")
    try:
        modelo = create_model(ativacao, otimizador, perda)
        historico = modelo.fit(train_images, train_labels, epochs=5, batch_size=32, verbose=0)
        perda_teste, acuracia_teste = modelo.evaluate(test_images, test_labels, verbose=0)
        resultados.append({
            'Ativação': ativacao,
            'Otimizador': otimizador,
            'Perda': perda,
            'Acurácia': acuracia_teste
        })
    except tf.errors.ResourceExhaustedError as e:
        print(f"⚠️ Aviso de memória insuficiente para a configuração.")
    except Exception as e:
        print(f"❌ Erro na configuração Ativação={ativacao}, Otimizador={otimizador}, Perda={perda}: {e}")

# Ordenar os resultados pela melhor acurácia
resultados_ordenados = sorted(resultados, key=lambda x: x['Acurácia'], reverse=True)

# Exibir os melhores resultados
print("\nAs melhores configurações encontradas foram:")
for resultado in resultados_ordenados[:10]:  # Mostra as 10 melhores
    print(f"Ativação: {resultado['Ativação']}, Otimizador: {resultado['Otimizador']}, "
          f"Perda: {resultado['Perda']} -> Acurácia: {resultado['Acurácia']:.4f}")

# Exibir resumo de todos os resultados de forma estruturada
print("\nResumo completo dos resultados:")
for resultado in resultados_ordenados:
    print(f"Ativação: {resultado['Ativação']}, Otimizador: {resultado['Otimizador']}, "
          f"Perda: {resultado['Perda']} -> Acurácia: {resultado['Acurácia']:.4f}")
