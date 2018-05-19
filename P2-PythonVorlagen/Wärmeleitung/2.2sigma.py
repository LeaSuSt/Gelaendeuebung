import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
 
print "Fehler berechnen"

IH = float(input("IHeiz? "))

UH = float(input("UHeiz? "))

IP = float(input("IP? "))

UP = float(input("UP? "))

E = np.sqrt((UH/(IP*UP))**2 *0.5**2 + (IH/(IP*UP))**2 * 0.1**2 + (IH*UH/(IP**2*UP))**2 * 0.5**2 + (IH*UH/(IP*UP**2))**2 * 0.1**2)
print E


