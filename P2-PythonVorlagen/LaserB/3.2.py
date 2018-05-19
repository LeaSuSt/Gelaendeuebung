import numpy as np
import matplotlib.pyplot as plt

emin, emax = -5, 3
npoints = 256
X = np.linspace(emin, emax, npoints, endpoint=True)

#y_ges = np.vstack([y1,y2,y3,y4,y5])
#x_ges = np.vstack([x1,x1,x1,x1,x1])
#print y_ges


N = 2000
l = 0.105

x_ges = [-2.9, -1.5, 0, 1.5, 2.5]
y_ges = np.array([9, 11, 12, 13, 14])




plt.plot(x_ges, y_ges,"ok", label = 'Messpunkte')
print x_ges, y_ges

fit1 = np.polyfit(x_ges, y_ges, 1)
print fit1
plt.plot(X, fit1[0] * X + fit1[1], 'b', label = '0.87*x+11.87')

print "Nochmal ein print:"
a =(632.8e-9*2.125*1e3)/(fit1[0]*1e-3)
print a



from scipy.stats import linregress
lin1 = linregress(x_ges,y_ges)
print lin1

plt.ylim(8, 15)
#plt.xlim(emin, emax)
#plt.ylim(0,7)
plt.xlabel("Strom I in A")
plt.ylabel("Winkel in Grad ")
plt.grid(True)
#plt.title("Regressionsgerade der 1. Messung")
plt.legend(loc='best')
#plt.text(0.5, 1.2, r'25,515x + 2,166')
plt.show()
