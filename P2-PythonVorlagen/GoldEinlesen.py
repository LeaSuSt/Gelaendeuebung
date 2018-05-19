import numpy as np
import matplotlib.pyplot as plt

x1,y1 = np.genfromtxt("gold1a.csv",delimiter=";")
x2,y2 = np.genfromtxt("gold2.csv",delimiter=";")
x3,y3 = np.genfromtxt("gold3.csv",delimiter=";")



f, axarr = plt.subplots(3, sharex=True)    
axarr[0].plot(x1, y1)
axarr[0].set_title('1.Messung')
axarr[0].set_xlabel(r'x in nm')
axarr[0].set_ylabel(r'y in pm')


axarr[1].plot(x2, y2)
axarr[1].set_title('2.Messung')
axarr[1].set_xlabel(r'x in nm')
axarr[1].set_ylabel(r'y in pm')

axarr[2].plot(x3, y3)
axarr[2].set_title('3.Messung')
axarr[2].set_xlabel(r'x in nm')
axarr[2].set_ylabel(r'y in pm')

plt.tight_layout()


plt.show()
