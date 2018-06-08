# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

x1,y1=np.loadtxt('m21_m2_mean.txt', unpack=True, delimiter=',')
x2,y2=np.loadtxt('M22_M23_Nr2_mean.txt', unpack=True, delimiter=',')
x3,y3=np.loadtxt('M24_M25_mean.txt', unpack=True, delimiter=',')
x4,y4=np.loadtxt('M26_M27_Nr2_mean.txt', unpack=True, delimiter=',')
x5,y5=np.loadtxt('M28_M29_Neu_mean.txt', unpack=True, delimiter=',')

y1=y1-48102
y2=y2-48102
y3=y3-48102
y4=y4-48102
y5=y5-48102
x4=x4+10
x5=x5+1

plt.plot(x2,y2,'-', color='black', linewidth=5, label='Profil M22-M23, Messgeraet Nr. 2')
plt.plot(x1,y1,'-', color='black', linewidth=3, label='Profil M21-M2, Messgeraet Nr. 1')
plt.plot(x3,y3,'-', color='black', linewidth=1.5,  label='Profil M24-M25, neues Messgeraet')
plt.plot(x4,y4,'--', color='black', linewidth=5, label='Profil M26-M27, Messgeraet Nr. 2')
plt.plot(x5,y5,'--', color='black', linewidth=2, label='Profil M28-M29, neues Messgeraet')

plt.xlabel('Profilkoordinate in m', fontsize=16)
plt.ylabel('Totalintensitaet in nT', fontsize=16)

plt.grid()
plt.legend(fontsize=16)

plt.show()
