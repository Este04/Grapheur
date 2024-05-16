import numpy as np
import matplotlib.pyplot as plt
from Utilisé import signal_emetteur as osc2

principal = osc2.offsetted
recu = principal+np.array([*principal[-100:],*principal[:900]])*2/3 + np.array([*principal[-285:],*principal[:715]])*2/5

# Paramètres du signal de bruit
durée = 1.0  # Durée du signal en secondes
fréquence_échantillonnage = 1000  # Fréquence d'échantillonnage en Hz
nombre_échantillons = int(durée * fréquence_échantillonnage)
y = np.zeros_like(principal)
# Génération du bruit blanc gaussien
bruit = np.random.normal(0, 0.01, nombre_échantillons)
y = recu+1.5*bruit
# Temps
temps = np.arange(nombre_échantillons) / fréquence_échantillonnage

# Tracé du signal de bruit
plt.figure(figsize=(20, 10))
plt.plot(temps, y)
plt.axis('off')
# plt.title('Signal de bruit électrique')
# plt.xlabel('Temps (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)
# plt.savefig("Demo_signal_filtré_amplifié.pdf")
plt.show()
