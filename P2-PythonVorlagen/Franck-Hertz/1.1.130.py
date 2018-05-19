#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import os, sys
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
 
filelist = ['1.1.170']
 
 
for file in filelist: # Alles, was jetzt kommt, wird fuer jedes Textdokument wiederholt, welches in der filelist drinsteht.
    # Einlesen der Daten aus der Textdatei
    with open('{}.txt'.format(file)) as f:
        f.readline()                # Liest erste Zeile des Textdokuments, speichert sie nirgends (beinhaltet nur Erklaerungen)
        f.readline()   
 
        zero, x_value, y_value = [], [],[] # Definiert leere arrays x_value, y_value, x_error und y_error
        for line in f: #liest 4 Zahlen pro Zeile, ersetzt Komma durch Punkt, sofern vorhanden.
            
            zero.append(float(line.split()[0].replace(',','.')) )
            x_value.append(float(line.split()[1].replace(',','.')) )
            y_value.append(float(line.split()[2].replace(',','.')) )
            
 
    # Definiere lineare Funktion um sie an die Daten anzufitten
    
 
 
    # RealData object: Definiere X- und Y-Groesse und dazugehoerige Fehler
    data = RealData(x_value, y_value)
 
     
    # Vorbereitung der Plots
   # m, m_error =  round(odr.output.beta[0],3), round(odr.output.sd_beta[0],3)
   # c, c_error =  round(odr.output.beta[1],3), round(odr.output.sd_beta[1],3)
 
 
   # x_fit = np.linspace(np.amin(x_value), np.amax(x_value), 1000)
    #y_fit = lin_func(out.beta, x_fit)
 
    # Plotten
    #plt.errorbar(x_value, y_value, xerr=x_error, yerr=y_error, linestyle='None', marker='o', color='black', markersize=5, label='Messwerte')
    #fitlabel='Lineare Regression \n $ y= m \cdot x +c$ \n $m= {} \pm {}$ \n $c= {} \pm {}$'.format(str(m),str(m_error),str(c),str(c_error))
    plt.plot(y_value, x_value)
    #plt.legend(loc='best', numpoints = 1)
    plt.title("Aufg.1.1e", size=20) 
    plt.xlabel("Beschleunigungsspannung in V", size=15)
    plt.ylabel(u"Aufhängerstrom I$_{\mathrm{A}}$ in nA", size=15)
    plt.grid(True)
    #plt.savefig('plot_{}.png'.format(file), dpi=800)
    #plt.savefig('plot_{}.pdf'.format(file), dpi=800)
    #plt.close()
    plt.show()
