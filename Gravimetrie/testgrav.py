import numpy as np
 
def niv(h):
  return -0.3086*h*10.**(-5.) #Ergebnis in SI-EInheiten

def boug(h,rho):
  return 0.0419*h*rho*10.**(-8.) #Ergebnis in SI-Einheiten

print niv(0.523)
print boug(0.523,2.8*10**3.)
print -niv(0.523)-boug(0.523,2.8*10**3.)
print boug(1,2387)
