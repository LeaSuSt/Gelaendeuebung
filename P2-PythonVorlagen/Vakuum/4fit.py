#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys
import numpy as np


V = 10.51
t = [100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
x = np.array([ 1.63, 1.61, 1.57, 1.55, 1.52, 1.5,1.48, 1.46, 1.44, 1.42, 1.41, 1.39, 1.38, 1.36, 1.35, 1.34, 1.32, 1.31, 1.3, 1.29])
x = x* 10**(-4)
s = - V *np.log(x/1000) * 1/t
plt.xlabel('t')
plt.ylabel('ln(P)')
p= np.log(x)

plt.plot(t, p, "og")


plt.grid(True)

print s
print "----------------------------"
print p

#plt.axis([-50., 1050., -0.1, 1.2])

plt.show()
