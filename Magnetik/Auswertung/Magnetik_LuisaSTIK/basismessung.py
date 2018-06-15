import numpy as np
import matplotlib.pyplot as plt

t,alpha=np.loadtxt('basismessung.dat',unpack=True)
k=253
deltak=3.7
deltaalpha=0.03

B=alpha*k
B=B-min(B)
deltaB=np.sqrt((alpha*deltak)**2+(k*deltaalpha)**2)

plt.plot(t,B,'s', label='Tagesgang')
plt.xlabel('Zeit nach 12:35 Uhr in min', fontsize=16)
plt.ylabel('relative Vertikalkomponente in nT', fontsize=16)
plt.errorbar(t,B,yerr=deltaB, label='Fehlerbalken')
plt.legend()
plt.show()
