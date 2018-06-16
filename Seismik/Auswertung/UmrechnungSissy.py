import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import curve_fit

#Daten eingeben:
sissyruck=np.array([1.2, 1.8, 2.4, 2.6, 3.2, 3.45, 3.7, 3.9, 4.1, 4.2, 4.3, 4.4, 4.6, 4.75, 4.9, 5.05, 5.45, 5.65, 6, 6.2, 6.3, 6.6, 6.9, 5.55+1.85, 5.55+2.1, 5.55+2.5, 5.55+2.7, 5.55+3.1, 5.55+3.2, 5.55+3.7, 5.55+3.9,
                    5.55+4.1, 5.55+4.25, 5.55+4.25, 5.55+4.4, 5.55+4.75, 5.55+4.9, 5.55+4.9, 5.55+5.05, 5.55+5.2, 5.55+5.25, 5.55+5.35, 5.55+5.4, 5.55+5.5, 5.55+5.5, 5.55+5.6, 5.55+5.8, 5.55+6, 5.55+5.95, 5.55+6.2, 5.55+6.3, 5.55+6.35, 5.55+6.6, 5.55+6.7, 5.55+6.9, 5.55+7, 9.25+3.6, 9.25+3.6, 9.25+3.75, 9.25+4, 9.25+4.1, 9.25+4.2, 9.25+4.7, 9.25+5, 9.25+5.2, 9.25+5.4, 9.25+5.5, 9.25+5.6, 9.25+5.7, 9.25+6.15, 9.25+6.25, 9.25+6.4
                    ])

sissyhin=np.array([1.2, 1.8, 2.4, 2.8, 3.5, 4.3, 4.8, 5.15, 5.5, 5.8, 5.9, 6, 6.05, 6.1, 6.2, 6.5, 6.6, 6.75, 6.85, 7.05, 5.55+1.7, 5.55+1.85, 5.55+2, 5.55+2.2, 5.55+2.3, 5.55+2.6, 5.55+2.8, 5.55+3.1, 5.55+3.2, 5.55+3.45, 5.55+3.6, 5.55+3.7, 5.55+4.05, 5.55+4.6, 5.55+4.7, 5.55+4.9, 5.55+5.15, 5.55+5.2, 5.55+5.5, 5.55+5.5, 5.55+5.9, 5.55+6, 5.55+6.2, 5.55+6.25, 5.55+6.4, 5.55+6.5, 5.55+6.7, 5.55+6.9, 5.55+7, 9.25+3.4, 9.25+3.5, 9.25+3.5, 9.25+3.5, 9.25+3.6, 9.25+3.7, 9.25+3.8, 9.25+3.9, 9.25+4, 9.25+4.2, 9.25+4.3, 9.25+4.4, 9.25+4.7, 9.25+4.9, 9.25+5, 9.25+5.2, 9.25+5.5, 9.25+5.7, 9.25+5.85, 9.25+6, 9.25+6.1, 9.25+6.2, 9.25+6.25])

#Umrechnung in Zeiten:
trueck = sissyruck *0.02/3.7
thin=sissyhin *0.02/3.7

#Profilkoordinaten:
x = [1.5, 2.5, 3.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 78.5, 80.5, 82.5, 84.5, 86.5, 88.5, 90.5, 92.5, 94.5, 96.5, 98.5, 100.5, 102.5, 104.5, 106.5, 108.5, 110.5, 112.5, 114.5, 116.5, 118.5, 120.5, 122.5, 124.5, 126.5, 128.5, 130.5, 132.5, 134.5, 135.5, 136.5, 137.5]

#umgedrehte Koordinaten (fuer den Rueckschuss)
reversed_x=x[::-1]

def func(xx, a, b):
    return a*xx+b

def ursprung(z,a):
  return a*z

#Plot Hinschuss:
plt.plot(x,thin,"x", color='black', label="Hinschuss")

##############################################################
#Geradenfits Hinschuss
grenze=8

popt1, pcov1= curve_fit(ursprung,x[0:grenze],thin[0:grenze])

y1=np.empty(grenze)
for i in range(0,grenze):
  y1[i]=ursprung(x[i],popt1[0])

plt.plot(x[0:grenze], y1, color='black', linewidth=1, label='1. refraktierte Welle')


popt2, pcov2= curve_fit(func,x[grenze:len(x)],thin[grenze:len(x)])

y2=np.empty(len(x))
for i in range(0,len(y2)):
  y2[i]=func(x[i],popt2[0],popt2[1])

plt.plot(x, y2, color='black', linewidth=1, label='2. refraktierte Welle')

print func(0,popt2[0],popt2[1])                           #y-achsenabschnitt 2.gerade

############################################################
#Geradenfits fuer Fehlerrechnung Hinschuss
grenzef=10

popt1f, pcov1f= curve_fit(ursprung,x[0:grenze],thin[0:grenze])

y1f=np.empty(grenzef)
for i in range(0,grenzef):
  y1f[i]=ursprung(x[i],popt1f[0])

plt.plot(x[0:grenzef], y1f, color='black', linewidth=1, label='1. refraktierte Welle')


popt2f, pcov2f= curve_fit(func,x[grenzef:len(x)],thin[grenzef:len(x)])

y2f=np.empty(len(x))
for i in range(0,len(y2f)):
  y2f[i]=func(x[i],popt2f[0],popt2f[1])

plt.plot(x, y2f,'--', color='black', linewidth=1, label='2. refraktierte Welle')


#Plot Ruechschuss
plt.plot(reversed_x, trueck,"*", color='black', label="Rueckschuss")

#########################################################
#Geradenfits Rueckschuss
def ursprung2(z,a):
  return a*(z-139.)

grenze2=6
popt3, pcov3= curve_fit(ursprung2,reversed_x[0:grenze2],trueck[0:grenze2])

y3=np.empty(grenze2)
for i in range(0,grenze2):
  y3[i]=ursprung2(reversed_x[i],popt3[0])

plt.plot(reversed_x[0:grenze2], y3, color='black', linewidth=2, label='1. refraktierte Welle')

popt4, pcov4= curve_fit(func,reversed_x[grenze2:len(x)],trueck[grenze2:len(x)])

y4=np.empty(len(x))
for i in range(0,len(y4)):
  y4[i]=func(reversed_x[i],popt4[0],popt4[1])

plt.plot(reversed_x, y4, color='black', linewidth=2, label='2. refraktierte Welle')


#########################################################
#Ausgabe des Plots
plt.xlabel("Abstand zu S11 in Richtung S12 in m", fontsize=14)
plt.ylabel("Zeit nach Zuendung in s", fontsize=14)
plt.legend(loc="lower center", fontsize=14)
plt.grid()
plt.show()
