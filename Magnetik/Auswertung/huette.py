import numpy as np
import matplotlib.pyplot as plt

x,y=np.loadtxt('Huette.txt', unpack=True)

#x-Werte rumdrehen: Basis bei x=0
#Huette bei 19m
#Tisch bei 13,5m
reversed_x = x[::-1]
print (reversed_x)


plt.plot(reversed_x,y,'x')
plt.xlabel('Abstand zur Basisstation in m')
plt.ylabel('Totalintensitaet in nT')

plt.savefig('plot_huette.pdf')
