# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1,y1=np.loadtxt('M26_M27_Nr2_mean.txt', unpack=True, delimiter=',')
#x3,y3=np.loadtxt('M24_M25_mean.txt', unpack=True, delimiter=',')

y1=y1-48102
#y2=y2-48102
#y3=y3-48102

#plt.plot(x2,y2,'s', label='Profil M22-M23, Messgeraet Nr. 2')
plt.plot(x1,y1,'o', label='Profil M26-M27, Messgeraet Nr. 2')
#plt.plot(x3,y3,'^', label='Profil M24-M25, neues Messgeraet')

plt.xlabel('Profilkoordinate in m', fontsize=16)
plt.ylabel('Totalintensitaet in nT', fontsize=16)

plt.grid()
plt.legend(fontsize=16)

plt.show()

