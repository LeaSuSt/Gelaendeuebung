#! /usr/bin/python3
 
#########################################################
#                                                       #
#   Vorlage fuer Plots                                  #
#   Anselm Baur                                         #
#   Oktober 2016                                        #
#                                                       #
#########################################################
 
#%% Initialisierung
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit
 
 
a= 1.059
b= -1006.176
c= 0.659
d= -197.071
def temp_spannung(u):
    return 0.19084+25.83977*u-0.59813*u**2-0.16786*u**3-0.04991*u**4
 

x_raw = np.arange(-200,40)
#y_raw = 6564.7*0.0065*((x_raw+6989.5)/6564.7)**((1/0.0065)*(0.0065-1))
#y_raw = 846153.29613*5*10**(-5)*((x_raw+846587.62478)/846153.29613)**((5*10**(-5)-1)/(5*10**(-5)))
y_raw = a*((x+b)**c)+d
 
# Achsenausschnitt auf der x und y Achse
x_scal = np.array([-200,40])
y_scal = np.array([0,0.25])
 
label =["Temperatur", r'$\dot{T}(T)$']
 
#%% Plots
# FIGURE
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.clear()
 
 
 
###################################### Hier nur Style #################################
xmajor_ticks = np.arange(x_scal[0],x_scal[1]+0.1,(x_scal[1]-x_scal[0])/12)
xminor_ticks = np.arange(x_scal[0],x_scal[1],(x_scal[1]-x_scal[0])/120)
 
ymajor_ticks = np.arange(y_scal[0],y_scal[1]+0.01,(y_scal[1]-y_scal[0])/10)
yminor_ticks = np.arange(y_scal[0],y_scal[1],(y_scal[1]-y_scal[0])/100)
 
ax.set_xlim(x_scal[0],x_scal[1])
ax.set_ylim(y_scal[0], y_scal[1])
ax.axhline(linewidth=0.5, color="k")
ax.axvline(linewidth=0.5, color="k")
# Schriftgroesse der Achsenwerte
plt.setp(ax.get_xticklabels(), fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=18)
 
ax.set_xticks(xmajor_ticks)
ax.set_xticks(xminor_ticks, minor=True)
ax.set_yticks(ymajor_ticks)                                                       
ax.set_yticks(yminor_ticks, minor=True)
ax.tick_params("both", length=10, which="major")
ax.tick_params("both", length=5, which="minor")
 
ax.grid(which="major", alpha=0.5)
######################################################################################
 
#ax.set_title("Diagrammtitel", fontsize=18)
ax.set_ylabel(r'$\dot{T}$ in Abhängigkeit Temperatur $T$ in $^\circ$Cs$^{-1}$', fontsize=18)
ax.set_xlabel(r'Temperatur $T$ in $^\circ$C', fontsize=18)
 
color = ['b','r','g','k','c']
color_marker = ['rv','gv','gX','kd','co']
 
# Plot der Messwerte und der Fits
 
    #ax.plot(x_fit, y_fit[i], color[i], linestyle="solid", linewidth = 0.5, label="Fit " + label[i+1]) # Fit Plot
    #ax.errorbar(x_raw[i], y_raw[i], xerr=0.02, yerr=0.00981, fmt='o', c=color[i], label=label[i]) # Messdatenus
ax.plot(x_raw,y_raw, ""+color[0], label=label[1])
 
 
# Legende
ax.legend(loc="upper right", prop={'size':16}).get_frame().set_linewidth(0.5)
 
# Text im Plot
ax.text(-125, 0.18, r'$\dot{T}$' + ' = '+str(np.round(a*b,3))+r'$\left(\frac{T +'+str(np.round(-c,3))+r'}{'+str(np.round(a,3))+r'}\right)^{' + str(np.round((b-1)/(b),3))+r'}$', fontsize=16)
plt.show()


# Save figure
#fig.savefig('../fig/2_1_b_plot.eps')
