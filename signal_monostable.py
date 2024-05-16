import numpy as np
import matplotlib . pyplot as plt

y = np.zeros(1000)

for i in range (0, 2, 1) :
    y[i*500 :i*500 + int (500*5/6)] = np.ones( int (500*5/6))
    # y[int (500*5/6) : 500] =

x = np.linspace(0, 10, 1001)
plt.plot(x, [0, *y])
plt.ylim(0, 2)
plt.axis('off')
# plt.savefig("P2_signalmonostable.pdf")
plt.show()