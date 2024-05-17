import numpy as np
import matplotlib.pyplot as plt


def bascule() :
    filename = "mesures_Bascule"

    file_location = "Data/Bascule.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[:, 0] * 1000
    V1 = data[:, 1]
    V2 = data[:, 2]


    # plt.figure(figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    plt.plot(t, V2, label="$V_{interrupteur}$ [V]", color="r")

    plt.plot(t, V1, label="$V_{bascule}$ [V]", color="b")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc=(1.05, 0.85))

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def oscillateur1() :
    filename = "mesures_oscillateur1"

    file_location = "Data/Oscillateur_1.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[:400, 0] * 1000
    V1 = data[:400, 1]
    Vo = data[:400, 2]
    V2 = data[:400, 3]

    plt.figure(figsize=(10, 6))
    plt.plot(t, V2, label="$V_{in_+}$ [V]", color="g")
    plt.plot(t, V1, label="$V_{in_-}$ [V]", color="b")
    plt.plot(t, Vo, label="$V_{out}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc=(1.05, 0.85))

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

# bascule()
# oscillateur1()