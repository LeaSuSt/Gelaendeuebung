#csv-Datei mit Hoehenangaben erstellen

import numpy as np

werte=np.genfromtxt('tachymeter_ergebnisse.txt')
relhoehe=np.array(werte[:,0])
np.savetxt("hoehen.csv", relhoehe, delimiter=",")

print "Program executed succesfully!"
