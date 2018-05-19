import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import matplotlib.pyplot as plt
import os, sys


print "Berechnen von Poissonverteilung"

x = float(input("x? "))


m= 22.8


p= 165*(np.exp(-m)*m**x/(factorial(x)))

print p

