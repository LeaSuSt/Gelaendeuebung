import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit


xdata = np.array([0, 2, 3, 4, 5,6, 8, 10, 12, 13, 17, 19, 21, 24, 27, 28, 32])
y=np.array([4, 3.5, 2.5, 2.4, 2, 2, 1.8, 2, 1.6, 1.5, 1, 1.2, 1, 1.2, 0.8, 0.6, 0.4])


def func(x, a, b):
    return a*np.exp(-b*x)

#y_noise = 0.2 * np.random.normal(size=xdata.size)

ydata = y 
plt.plot(xdata, ydata, 'bo', label='Messwerte')

popt, pcov = curve_fit(func, xdata, ydata)
popt
yerr=0.29*y
plt.errorbar(xdata, ydata, yerr=yerr, fmt='o')

from scipy.stats import linregress
lin1 = linregress(xdata,ydata)
print lin1

plt.plot(xdata, func(xdata, *popt), 'r-', label= 'fit: a=%5.3f, b=%5.3f' %tuple(popt))
plt.xlabel('Zeit in s')
plt.ylabel('doppelte Amplitude in m')
plt.legend()
plt.title('Messung bei 0,7 A')
plt.grid(True)
plt.show()
