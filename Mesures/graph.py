import numpy as np
import matplotlib.pyplot as plt


def simu_bascule() :
    filename = "simu_bascule"

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


def simu_oscillateur1() :
    filename = "simu_oscillateur1"

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


def simu_oscillateur2() :
    filename = "simu_oscillateur2"

    file_location = "Data/Oscillateur2.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[:, 0] * 1000
    V1 = data[:, 1]
    V2 = data[:, 2]

    # plt.figure(figsize=(10, 6))
    plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{oscillateur_1}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{oscillateur_2}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc=(1.05, 0.85))

    plt.tight_layout()
    plt.savefig(filename + '.pdf')
    plt.show()

# simu_bascule()
# simu_oscillateur1()
simu_oscillateur2()