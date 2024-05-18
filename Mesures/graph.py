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

    t =  data[:275, 0] * 1000
    V1 = data[:275, 1]
    Vo = data[:275, 2]
    V2 = data[:275, 3]

    plt.figure(figsize=(10, 6))
    plt.plot(t, V2, label="$V_{in_+}$ [V]", color="g")
    plt.plot(t, V1, label="$V_{in_-}$ [V]", color="b")
    plt.plot(t, Vo, label="$V_{out}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def simu_oscillateur2() :
    filename = "simu_oscillateur2"

    file_location = "Data/Oscillateur2.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[96:4585, 0] * 1000
    V1 = data[96:4585, 1]
    V2 = data[96:4585, 2]

    t -= t[0]
    # plt.figure(figsize=(10, 6))
    plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{oscillateur_1}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{oscillateur_2}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
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
    filename = "mesures_monostableA"

    file_location1 = "Data/mesures_monoA.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)
    file_location2 = "Data/mesures_osc1&VplusmonoA.csv"
    data2 = np.loadtxt(file_location2, delimiter=",", skiprows=8)

    t =  data1[1090:5665, 1]
    V1 = data1[1090:5665, 2]
    V2 = data1[1090:5665, 3]
    V3 = data2[1090:5665, 3]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{in_+}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{monostable\ A}$ [V]", color="r")
    plt.plot(t, V3, label="$V_{seuil}$ [V]", color="g")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left')

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

def mesures_oscillateur1() :
    filename = "mesures_oscillateur1"

    file_location1 = "Data/mesures_osc1&VplusmonoA.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)

    t =  data1[960:4000, 1]
    V1 = data1[960:4000, 2]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V1, label="$V_{oscillateur_1}$ [V]", color="b")
    plt.grid(True)

    plt.xlabel("Temps [ms]")
    plt.ylabel("Tension [V]")
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right')

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

# simu_bascule()
# simu_oscillateur1()
# simu_oscillateur2()
simu_integrateur()
# mesures_integrateur()
# mesures_monostableA()
# mesures_oscillateur1()