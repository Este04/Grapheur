import numpy as np
import matplotlib.pyplot as plt

from Utilisé import signal_osc1, signal_emetteur, signal_filtré_amplifié, signal_crete, signal_comparateur, \
    signal_interrupteur, signal_bascule, signal_monostable_B, signal_monostable_A, signal_integrateur, signal_décideur, \
    signal_SH

T = 2

osc1 = signal_osc1.y * 30 - 15
osc2 = signal_emetteur.y * 30 - 15
filtred_amplified = signal_filtré_amplifié.y * 15
crete = signal_crete.y * 7.5
Vref = np.full(len(crete) + 1, 1)
comparateur = signal_comparateur.y * 15
interrupteur = signal_interrupteur.y * 15

monostable_A = signal_monostable_A.y * 15
integrateur = signal_integrateur.y * 12
Vseuil = np.full(len(integrateur) + 1, integrateur[88])
decideur = signal_décideur.y * 15
bascule = signal_bascule.y * 15
monostable_B = signal_monostable_B.y * 15
SH = signal_SH.y * 12

x = np.linspace(0, 2 * T, 1001)

f, axs = plt.subplots(6, 2)
plt.subplots_adjust(hspace=0, wspace=0.4)
plt.subplots_adjust(left=0.1, right=0.99, top=0.99, bottom=0.06)

# === Colonne 1 ===
axs[0][0].plot(x, [0, *osc1], linewidth=0.8)
axs[0][0].set_ylabel('Oscillateur 1', fontsize=6.5)

axs[1][0].plot(x, [0, *osc2], linewidth=0.8)
axs[1][0].set_ylabel('Oscillateur 2', fontsize=6.5)

axs[2][0].plot(x, [0, *filtred_amplified], linewidth=0.8)
axs[2][0].set_ylabel('Filtre', fontsize=6.5)

axs[3][0].plot(x, [0, *crete], linewidth=0.8)
axs[3][0].plot(x, Vref, linewidth=0.8, linestyle='--', color='orange')
axs[3][0].set_yticks([0,Vref[0],5])
axs[3][0].set_yticklabels([0,r'$V_{\text{ref}}$'+'\n',5])
axs[3][0].set_ylabel('Crête', fontsize=6.5)

axs[4][0].plot(x, [0, *comparateur], linewidth=0.8)
axs[4][0].set_ylabel('Comparateur', fontsize=6.5)

axs[5][0].plot(x, [0, *interrupteur], linewidth=0.8)
axs[5][0].set_ylabel('Interrupteur', fontsize=6.5)

# === Colonne 2 ===
axs[0][1].plot(x, [0, *monostable_A], linewidth=0.8)
axs[0][1].set_ylabel('Monostable A', fontsize=6.5)

axs[1][1].plot(x, [0, *integrateur], linewidth=0.8)
axs[1][1].plot(x, Vseuil, linestyle='--', linewidth=0.8, color='orange')
axs[1][1].vlines(x=[T / 6, 7 * T / 6], ymin=-1, ymax=15, linestyle='--', linewidth=0.8, color='r')
axs[1][1].set_yticks([0,Vseuil[0], 10])
axs[1][1].set_yticklabels([0,r'$V_{\text{ref}}$'+'\n', 10])
axs[1][1].set_ylabel('Intégrateur', fontsize=6.5)

axs[2][1].plot(x, [0, *decideur], linewidth=0.8)
axs[2][1].set_ylabel('Décideur', fontsize=6.5)

axs[3][1].plot(x, [0, *bascule], linewidth=0.8)
axs[3][1].set_ylabel('Bascule', fontsize=6.5)

axs[4][1].plot(x, [0, *monostable_B], linewidth=0.8)
axs[4][1].vlines(x=[T * 142 / 500, T * 642 / 500], ymin=-1, ymax=0, linestyle='--', linewidth=0.8, color='r')
axs[4][1].set_ylabel('Monostable B', fontsize=6.5)

axs[5][1].plot(x, [0, *integrateur], linewidth=0.5, linestyle=':')
axs[5][1].plot(x, [0, *SH], linewidth=0.8, color='#1f77b4')
axs[5][1].set_ylim((-0.5, 12))
axs[5][1].vlines(x=[T * 142 / 500, T * 642 / 500], ymin=-1, ymax=15, linestyle='--', linewidth=0.8, color='r')
axs[5][1].set_ylabel('S/H', fontsize=6.5)


for i in range(6):
    if i!=5:
        axs[i][0].set_xticks([])
        axs[i][1].set_xticks([])
        for j in range(2):
            axs[i][j].spines['bottom'].set_linestyle(':')
    if i != 0:
        for j in range(2):
            axs[i][j].spines['top'].set_visible(False)

    for j in range(2):
        axs[i][j].yaxis.set_label_coords(-0.2, 0.5)
        axs[i][j].tick_params(axis='y', labelsize=8, width=0.5)
        for spine in axs[i][j].spines.values():
            spine.set_linewidth(0.5)

for j in range(2):
    axs[5][j].set_xticks([0, T, 2*T])
    axs[5][j].set_xticklabels([0,'T', '2T'])

# plt.text(x=T, y = 0, s="CHANGE PERIOD!")
# plt.savefig("TOUT.pdf")
plt.show()
