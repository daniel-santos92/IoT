import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = 'aula4-matriz.csv'
data = pd.read_csv(file_path)

# Centrar pela média (meancenter)
meancentered_data = data - data.mean()

# Autoescalar as colunas (autoscale)
autoscaled_data = meancentered_data / meancentered_data.std()

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
