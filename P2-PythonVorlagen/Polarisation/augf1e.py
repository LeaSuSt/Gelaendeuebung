#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy


r = np.array([0.147, 0.145, 0.142, 0.139, 0.136, 0.1334, 0.1329, 0.1334, 0.1318, 0.1338, 0.1352, 0.1350, 0.1354, 0.1364, 0.140, 0.1425, 0.1429, 0.1411, 0.1386, 0.1368, 0.1350, 0.1351, 0.1324, 0.1328, 0.1329, 0.1328, 0.1340, 0.1357, 0.1366, 0.1377, 0.1364, 0.1432, 0.1461, 0.1465, 0.1468, 0.1457, 0.147 ])

a = np.array([240., 230., 220., 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 360, 350, 340, 330, 320, 310, 300, 290, 280, 270, 260, 250, 240])
theta = a-45
theta *= 2.*np.pi / 360. 

print theta
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, "k.-")
ax.set_rmax(0.2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title( u"Zirkulare Polarisation", va='bottom')
plt.show()
