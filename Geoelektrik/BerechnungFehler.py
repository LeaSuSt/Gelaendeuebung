import numpy as np

a = 5.
b = 10.
c = 5.
d = 10.


f = 2 *np.pi/(1/a-1/b+1/c-1/d)

fa = 2 *np.pi/(a**2*(1/a-1/b+1/c-1/d)**2)

fb = 2 *np.pi/(b**2*(1/a-1/b+1/c-1/d)**2)

fc = 2 *np.pi/(c**2*(1/a-1/b+1/c-1/d)**2)

fd = 2 *np.pi/(d**2*(1/a-1/b+1/c-1/d)**2)

Fehler = np.sqrt((fa*0.2)**2+(fb*0.4)**2+(fc*0.2)**2+(fd*0.4)**2)
print f
print Fehler


print "Wiederstand"
print 237.593/220.13*f
print "roh Fehler"
print 237.593/220.13*Fehler
