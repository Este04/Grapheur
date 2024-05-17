import numpy as np
import matplotlib . pyplot as plt
from Utilisé import signal_integrateur

y = [*np.zeros(101), *np.ones(1000-101)]
integrateur = signal_integrateur.y

y = np.array([*y[:101], *integrateur[101:101+20], *np.ones(1000-101-20)*integrateur[120]])
np.put(y, range(500+101,500+101+20), integrateur[500+101:500+101+20])


def plot(y, save=False):
    x = np.linspace(0, 10, 1000)
    plt.plot(x, y)
    plt.axis('off')
    plt.ylim(-0.2, 1.2)
    if save: plt.savefig("Demo_signal_SH.pdf")
    plt.show()

# plot(y)
