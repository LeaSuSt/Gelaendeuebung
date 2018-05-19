import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
 
print "Epsilon berechnen"

IH = float(input("IHeiz? "))

UH = float(input("UHeiz? "))

IP = float(input("IP? "))

UP = float(input("UP? "))

E = IH * UH /(IP * UP)
print E


