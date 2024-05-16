import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 510

for i in range (0, 2, 1) :
    y[i*510 : i*510 + 77] = np.ones(77)
    y[i*510 + 101 : i*510+101 + 77] = np.ones(77)
    y[i*510 + 301 : i*510+301 + 77] = np.ones(77)

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(-0.5, 1.5)
plt.axis('off')
# plt.savefig("Demo_comparateur.pdf")
plt.show()