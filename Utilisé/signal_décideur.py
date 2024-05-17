import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 500

for i in range (0, 2, 1) :
    y[i*T + 85 : int(i*T + 5/6*T)] = np.ones(int(5/6*T) - 85)

def plot(y, save=False):
    x = np.linspace(0, 10, 1001)
    plt.plot(x, [0, *y])
    plt.ylim(0, 2)
    plt.axis('off')
    if save: plt.savefig("Demo_décideur.pdf")
    plt.show()

# plot(y)