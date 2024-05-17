import numpy as np
import matplotlib.pyplot as plt

y = np.zeros(1000)
T = 510

bruit = np.random.normal(0, 0.01, 1000)

for i in range(0, 2, 1):
    y[i * 510: i * 510 + 77] = np.ones(77)
    y[i * 510 + 101: i * 510 + 101 + 77] = np.ones(77) * 2 / 3
    y[i * 510 + 301: i * 510 + 301 + 77] = np.ones(77) * 2 / 5


def plot(y, bruit, save=False):
    x = np.linspace(0, 10, 1001)
    plt.plot(x, [0, *(y + bruit)])
    plt.ylim(-0.5, 1.5)
    plt.axis('off')
    if save: plt.savefig("Demo_signal_crete.pdf")
    plt.show()

# plot(y, bruit)
