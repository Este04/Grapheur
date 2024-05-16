import numpy as np
import matplotlib . pyplot as plt
import colorsys
rapport_cyclique = 1/6
T = 510

y = np.zeros(1000)

def oscillo (plage, T2) :
    rapport_cyclique2 = 1/2
    p = np.zeros(plage)
    j = 0
    while j < plage:
        if j + rapport_cyclique2 * T2 < plage:
            p[j: int(j + rapport_cyclique2 * T2)] = np.ones(int(rapport_cyclique2 * T2)) * 1
        else:
            p[j::] = 1
            break
        j += round(rapport_cyclique2 * T2)
        if j + (1 - rapport_cyclique2) * T2 < plage:
            p[j: round(j + rapport_cyclique2 * T2)] = np.zeros(round(rapport_cyclique2 * T2))
        else:
            p[j::] = 0
            break
        j += int((1 - rapport_cyclique2) * T2)
    return p

i = 0
while i < 1000 :
    if i + rapport_cyclique*T < 1000 :
        y[i: int(i+rapport_cyclique*T)] = oscillo(int(rapport_cyclique*T), 22)
    else :
        y[i::] = oscillo(len(y) - i, 10)
        break
    i += round(rapport_cyclique*T)
    if i + (1-rapport_cyclique) * T < 1000:
        y[i : round(i + rapport_cyclique * T)] = np.zeros(round(rapport_cyclique * T))
    else :
        y[i::] = 0
        break
    i += int((1 - rapport_cyclique) * T)

x = np.linspace(0, 10, 1001)
# plt.plot(x, [0, *y], label="V$_{émis}$")
plt.plot(x, [*np.zeros(101), *y[0:len(y)-100]])#, color='b', label="V$_{direct}$")
plt.plot(x, [*np.zeros(301), *y[0:len(y)-300]])#, color='b', label="V$_{réfléchi}$")
###
bruit = np.random.normal(0, 0.2, 1001)
# plt.plot(x, bruit, linewidth=0.5, color=colorsys.hsl_to_rgb(205,71,41))
plt.plot(x, bruit, linewidth=0.5)
###
# plt.legend(bbox_to_anchor=(0.90,0.75),loc="upper left",borderaxespad=0.)
print(y)
plt.ylim(-2, 2)
plt.axis('off')
# plt.savefig("P2_signalbruit.pdf")
plt.show()