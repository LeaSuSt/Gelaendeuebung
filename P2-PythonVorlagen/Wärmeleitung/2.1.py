#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys


x = [5, 10, 15, 18]
a = [16.5, 30.3, 34.0, 36.0]


plt.xlabel('Strom I in A')
plt.ylabel(u'Temperatur in Grad Celsius')

plt.plot(x, a, "ok")



plt.grid(True)

plt.legend(loc='upper left')

plt.show()
