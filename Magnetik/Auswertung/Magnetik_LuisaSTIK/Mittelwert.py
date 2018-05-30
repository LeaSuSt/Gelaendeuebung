# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:11:57 2018

@author: Rebekka
"""

import numpy as np

#daten=np.genfromtxt('M22_M23_Nr2.txt')

#Feldstaerken = daten[:, 1:3]

#Mittelwerte = np.mean(Feldstaerken, axis=1)
#print(Mittelwerte)

#np.savetxt('M22_M23_Nr2_mean.txt', daten[1,:], Mittelwerte)

#Ziel: <x> <Leerzeichen> <mw> in eine txt-Datei schreiben!!!

x,y1,y2,y3=np.loadtxt('M22_M23_Nr2.txt', unpack=True)
mw=(y1+y2+y3)/3.
daten=np.array([len(x),2])
daten[:,0]=x
daten[:,1]=mw
np.savetxt('M22_M23_Nr2_mean.txt', daten)
