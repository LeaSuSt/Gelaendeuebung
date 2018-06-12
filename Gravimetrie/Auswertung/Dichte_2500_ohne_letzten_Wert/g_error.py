# -*- coding: utf-8 -*-
"""
Created on Fri May 25 17:57:35 2018

@author: Kappa
"""

import numpy as np

#_______________________________#
# berechne ungenauigkeit in mgal
#_______________________________#

#declare constants
vert_grad = 0.3086                       # mgal/m | Vertikalgradient
eichf = 1.04956                          #mgal/skt | 1.02391 für 686 Eichfaktor (gerätespezifisch)
g_abs = 980722.809                       #mgal | absoluter Schwerewert in Engen -> Notiz im Protokoll, dass dieser verwendet wurde (und nicht der lokale)



#declare errors
delta_zoll = 0.005                       #m | Unsicherheit auf die Ablesung am Zollstock bei der Bestimmung der Gerätehöhe; bedenke Schräghaltung!
delta_messrad = 0.003                    #skt| Fehler auf das Messrad (-> zum Drehen) 
                                         #bedenke auch Paralaxenfehler zb 0.010 skt?, gerätespezifisch
delta_gezeiten = 0.002                   #mgal| Fehler beim Ablesen der Gezeitentabelle
delta_libelle = 0.5*1.45*10**(-4)        #rad | Fehler auf die Genauigkeit der Horizontierung mit den Libellen; 1 Teilstrich entspricht 1.45*10**(-4) rad
#delta_x =                               Fehler auf die Bestimmung der Profilkoordinate, ist aber zu klein (Diskussion am Anfang: Änderung erst bei etwa 10 Metern)

#formel für den systematischen Messfehler auf g, Größtfehlerabschätzung
delta_g = vert_grad*delta_zoll+eichf*delta_messrad+delta_gezeiten+g_abs/2.*(delta_libelle)**2   #Formel: s. Hilfreiche Handreichung Nr. 3

#Gerät 156: array mit den driftkorrigierten Werte
drift_g_1 = np.array([4413.35,4413.148,4412.973,4412.893,4412.832,4412.677,4412.456,4412.2,4411.907])
drift_g_2 = np.array([4413.345,4413.091,4412.973,4412.887,4412.847,4412.669,4412.45,4412.207,4411.899])
#Anmerkung: letzter Wert weggelassen, da einer zu viel -> dadurch hervorgerufener Fehler egal


#Gerät 686: array mit den driftkorrigierten Werte
#drift_g_1 = np.array([3987.071,3986.962,3986.776,3986.641,3986.597,3986.467,3986.27,3986.066,3985.743])
#drift_g_2 = np.array([3987.075,3986.945,3986.787,3986.637,3986.593,3986.475,3986.27,3986.061,3985.705])


#Formel für den Fehler auf eine Einzelmessung der Messwerte
Delta_g=drift_g_1-drift_g_2
delta_g_std = np.sqrt(np.sum((Delta_g-np.mean(Delta_g))**2)/len(drift_g_1-1))


#einheit fehler in mgal!?
#output
print("delta_g = ", 1000*delta_g, " ist der theoretische statistische Fehler auf g.")
print("delta_g_std = ", 1000*delta_g_std, " ist der statistische Fehler bei der Bestimmung der driftkorrigierten Werte von g aus den Mittelwerten der Tabelle.")


