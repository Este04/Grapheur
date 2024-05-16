import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 500

for i in range (0, 2, 1) :
    y[i*T + 201 : int(i*T + 5/6*T)] = np.ones(int(5/6*T) - 201)

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(0, 2)
plt.axis('off')
# plt.savefig("P2_signalcomparateur.pdf")
plt.show()