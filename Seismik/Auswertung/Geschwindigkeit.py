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

t3 =0.0325- 0.027
ti3 = 0.018
x = 10.
v3 = x/t3
print "Geschindigkeit v3 ist:" 
print v3

#Winkel berechnen

w1 = np.arcsin(v1/v2)
w2 = np.arcsin(v2/v3)
w12 = np.arcsin(v1/v3)
print "Winkel w1, w2, w12"
print w1, w2, w12

#bestimmen von d

d1 = ti2*v1 /(2.*np.cos(w1))
print "d1 ist:" 
print d1

d2 = (ti3*v2-2*d1*np.cos(w12)*v2/v1)*(1/(2*np.cos(w2)))
print "d2 ist:" 
print d2





