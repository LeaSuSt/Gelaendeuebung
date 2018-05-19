#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys

import numpy as np
import matplotlib.pyplot as plt
import scipy


r = [4.038, 4.0381, 4.037, 4.0347, 4.0314, 4.0226, 4.0175, 3.998, 3.599, 2.803, 2.861, 3.7586, 4.003, 4.018, 4.0268, 4.0321, 4.0353, 4.0373, 4.0384, 4.0383, 4.0374, 4.0354, 4.0321, 4.0272, 4.0187, 3.999, 3.598, 2.781, 2.817, 3.769, 4.002, 4.0187, 4.0267, 4.0321, 4.0355, 4.0376, 4.038]

theta = np.array([330., 320., 310, 300, 290, 280, 270, 260, 250, 240, 230, 220, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 110, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 360, 350, 340, 330.])
theta *= 2.*np.pi / 360. 

print theta
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, "k.-")
ax.set_rmax(5)
#ax.set_rticks([0.5, 1, 1.5, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title(u"Weißes Licht", va='bottom')
plt.show()
