import numpy as np
import matplotlib.pyplot as plt

y = np.zeros(1000)

for i in range(0, 2, 1):
    y[i * 500 + int(500 * 5 / 6):(i + 1) * 500] = np.ones(int(500 * 1 / 6) + 1)
y[-1] = 0


def plot(y, save=False):
    x = np.linspace(0, 10, 1001)
    plt.plot(x, [*y, 0])
    plt.ylim(0, 2)
    plt.axis('off')
    if save: plt.savefig("Demo_signalmonostable_A.pdf")
    plt.show()


# plot(y,0)