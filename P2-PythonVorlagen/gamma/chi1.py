import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import matplotlib.pyplot as plt
import os, sys


print "Berechnen von Gausswerten"

x = float(input("x? "))


sigma=4.613
mu=22.8


f= 165 *(np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)

print f
