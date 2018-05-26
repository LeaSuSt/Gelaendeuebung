# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:08:38 2018

@author: Kappa
"""

import numpy as np
import matplotlib.pyplot as plt

#import
data = np.genfromtxt('wennerkartierung.txt')

plt.plot(data[:,0], data[:,1])
plt.show()