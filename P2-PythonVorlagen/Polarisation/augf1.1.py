#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys

import numpy as np
import matplotlib.pyplot as plt
import scipy


r = np.array([0.2561, 0.2566, 0.2371, 0.2053, 0.172, 0.128, 0.0860, 0.0470, 0.0209, 0.0060, 0.0066, 0.0238, 0.0520, 0.088, 0.131, 0.174, 0.218, 0.239, 0.254, 0.237, 0.208, 0.171, 0.129, 0.084, 0.047, 0.019, 0.006, 0.0067, 0.0214, 0.0508, 0.088, 0.128, 0.173, 0.207, 0.236, 0.2561])

theta = np.array([330., 320., 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 360, 350, 340, 330.])
theta *= 2.*np.pi / 360. 

print theta
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, "k.-")
ax.set_rmax(5)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("Weises Licht", va='bottom')
plt.show()
