import numpy as np
import matplotlib.pyplot as plt

from Utilisé import signal_osc1, signal_emetteur, signal_filtré_amplifié, signal_crete, signal_comparateur, signal_interrupteur, signal_bascule, signal_monostable_B, signal_monostable_A, signal_integrateur, signal_décideur, signal_SH

osc1 = signal_osc1.y * 30 - 15
osc2 = signal_emetteur.y * 30 - 15
filtred_amplified = signal_filtré_amplifié.y * 15
crete = signal_crete.y * 7.5
comparateur = signal_comparateur.y * 15
interrupteur = signal_interrupteur.y * 15


monostable_A = signal_monostable_A.y * 15
integrateur = signal_integrateur.y * 12
decideur = signal_décideur.y * 15
bascule = signal_bascule.y * 15
monostable_B = signal_monostable_B.y * 15
SH = signal_SH.y * 12

x = np.linspace(0, 10, 1001)

f, axs = plt.subplots(6, 2)
plt.subplots_adjust(hspace=0)
axs[0][0].plot(x, [0, *osc1])
axs[1][0].plot(x, [0, *osc2])
axs[2][0].plot(x, [0, *filtred_amplified])
axs[3][0].plot(x, [0, *crete])
axs[4][0].plot(x, [0, *comparateur])
axs[5][0].plot(x, [0, *interrupteur])

axs[0][1].plot(x, [0, *monostable_A])
axs[1][1].plot(x, [0, *integrateur])
axs[2][1].plot(x, [0, *decideur])
axs[3][1].plot(x, [0, *bascule])
axs[4][1].plot(x, [0, *monostable_B])
axs[5][1].plot(x, [0, *SH])
axs[5][1].set_ylim((0, 12))

for i in np.arange(5):
    axs[i][0].set_xticks([])
    axs[i][1].set_xticks([])

plt.savefig("TOUT.pdf")
plt.show()
