import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(1000)

N_points = 100000
n_bins = 30

#Gerar as distribuicoes
dist = rng.standard_normal(N_points)

#Gerar o histograma
fig, ax = plt.subplots()

ax.hist(dist, bins=n_bins)
ax.set_xlabel("Numero de Ocorrencias")
ax.set_ylabel("Valores")
ax.set_title("Histograma")

plt.show()

