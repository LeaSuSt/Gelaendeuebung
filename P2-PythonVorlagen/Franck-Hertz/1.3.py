    
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
 
 
 # Definiere lineare Funktion um sie an die Daten anzufitten
xm = np.linspace(0., 30., 30)
ym = [0., 0., 0.02, 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.18, 0.21, 0.23, 0.25, 0.29, 0.32,               0.35, 0.37, 0.4, 0.44, 0.49, 0.53, 0.55, 0.59, 0.66, 0.73, 0.78, 0.92, 1.05, 1.34]
sx = np.linspace(0, 1, 30)   
sy = np.linspace(0, 2, 30)
x_error = np.linspace(0, 1, 30)
y_error = np.linspace(0, 2, 30)

def lin_func(p, x):
        m, c = p
        return x**m + c
 
    # Lineares Model
lin_model = Model(lin_func)
 
    # RealData object: Definiere X- und Y-Groesse und dazugehoerige Fehler
data = RealData(xm, ym)
 
    # ODR (Orthogonal Distance Regression): Passt das Model y=mx+c an unsere Daten an und gibt berechnete Werte aus
odr = ODR(data, lin_model, beta0=[0., 1.])
out = odr.run()
    #print 'Daten zur linearen Regression fuer Datei {}.txt'.format(file)
out.pprint()
    #print '\n'
     
    # Vorbereitung der Plots
 # Vorbereitung der Plots
m, m_error =  round(odr.output.beta[0],3), round(odr.output.sd_beta[0],3)
c, c_error =  round(odr.output.beta[1],3), round(odr.output.sd_beta[1],3)
 
x_fit = np.linspace(np.amin(xm), np.amax(xm), 1000)
y_fit = lin_func(out.beta, x_fit)

    # Plotten
plt.errorbar(xm, ym, xerr=x_error, yerr=y_error, linestyle='None', marker='o', color='black', markersize=5, label='Messwerte')
fitlabel='Lineare Regression \n $ y= m \cdot x +c$ \n $m= {} \pm {}$ \n $c= {} \pm {}$'.format(str(m),str(m_error),str(c),str(c_error))
plt.plot(x_fit, y_fit, color='blue')
plt.legend(loc='best', numpoints = 1)
plt.title("a", size=20) 
plt.xlabel("a", size=15)
plt.ylabel("c", size=15)
plt.grid(True)
plt.savefig('plot_{}.png'.format(file), dpi=800)
plt.savefig('plot_{}.pdf'.format(file), dpi=800)
plt.close()


