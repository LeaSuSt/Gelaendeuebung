#!/usr/bin/python
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import factorial
import matplotlib.pyplot as plt
import os, sys

# define a function (Gauss distribution)


def fgauss(x, mu, sigma):
    return (165 *(np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma))

def Poiss(x, m):
    return (165*(np.exp(-m)*m**x/(factorial(x))))

# generate random Gaussian numbers with mean 0 and variance 1
data = [20, 16, 23, 31, 30, 29, 24, 26, 20, 21, 15, 19, 17, 22, 24, 21, 32, 33, 20, 30, 16, 23, 24, 15, 19,  22, 27, 19, 22, 26, 25, 21, 21, 24, 20, 20, 25, 24, 23, 18, 21, 29, 22, 19, 28, 25, 18, 24, 30, 19, 22, 32, 32, 26,  29, 24, 29, 18, 23, 32, 20, 23, 24, 20, 26, 26, 16, 27, 11, 19, 23, 22, 21, 20, 26, 17, 27, 19, 24, 30, 19, 22, 18, 19, 21, 14, 21, 18, 25, 18, 20, 27, 25, 26, 22, 25, 19, 32, 24, 21, 24, 20, 18, 27, 20, 23, 32, 31, 28, 21, 36, 24, 17, 23, 16,21, 18, 22, 17, 20, 27, 19, 25, 23, 23, 21, 27, 17, 26, 31, 31, 24, 21, 18, 26, 22, 24, 20, 22, 18, 26, 23, 25, 22, 21, 19, 13, 22, 31, 18]

# set parameters for Gaussdistribtion
m= 22.8
mu = 22.8
sigma = 4.613

# plot data as histogram
n, bins, patches = plt.hist(data, 50, facecolor='g',
                            log=False, alpha=0.5)  # plot data


# make plot nicer:
# axis labels
plt.xlabel('Ereignisanzahl ')
plt.ylabel('Anzahl der Messungen')
# title


# plot Gauss distribution
x = np.arange(0, 40., 0.1)
plt.plot(x, fgauss(x, mu, sigma), '-r')  
plt.plot(x, fgauss(x, mu, sigma), "-r", label="Gaussverteilung" )  
plt.plot(x, Poiss(x, m), 'g-')
plt.plot(x, Poiss(x, m), '-g', label="Poissonverteilung")# plot function


plt.legend(loc='upper right')
plt.grid(True)  # show a grid for orientation
plt.show()      # now display everything on the screen
