import numpy as np
import matplotlib . pyplot as plt

rapport_cyclique = 1/6#1/2#1/6     #1/4
T = 510#22#510  #70        #230

y = np.zeros(1000)

i = 0
while i < 1000 :
    if i + rapport_cyclique*T < 1000 :
        y[i: int(i+rapport_cyclique*T)] = np.ones(int(rapport_cyclique * T))*1
    else :
        y[i::] = 1
        break
    i += round(rapport_cyclique*T)
    if i + (1-rapport_cyclique) * T < 1000:
        y[i : round(i + rapport_cyclique * T)] = np.zeros(round(rapport_cyclique * T))
    else :
        y[i::] = 0
        break
    i += int((1 - rapport_cyclique) * T)


x = np.linspace(0, 10, 1001)
print(y[84:86])
plt.plot(x, [0, *y])
plt.ylim(-0.1, 1.1)
plt.axis('off')
# plt.savefig("Demo_signal_osc1.pdf")
# plt.show()


