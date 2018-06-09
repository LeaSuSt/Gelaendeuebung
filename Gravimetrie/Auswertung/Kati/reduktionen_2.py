# Skript zur Berechunung der Reduktionen
# Gelaendereduktion wurde schon von Alexandra berechnet: kann eingelesen werden
# Einheiten immer mGal, kg, m

import numpy as np
import matplotlib.pyplot as plt

# driftkorrigierte und gemittelte Messwerte einlesen
# von oben nach unten von G0 nach G16
gdrift1=np.genfromtxt('Relativwerte_unreduziert.txt')
gdrift=np.array(gdrift1)
# relative Hoehe (Tachy), Rechtswert, Hochwert und Gelaendeeinfluss/Gelaendereduktion einlesen
werte=np.genfromtxt('tachymeter_ergebnisse.txt')
relhoehe=np.array(werte[:,0])
rw = np.array(werte[:,1])
hw = np.array(werte[:,2])
gelred=np.array(werte[:,3])

rwred= np.min(rw)
rw= rw-rwred
hwred= np.min(hw)
hw= hw-hwred



# konstante Variablen
rho=2300. # Dichte



# Bouguer-Plattenreduktion (h: Hoehe ueber Referenzniveau)
def boug(h):
	return 0.0000419*rho*h

# Freiluftreduktion/Niveaureduktion (h: Hoehe ueber Referenzniveau)
def niv(h):
	return -0.3086*h

# Breitenreduktion (hw: Hochwert (Fortschritt in Nordrichtung bzgl Referenzpunkt))
def breit(hw):
	return 0.00082*hw


# ueberregionaler Trend nach Karte der Bougueranomalien BW (geologische Reduktion?) wird uns gegeben
# geologische Reduktion 
# hw: Hochwert (Fortschritt in Nordrichtung bzgl Referenzpunkt)
# rw: Rechtswert (Fortschritt in Ostrichtung bzgl Referenzpunkt)
def geol(hw,rw):
	return 0.000953*hw-0.00055*rw
    

print "Gelaendereduktion: "
print (gelred)
print "Bouguerreduktion: "
print (boug(relhoehe))
print "Niveaureduktion: "
print (niv(relhoehe))
print "Breitenreduktion: "
print (breit(hw))
print "Geologische Reduktion: "
print (geol(hw, rw))
#print ("array")
#print (rw)
#print (gdrift)
print ("Korrektur")
Korr = gdrift - ( gelred + boug(relhoehe) + niv(relhoehe) +breit(hw)+ geol(hw, rw) )
print (Korr)
np.savetxt("g_red.csv", Korr, delimiter=",")
np.savetxt('alle_korrekturen.txt',np.r_[gelred, boug(relhoehe), niv(relhoehe), breit(hw), geol(hw, rw), Korr], delimiter=",", header="Gelaendereduktion, Bouguerreduktion, Niveaureduktion, Breitenreduktion, geologische Reduktion, reduzierte Messwerte")

x = [0, 7.952, 14.929, 20.897, 25.86, 29.78, 32.799, 34.825, 36.842, 39.792, 43.761, 48.741, 54.697, 61.658, 69.585, 78.549, 84.602 ]
plt.plot(x, Korr, label='reduzierte Messwerte')
plt.xlabel('Profilkoordinate / m')
plt.ylabel('$\Delta g$ / mgal')
plt.legend()
plt.show()

