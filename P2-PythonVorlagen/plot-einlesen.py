	
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *
 
 
#################################################################################
#                                                                               #
#   Programm zum Linearen Fitten:                                               #
#   - liest x, y, xerror, yerror Werte aus Textdokument                         #
#   - fuehrt linearen Fit durch, beachtet dabei Fehler der einzelnen Messwerte  #
#   - Plot mit Messwerten, linearem Fit und Parametern des linearen Fits        #
#   - speichert Plot als png und pdf mit selbem Namen wie die Textdatei         #
#   - kann mehrere Plots in einem Durchlauf machen                              #
#   Programm von Julia Handl
#                                                                               #
#################################################################################
 
 
#################################################################################
# Schreibe in die filelist alle Textdateien rein, die ausgelesen werden sollen. #
# Lass jeweils '.txt' weg, setze den restlichen Namen in ''                     #
# und trenne verschiedene Textdateien mit Komma.                                #
#################################################################################
 
filelist = ['Lasera']
 
 
for file in filelist: # Alles, was jetzt kommt, wird fuer jedes Textdokument wiederholt, welches in der filelist drinsteht.
    # Einlesen der Daten aus der Textdatei
    with open('{}.txt'.format(file)) as f:
       
 
        x_value, y_value = [],[] # Definiert leere arrays x_value, y_value, x_error und y_error
        for line in f: #liest 4 Zahlen pro Zeile, ersetzt Komma durch Punkt, sofern vorhanden.
            x_value.append( float(line.split()[0].replace(',','.')) )
            y_value.append( float(line.split()[1].replace(',','.')) )
           
 
  
 
  
 
   
   
plt.plot(x_value, y_value, color='blue', label=fitlabel)
plt.legend(loc='best', numpoints = 1)
plt.title(Laser für Messung bei sichtbarem Licht, size=20) 
plt.xlabel(x_name, size=15)
plt.ylabel(y_name, size=15)
plt.grid(True)
   
