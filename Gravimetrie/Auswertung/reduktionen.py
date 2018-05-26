# Skript zur Berechunung der Reduktionen
# Gelaendereduktion wurde schon von Alexandra berechnet: kan eingelesen werden
# Einheiten immer mGal, kg, m

import numpy as np
import matplotlib.pyplot as plt

# driftkorrigierte und gemittelte Messwerte einlesen
# von oben nach unten von G0 nach G16
filelist = ['G156Driftkorrigierte_Messwerte']
for file in filelist: # Alles, was jetzt kommt, wird fuer jedes Textdokument wiederholt, welches in der filelist drinsteht.
    # Einlesen der Daten aus der Textdatei
    with open('{}.txt'.format(file)) as f:
	    f.readline()
	    f.readline()
	    gdrift = np.array[] # Definiert leere arrays
	    for line in f: #liest 4 Zahlen pro Zeile, ersetzt Komma durch Punkt, sofern vorhanden.
		    gdrift.append( float(line.split()[0].replace(',','.')) )

# relative Hoehe (Tachy), Rechtswert, Hochwert und Gelaendeeinfluss/Gelaendereduktion einlesen
filelist = ['tachymeter_ergebnisse']
for file in filelist: # Alles, was jetzt kommt, wird fuer jedes Textdokument wiederholt, welches in der filelist drinsteht.
    # Einlesen der Daten aus der Textdatei
    with open('{}.txt'.format(file)) as f:
	    f.readline()
	    f.readline()
	    relhoehe,rw,hw,gelred = np.array[],np.array[],np.array[],np.array[] # Definiert leere arrays
	    for line in f: #liest 4 Zahlen pro Zeile, ersetzt Komma durch Punkt, sofern vorhanden.
		    relhoehe.append( float(line.split()[0].replace(',','.')) )
		    rw.append( float(line.split()[1].replace(',','.')) )
		    hw.append( float(line.split()[2].replace(',','.')) )
		    gelred.append( float(line.split()[3].replace(',','.')) )

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
