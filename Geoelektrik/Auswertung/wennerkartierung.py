# -*- coding: utf-8 -*-
"""
Created on Thu May 24 17:08:38 2018

@author: Kappa
"""

import numpy as np
import matplotlib.pyplot as plt

#import
data = np.genfromtxt('wennerkartierung.txt')
x = data[:,0]
x_reversed= x[::-1]-(16-7.5)

plt.plot(x_reversed, data[:,1], 'o')

plt.xlabel('Abstand in m')
plt.ylabel('spezifischer elektrischer Widerstand in Ohm m')
plt.legend()
plt.title('Wenner-Kartierung')
plt.grid(True)
plt.show()
