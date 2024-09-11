import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'aula4-matriz.csv'
data = pd.read_csv(file_path)

# 1º Passo: Cálculo da Média e Desvio Padrão para cada Coluna
medias = data.mean()
desvios_padrao = data.std()

# 2º Passo: Meancenter - Subtrair a média de cada valor na coluna
meancentered_data = data - medias

# 3º Passo: Autoscale - Dividir pelo desvio padrão de cada coluna
autoscaled_data = meancentered_data / desvios_padrao

# Plotar os gráficos
plt.figure(figsize=(18, 6))

# Gráfico dos dados originais
plt.subplot(1, 3, 1)
plt.plot(data)
plt.title("Dados Originais")
plt.xlabel("Índice")
plt.ylabel("Valores")

# Gráfico do meancenter
plt.subplot(1, 3, 2)
plt.plot(meancentered_data)
plt.title("Meancenter")
plt.xlabel("Índice")
plt.ylabel("Valores")

# Gráfico do autoscale
plt.subplot(1, 3, 3)
plt.plot(autoscaled_data)
plt.title("Autoscale")
plt.xlabel("Índice")
plt.ylabel("Valores")

plt.tight_layout()
plt.show()
