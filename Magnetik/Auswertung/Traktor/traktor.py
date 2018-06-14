import numpy as np
import matplotlib.pyplot as plt

y=np.loadtxt('traktortest7.dat', unpack=True)

print(len(y))
x=np.arange(0,30,1./8.)
print(len(x))

#plt.plot(x,y)
plt.xlabel('Zeit in s')
plt.ylabel('Gradient der Vertikalkomponente in nT/m')
plt.grid()

#plt.savefig('plot_traktor.pdf')

n=97 #Anzahl geplotteter Messpunkte
#Der Einfluss des Traktors ist nur am Anfang zu sehen.
#Deshalb reicht es, nur den Anfang der Messung zu plotten.

v=np.zeros(n)
w=np.zeros(n)
for i in range(0,n):
	v[i]=x[i]
	w[i]=y[i]

plt.plot(v,w)
plt.savefig('traktor_ausschnitt.pdf')
