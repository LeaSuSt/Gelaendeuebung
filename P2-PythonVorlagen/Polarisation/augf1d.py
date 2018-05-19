#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os, sys
import numpy as np
import matplotlib.pyplot as plt
import scipy


r = np.array([0.0803, 0.0773, 0.0836, 0.0883, 0.092, 0.0924, 0.0911, 0.0873, 0.0822, 0.0750, 0.0682, 0.062, 0.0567, 0.0536, 0.0526, 0.0543, 0.057, 0.0629, 0.069, 0.075, 0.0813, 0.086, 0.0894, 0.0904, 0.0896, 0.0869, 0.0824, 0.0758, 0.0696, 0.0625, 0.0568, 0.054, 0.0538, 0.0554, 0.0591, 0.064, 0.0803])

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

ax.set_title( u"Mit 170 $\mathbf{\mu}$m Glimmerplättchen", va='bottom')
plt.show()
