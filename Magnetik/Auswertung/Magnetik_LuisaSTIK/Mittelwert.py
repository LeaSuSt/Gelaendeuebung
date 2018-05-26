# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:11:57 2018

@author: Rebekka
"""

import numpy as np

daten=np.genfromtxt('m21_m2.dat')

Feldstaerken = daten[:, 1:3]

Mittelwerte = np.mean(Feldstaerken, axis=1)
print(Mittelwerte)