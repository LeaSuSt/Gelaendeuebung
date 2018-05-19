#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys
import numpy as np


V = 10.51
t = [ 195, 210, 225, 240, 250, 260, 270, 280, 290, 310, 320, 330, 340, 350, 360, 370, 380,  390, 400]
x = np.array([ 0.0513, 0.0494, 0.045, 0.042, 0.0395, 0.038, 0.0369, 0.0357, 0.035, 0.0342, 0.0335, 0.0329, 0.0322, 0.0317, 0.0313, 0.0310, 0.0306, 0.0303, 0.0299])
s = - V *np.log(x/1000) * 1/t
plt.xlabel('Zeit in s')
plt.ylabel('ln(P)')
p= np.log(x)
print s
print "----------------------------"
print p
plt.plot(x, p, "og")


plt.grid(True)




plt.show()
