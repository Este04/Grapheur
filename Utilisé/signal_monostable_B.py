import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)
T = 510

for i in range (0, 2, 1) :
    y[i*T + 101 : int(i*T + 121)] = np.ones(20)

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(0, 2)
plt.axis('off')
# plt.savefig("Demo_signal_monostable_B.pdf")
# plt.show()