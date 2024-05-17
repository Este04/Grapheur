import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)

for i in range (0, 2, 1) :
    y[i * 500 + 142: int(i*500 + 5/6*500)] = np.ones(274)

def plot(y, save=False):
    x = np.linspace(0, 10, 1001)
    plt.plot(x, [0, *y])
    plt.ylim(0, 2)
    plt.axis('off')
    if save: plt.savefig("Demo_signal_bascule.pdf")
    plt.show()

# plot(y,0)