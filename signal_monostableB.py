import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)

for i in range (0, 2, 1) :
    y[i * 510 + 301: int(i*510 + 5/6*510)] = np.ones(124)

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(0, 2)
plt.axis('off')
# plt.savefig("Demo_signalmonostableB.pdf")
plt.show()