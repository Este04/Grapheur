import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 510

for i in range (0, 2, 1) :
    y[i*510 + 301 : i*510+301 + 77] = np.ones(77)

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(0, 2)
plt.axis('off')
# plt.savefig("P2_signalinterrupteurB.pdf")
plt.show()