import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

I, alpha=np.loadtxt('kalibrierung.dat', unpack=True)
B=I*26.5

slope, intercept, r_value, p_value, std_err = stats.linregress(B, alpha)

#To get coefficient of determination (r_squared)
print("r-squared:", r_value**2)
print(slope)
print(1./slope)

#Plot the data along with the fitted line
#Noch umrechnen in nT!!!!
plt.plot(B, alpha, 'o', label='Messwerte')
plt.plot(B, intercept + slope*B, 'r', label='lineare Regression')
plt.xlabel(r'$B_z$ in nT')
plt.ylabel(r'Ablesewert in Skt')
plt.legend()

plt.show()
#plt.savefig('kalibrierung.pdf')
