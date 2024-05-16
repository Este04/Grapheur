import numpy as np
import matplotlib . pyplot as plt

rapport_cyclique = 1/6
T = 510#300

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
# offsetted = np.array([y[i] - max(y)/2 if i%len(pr<len(y)/2 else y[i] for i in range(len(y))])
offsetted = np.array(y.copy())

for i in range(len(offsetted)):
    if (i%T)/T < rapport_cyclique :
        offsetted[i] -= max(offsetted)/2
x = np.linspace(0, 10, 1001)
# plt.plot(x, [0, *y])
plt.plot(x, [0, *offsetted])
plt.axis('off')
plt.ylim(-1, 1)
# plt.savefig("P1_signalemetteurvf.pdf")
plt.show()


