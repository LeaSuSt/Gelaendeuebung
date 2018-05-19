import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
 
print "Spannung in Temperatur umrechnen"

U = float(input("U? "))

T= 0.19084+25.83977 * U-0.59813* U**2-0,16786 * U**3-0.04991 * U**4
print T


