import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 500

for i in range(2) :
    y[int(i*T) : int(i*T + T * 5/6)] = np.linspace(0, 1, int(T * 5 / 6))
    y[int(i*T + 1*T*5/6) : int(i*T + 1*T)] = np.zeros(int(T / 6) + 1)

def plot(y, save=False):
    x = np.linspace(0, 10, 1001)
    plt.plot(x, np.array([*y, 0]))
    plt.axis('off')
    if save: plt.savefig("Demo_integrateur.pdf")
    plt.show()

# plot(y)