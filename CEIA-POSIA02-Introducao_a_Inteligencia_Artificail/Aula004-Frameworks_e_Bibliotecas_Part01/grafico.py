import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0.01, 5.0, 100)
s = np.exp(-t)

fig, ax = plt.subplots()

ax.plot(t, s)
ax.set_xlabel('Tempo')
ax.set_ylabel('Quantidade')
ax.set_title('Crescimento')
ax.grid(True)

plt.show()