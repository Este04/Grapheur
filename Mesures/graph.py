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

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def simu_oscillateur1() :
    filename = "simu_oscillateur1"

    file_location = "Data/Oscillateur1.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  [*np.zeros(1), *data[:275, 0] * 1000]
    V1 = [*np.ones(1)*-1.340489e+01, *data[:275, 1]]
    Vo = [*np.ones(1)*-1.340489e+01, *data[:275, 2]]
    V2 = [*np.ones(1)*-1.147591e+01, *data[:275, 3]]

    plt.figure(figsize=(10, 6))
    plt.plot(t, V2, label="$V_{in_+}$ [V]", color="g")
    plt.plot(t, V1, label="$V_{in_-}$ [V]", color="b")
    plt.plot(t, Vo, label="$V_{out}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def simu_oscillateur2() :
    filename = "simu_oscillateur2"

    file_location = "Data/Oscillateur2.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[85:4585, 0] * 1000
    V1 = data[85:4585, 1]
    V2 = data[85:4585, 2]

    t -= t[0]
    # plt.figure(figsize=(10, 6))
    plt.figure(figsize=(10, 6))
    plt.plot(t, V2, label="$V_{oscillateur_1}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{oscillateur_2}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]" , fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def simu_integrateur():
    filename = "simu_integrateur"

    file_location = "Data/Integrateur.txt"
    data = np.loadtxt(file_location, delimiter="\t", skiprows=1)

    t =  data[600:5500, 0] * 1000
    V1 = data[600:5500, 1]
    V2 = data[600:5500, 2]

    t -= t[0]

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V1, label="$V_{contrôle}$ [V]", color="b")
    plt.plot(t, V2, label="$V_{intégrateur}$ [V]", color="r")

    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def mesures_integrateur() :
    filename = "mesures_integrateur"

    file_location1 = "Data/I_4ms_5v.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)
    file_location2 = "Data/M1_4ms_5v.csv"
    data2 = np.loadtxt(file_location2, delimiter=",", skiprows=8)

    t =  data1[175:3200, 1]
    V1 = data1[175:3200, 2]
    V2 = data2[175:3200, 2]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{monostable\ A}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{intégrateur}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

def mesures_monostableA():
    filename = "mesures_monostableA"

    file_location1 = "Data/mesures_monoA.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)
    file_location2 = "Data/mesures_osc1&VplusmonoA.csv"
    data2 = np.loadtxt(file_location2, delimiter=",", skiprows=8)

    t =  data1[1090:4150, 1]
    V1 = data1[1090:4150, 2]
    V2 = data1[1090:4150, 3]
    V3 = data2[1090:4150, 3]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{in_+}$ [V]", color="b")

    plt.plot(t, V1, label="$V_{monostable\ A}$ [V]", color="r")
    plt.plot(t, V3, label="$V_{seuil}$ [V]", color="g")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left', fontsize=18)

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

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

def mesures_oscillateur12() :
    filename = "mesures_oscillateur1&2"

    file_location1 = "Data/mesures_osc1&2.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)

    t =  data1[80:3110, 1]
    V1 = data1[80:3110, 2]
    V2 = data1[80:3110, 3]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{oscillateur_2}$ [V]", color="r")
    plt.plot(t, V1, label="$V_{oscillateur_1}$ [V]", color="b")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def mesure_SH():
    filename = "mesures_SH1m5"

    file_location1 = "Data/I&NE_4ms_5v_1m5.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)
    file_location2 = "Data/SH_4ms_5v_1m5.csv"
    data2 = np.loadtxt(file_location2, delimiter=",", skiprows=8)

    n = 470

    t =  data1[:, 1]
    V1 = data1[:, 2]
    V2 = np.array([*np.zeros(n), *data2[:len(data2)-n, 2]]) + 0.80
    V3 = data1[:, 3]

    t =   t[1550:4750]
    V1 = V1[1550:4750]
    V2 = V2[1550:4750]
    V3 = V3[1550:4750]


    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))

    plt.plot(t, V1, label="$V_{Intégrateur}$ [V]", color="r")
    plt.plot(t, V3, label="$V_{monostable\ B}$ [V]", color="g")
    plt.plot(t, V2, label="$V_{S/H}$ [V]", color="b")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper left', fontsize=18)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()


def simu_osc2integrateur() :
    filename = "simu_osc2integrateur"

    file_location1 = "Data/Oscillateur2int.txt"
    data1 = np.loadtxt(file_location1, delimiter="\t", skiprows=1)

    t =  data1[200:, 0]
    V1 = data1[200:, 1]
    V2 = data1[200:, 2]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{intégrateur}$ [V]", color="b")
    plt.plot(t, V1, label="$V_{oscillateur_2}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()

def mesures_crete() :
    filename = "mesures_crete"

    file_location1 = "Data/mesures_crete.csv"
    data1 = np.loadtxt(file_location1, delimiter=",", skiprows=8)

    t =  data1[:3000, 1]
    V1 = data1[:3000, 2]
    V2 = data1[:3000, 3]

    t = (t - t[0]) * 1000

    plt.figure(figsize=(10, 6))
    # plt.figure(figsize=(20, 6))
    plt.plot(t, V2, label="$V_{filtre}$ [V]", color="b")
    plt.plot(t, V1, label="$V_{crête}$ [V]", color="r")
    plt.grid(True)

    plt.xlabel("Temps [ms]", fontsize=20)
    plt.ylabel("Tension [V]", fontsize=20)
    plt.yticks(fontsize=20)
    plt.xticks(fontsize=20)
    # plt.title("Tension en fonction de la distance")
    plt.legend(loc='upper right', fontsize=20)

    plt.tight_layout()
    # plt.savefig(filename + '.pdf')
    plt.show()




# simu_bascule()
# simu_oscillateur1()
# simu_oscillateur2()
# simu_integrateur()
# mesures_integrateur()
# mesures_monostableA()
# mesures_oscillateur1()
# mesures_oscillateur12()
# mesure_SH()
# mesures_crete()
# simu_osc2integrateur()
