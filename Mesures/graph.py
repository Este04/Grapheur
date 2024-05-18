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

    file_location = "Data/Oscillateur1.txt"
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
    plt.legend(loc='upper right')

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


def simu_integrateur():
    filename = "simu_integrateur"

    file_location = "Data/Integrateur.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[600:, 0] * 1000
    V1 = data[600:, 1]
    V2 = data[600:, 2]

    t -= t[0]

    plt.figure(figsize=(15, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V1, label="$V_{contrôle}$ [V]", color="b")
    plt.plot(t, V2, label="$V_{intégrateur}$ [V]", color="r")

    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left')

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def mesures_integrateur() :
    filename = "mesures_integrateur"

    file_location1 = "Data/I_4ms_5v.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)
    file_location2 = "Data/M1_4ms_5v.csv"
    data2 = np.loadtxt(file_location2, delimiter=",", skiprows=8)

    t =  data1[175:4750, 1]
    V1 = data1[175:4750, 2]
    V2 = data2[175:4750, 2]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{monostable\ A}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{integrateur}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.savefig(filename + '.pdf')
    plt.show()

def mesures_monostableA():
    filename = "mesures_integrateur"

    file_location = "Data/M1E_4ms_3v.csv"
    data = np.loadtxt(file_location, delimiter=",", skiprows=8)

    t =  data[:, 1]
    V1 = data[:, 2]
    V2 = data[:, 2]

    # t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{monostable\ A}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{integrateur}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left')

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

# simu_bascule()
# simu_oscillateur1()
# simu_oscillateur2()
# simu_integrateur()
# mesures_integrateur()
mesures_monostableA()