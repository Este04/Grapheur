import numpy as np
import matplotlib.pyplot as plt


def bascule() :
    filename = ""

    file_location = filename + ".csv"
    data = np.loadtxt(file_location, delimiter=";", skiprows=1)

    x = data[:, 1]
    y1 = data[:, 0]
    
    plt.plot(x, y1, label="Tension mesurée [V]", color="b")
    plt.plot(x, droite, label="Régression linéaire", color="g", linestyle="--")

    print(np.array(x, dtype=int))

    col_labels = ["Dist", "V"]
    table_vals = np.array([x, y1]).T
    print(table_vals)
    print([table_vals[:, 0].tolist(), table_vals[:, 1].tolist()])
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
    # plt.savefig(filename + '.pdf')
    plt.show()
