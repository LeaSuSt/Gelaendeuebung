
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
 
filelist = ['testdata1','testdata2',]
 
 
for file in filelist: # Alles, was jetzt kommt, wird fuer jedes Textdokument wiederholt, welches in der filelist drinsteht.
    # Einlesen der Daten aus der Textdatei
    with open('{}.txt'.format(file)) as f:
        f.readline()                # Liest erste Zeile des Textdokuments, speichert sie nirgends (beinhaltet nur Erklaerungen)
        title = f.readline().replace('\r\n','') # Liest zweite Zeile, speichert den Titel
        f.readline()                # Liest dritte Zeile des Textdokuments, speichert sie nirgends
        x_name = f.readline().replace('\r\n','')# Liest vierte Zeile, speichert x-Achsenbeschriftung
        f.readline()
        y_name = f.readline().replace('\r\n','')
        f.readline()
 
        x_value, y_value, x_error, y_error = [],[],[],[] # Definiert leere arrays x_value, y_value, x_error und y_error
        for line in f: #liest 4 Zahlen pro Zeile, ersetzt Komma durch Punkt, sofern vorhanden.
            x_value.append( float(line.split()[0].replace(',','.')) )
            y_value.append( float(line.split()[1].replace(',','.')) )
            x_error.append( float(line.split()[2].replace(',','.')) )
            y_error.append( float(line.split()[3].replace(',','.')) )
 
    # Definiere lineare Funktion um sie an die Daten anzufitten
    def lin_func(p, x):
         m, c = p
         return m*x + c
 
    # Lineares Model
    lin_model = Model(lin_func)
 
    # RealData object: Definiere X- und Y-Groesse und dazugehoerige Fehler
    data = RealData(x_value, y_value, sx=x_error, sy=y_error)
 
    # ODR (Orthogonal Distance Regression): Passt das Model y=mx+c an unsere Daten an und gibt berechnete Werte aus
    odr = ODR(data, lin_model, beta0=[0., 1.])
    out = odr.run()
    print 'Daten zur linearen Regression fuer Datei {}.txt'.format(file)
    out.pprint()
    print '\n'
     
    # Vorbereitung der Plots
    m, m_error =  round(odr.output.beta[0],3), round(odr.output.sd_beta[0],3)
    c, c_error =  round(odr.output.beta[1],3), round(odr.output.sd_beta[1],3)
 
 
    x_fit = np.linspace(np.amin(x_value), np.amax(x_value), 1000)
    y_fit = lin_func(out.beta, x_fit)
 
    # Plotten
    plt.errorbar(x_value, y_value, xerr=x_error, yerr=y_error, linestyle='None', marker='o', color='black', markersize=5, label='Messwerte')
    fitlabel='Lineare Regression \n $ y= m \cdot x +c$ \n $m= {} \pm {}$ \n $c= {} \pm {}$'.format(str(m),str(m_error),str(c),str(c_error))
    plt.plot(x_fit, y_fit, color='blue', label=fitlabel)
    plt.legend(loc='best', numpoints = 1)
    plt.title(title, size=20) 
    plt.xlabel(x_name, size=15)
    plt.ylabel(y_name, size=15)
    plt.grid(True)
    plt.savefig('plot_{}.png'.format(file), dpi=800)
    plt.savefig('plot_{}.pdf'.format(file), dpi=800)
    plt.close()

xm = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
ym = [5.5, 5.5, 6, 6, 6, 11, 11, 11.5, 12, 11, 17, 17, 17, 17.5, 17, 22, 22, 23, 23, 22.5, 28, 28, 28,      28, 29]


