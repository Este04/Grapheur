import numpy as np
import matplotlib . pyplot as plt

y = [*np.zeros(101), *np.ones(1000-101)]
print(len(y))
integrateur = np.linspace(0, 1, int(500*5/6))

y = [*y[:101], *integrateur[101:101+20], *np.ones(1000-101-20)*integrateur[120]]


def plot(y, save=False):
    x = np.linspace(0, 10, 1000)
    plt.plot(x, y)
    plt.axis('off')
    plt.ylim(-0.2, 1.2)
    if save: plt.savefig("Demo_signal_SH.pdf")
    plt.show()

# plot(y)