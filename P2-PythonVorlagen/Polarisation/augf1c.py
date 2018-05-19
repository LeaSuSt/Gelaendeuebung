#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy


r = np.array([0.095, 0.070, 0.047, 0.0326, 0.0256, 0.026, 0.036, 0.0465, 0.0686, 0.0951, 0.1173, 0.1385, 0.1534, 0.1626, 0.162, 0.1526, 0.1373, 0.113, 0.086, 0.059, 0.0399, 0.0255, 0.018, 0.019, 0.0286, 0.0464, 0.0682, 0.092, 0.119, 0.141, 0.1568, 0.163, 0.164, 0.156, 0.138, 0.1168, 0.095])

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

ax.set_title( u"Mit 60 $\mathbf{\mu}$m Glimmerplätchen", va='bottom')
plt.show()
