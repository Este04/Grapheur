import numpy as np
import matplotlib.pyplot as plt

filename = "Mesures-distances"

file_location = "C:/Users/robin/OneDrive/Documents/EPL UCLouvain/Bac2/Q4/ELEC Projet/Mesures/" + filename + ".csv"
data = np.loadtxt(file_location, delimiter=";", skiprows=1)

x = data[:, 1]
y1 = data[:, 0]
# y2 = data[4:4000, 2]
fit = np.polyfit(x[1:], y1[1:], 1)
droite = np.polyval(fit, x)

plt.plot(x, y1, label="Tension mesurée [V]", color="b")
plt.plot(x, droite, label="Régression linéaire", color="g", linestyle="--")

print(fit)

col_labels = ["Dist", "V"]
table_vals = np.array([x, y1]).T

the_table = plt.table(cellText=[[int(x[i]), y1[i]] for i in range(16)],
                      colWidths=[0.062, 0.08],
                      colLabels=col_labels,
                      loc='lower right')

# Texte sur le graphe :
# plt.text(12,2,'Table Title',size=8)

# Espace entre lex axes (fraction de la taille totale)
# f.subplots_adjust(hspace=0)

theorie = x * 2 / 100 / 344 * 961
plt.plot(x, theorie, label="Tension théorique [V]", color="r", linestyle="--")

plt.xlabel("Distance [cm]")
plt.ylabel("Tension [V]")
plt.title("Tension en fonction de la distance")
plt.legend(loc="upper left")
# plt.xlim(0, 4)
plt.ylim(0)
plt.savefig(filename + '.pdf')
plt.show()
