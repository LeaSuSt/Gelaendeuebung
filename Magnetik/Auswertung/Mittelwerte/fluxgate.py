# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1,y1=np.loadtxt('fluxgate_m21-m2_mean.dat', unpack=True, delimiter=',')
x3,y3=np.loadtxt('fluxgate_m24-m25_mean.dat', unpack=True, delimiter=',')

y1=y1-616.525
y3=y3-616.525

plt.plot(x1,y1,'o', label='Profil M21-M2')
plt.plot(x3,y3,'s', label='Profil M24-M25')

plt.xlabel('Profilkoordinate in m', fontsize=16)
plt.ylabel('Vertikalkomponente in nT', fontsize=16)

plt.grid()
plt.legend(fontsize=16)

plt.show()

