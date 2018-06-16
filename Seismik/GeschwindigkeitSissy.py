import numpy as np


#Berechnen der Geschwindigkeit
#uber Basaltang S21 S22 Hinschuss
#t1 erste Welle

#t2 refraktierte Welle

#t3 Kopfewlle an zweiter Schichtgrenze

v1 = 2./ 0.011

print ("Geschindigkeit v1 ist:") 
print v1


t2 = 0.0215-0.015
x= 4.
ti2= 0.00995
v2 = x/t2
print "Geschindigkeit v2 ist:" 
print v2 



#Winkel berechnen

w1 = np.arcsin(v1/v2)

print "Winkel w1"
print w1

#bestimmen von d

d1 = ti2*v1 /(2.*np.cos(w1))
print "d1 ist:" 
print d1






