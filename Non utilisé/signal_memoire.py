import numpy as np
import matplotlib . pyplot as plt

y = [*np.zeros(301), *np.ones(1000-301)]
print(len(y))
integrateur = np.linspace(0, 1, int(500*5/6))

y = [*y[:301], *integrateur[301:301+20], *np.ones(1000-301-20)*integrateur[320]]
# print(np.shape(y), y)
x = np.linspace(0, 10, 1000)
plt.plot(x, y)
plt.axis('off')

# plt.savefig("Demo_signalSH.pdf")
plt.show()