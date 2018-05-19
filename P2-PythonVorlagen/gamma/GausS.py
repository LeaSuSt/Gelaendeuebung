#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import matplotlib.pyplot as plt
import os, sys

# define a function (Gauss distribution)


def fgauss(x, mu, sigma):
    return (150 *(np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma))

def Poiss(x, m):
    return (150*(np.exp(-m)*m**x/(factorial(x))))

# generate random Gaussian numbers with mean 0 and variance 1
data = [2 ,1 ,1, 6, 4, 5, 4, 3, 2, 0, 1, 3, 4, 1, 1, 3, 4, 5, 2, 2, 2, 5, 1, 1, 4, 2, 4, 0, 3, 2, 0, 3, 2, 3, 2, 2, 2, 0, 6, 2, 2, 2, 5, 2, 4, 3, 4, 1, 3, 2, 3, 1, 1, 2, 0, 2, 2, 2, 0, 0, 2, 1, 2, 1, 0, 3, 3, 1, 3, 1, 2, 1, 3, 1, 2, 1, 2, 4, 2, 3, 2, 0, 3, 1, 1, 0, 2, 1, 4, 1, 1, 4, 1, 3, 2, 0, 2, 6, 1, 1, 1, 0, 2, 0, 1, 5, 3, 3, 3, 4, 5, 3, 2, 1, 1, 1, 0, 1, 1, 0, 6, 1, 2, 3, 1, 2, 3, 1, 1, 1, 2, 2, 3, 5, 3, 5, 2, 3, 2, 3, 4, 0, 2, 2, 5, 2, 3, 1,3, 3, 0]

# set parameters for Gaussdistribtion
m= 2.2
mu = 2.2
sigma = 1.473

# plot data as histogram
n, bins, patches = plt.hist(data, 50, facecolor='g',
                            log=False, alpha=0.5)  # plot data


# make plot nicer:
# axis labels
plt.xlabel('Ereignisanzahl ')
plt.ylabel('Anzahl der Messungen')
# title


# plot Gauss distribution
x = np.arange(0, 6., 0.01)
plt.plot(x, fgauss(x, mu, sigma), '-r')  
plt.plot(x, fgauss(x, mu, sigma), "-r", label="Gaussverteilung" )  
plt.plot(x, Poiss(x, m), 'g-')
plt.plot(x, Poiss(x, m), '-g', label="Poissonverteilung")# plot function


plt.legend(loc='upper right')
plt.grid(True)  # show a grid for orientation
plt.show()      # now display everything on the screen
