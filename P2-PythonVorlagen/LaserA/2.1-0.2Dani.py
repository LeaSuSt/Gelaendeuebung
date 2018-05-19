import numpy as np
import matplotlib.pyplot as plt

emin, emax = 0,6
npoints = 256
X = np.linspace(emin, emax, npoints, endpoint=True)

#y_ges = np.vstack([y1,y2,y3,y4,y5])
#x_ges = np.vstack([x1,x1,x1,x1,x1])
#print y_ges
x1= [1, 2, 3, 4, 5]
y1 = [8.5, 16, 24, 32.5, 39.5]
y2=[8.5, 16.5, 23.5, 31.5, 40]
y3 = [8.5, 16, 23.5, 31.5, 40]
y4 = [8, 16.5, 25, 32.5, 40]
y5 = [8, 16.5, 25, 32, 39.5]
plt.plot(x1, y1,"ok", label = 'Messreihe 1')
plt.plot(x1, y2,"or", label = 'Messreihe 2')
plt.plot(x1, y3,"og", label = 'Messreihe 3')
plt.plot(x1, y4,"om", label = 'Messreihe 4')
plt.plot(x1, y5,"oy", label = 'Messreihe 5')

x_ges = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
y_ges = [8.5, 8.5, 8.5, 8, 8, 16, 16.5, 16, 16.5, 16.5, 24, 23.5, 24.5, 25, 25, 32.5, 31.5, 32.0, 32.5, 32, 39.5, 40, 40, 40, 39.5]

print x_ges, y_ges

fit1 = np.polyfit(x_ges, y_ges, 1)
print fit1
plt.plot(X, fit1[0] * X + fit1[1], 'b', label = '7,88*x + 0,54')

print "Nochmal ein print:"
a =(632.8e-9*2.125*1e3)/(fit1[0]*1e-3)
print a



from scipy.stats import linregress
lin1 = linregress(x_ges,y_ges)
print lin1


#plt.xlim(emin, emax)
#plt.ylim(0,7)
plt.ylabel("Abstand in mm")
plt.xlabel("Beugungsordnung")
plt.grid(True)
#plt.title("Regressionsgerade der 1. Messung")
plt.legend(loc='best')
#plt.text(0.5, 1.2, r'25,515x + 2,166')
plt.show()
