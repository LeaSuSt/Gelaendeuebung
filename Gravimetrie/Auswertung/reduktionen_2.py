# Skript zur Berechunung der Reduktionen
# Gelaendereduktion wurde schon von Alexandra berechnet: kan eingelesen werden
# Einheiten immer mGal, kg, m

import numpy as np
import matplotlib.pyplot as plt

# driftkorrigierte und gemittelte Messwerte einlesen
# von oben nach unten von G0 nach G16
gdrift=np.genfromtxt('G156Driftkorrigierte_Messwerte.dat')

# relative Hoehe (Tachy), Rechtswert, Hochwert und Gelaendeeinfluss/Gelaendereduktion einlesen
relhoehe,rw,hw,gelred=np.genfromtxt('tachymeter_ergebnisse.txt')

# konstante Variablen
rho=2300. # Dichte

# ueberregionaler Trend nach Karte der Bougueranomalien BW (geologische Reduktion?) wird uns gegeben

# Bouguer-Plattenreduktion (h: Hoehe ueber Referenzniveau)
def boug(h):
	return 0.0000419*rho*h

# Freiluftreduktion/Niveaureduktion (h: Hoehe ueber Referenzniveau)
def niv(h):
	return -0.3086*h

# Breitenreduktion (hw: Hochwert (Fortschritt in Nordrichtung bzgl Referenzpunkt))
def breit(hw):
	return 0.00082*hw

# geologische Reduktion 
# hw: Hochwert (Fortschritt in Nordrichtung bzgl Referenzpunkt)
# rw: Rechtswert (Fortschritt in Ostrichtung bzgl Referenzpunkt)
def geol(hw,rw):
	0.000953*hw-0.00055*rw

print (boug(relhoehe))
