import numpy as np
import matplotlib.pyplot as plt

import Signal_carré
osc1 = Signal_carré.y

import signal_emetteur
osc2 = signal_emetteur.y

import signal_recepteur
filtre = signal_recepteur.y

import signal_crete
crete = signal_crete.y

import signal_interrupteur
interrupteur = signal_interrupteur.y

import signal_comparateur
comparateur = signal_comparateur.y

import signal_monostableA
monostable_A = signal_monostableA.y

import signal_integrateur
integrateur = signal_integrateur.y

import signal_comparateur
comparateur = signal_comparateur.y


x = np.linspace(0, 10, 1001)

f, axs = plt.subplots(6, 2)
plt.subplots_adjust(hspace=0)
axs[0][0].plot(x, [0, *osc1])
axs[1][0].plot(x, [0, *osc2])
axs[2][0].plot(x, [0, *filtre])
axs[3][0].plot(x, [0, *crete])
axs[4][0].plot(x, [0, *comparateur])

axs[5][0].plot(x, [0, *interrupteur])
# plt.savefig("Demo_comparateur.pdf")
plt.show()
