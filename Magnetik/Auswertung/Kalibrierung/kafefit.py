''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''

import kafe
import numpy as np
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par


# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression='b * x + c')
@LaTeX(name='f', parameter_names=('a', 'b'), expression=r'a\,x+b')
@FitFunction
def lin(x,  a=-0.0039, b=0):
    return a * x + b











# ---- begin of fit ---
# set the function
fitf = lin             # own definition




# --------- begin of workflow ----------------------
# set data

#rawdata
I, alpha=np.loadtxt('kalibrierung.dat', unpack=True)
B=I*26.5

#x=np.array([6, 10, 8, 13, 7]) 
#y=np.array([36.1, 11.5, 17.4, 7.55, 23.9])
Be=0.1*26.5 #besser array
alphae=0.03



#weitere Variablen ggf umformungen



kdata = kafe.Dataset(data=(B, alpha), basename='kData',
                     title='Messwerte')
kdata.add_error_source('x', 'simple', Be)
kdata.add_error_source('y', 'simple', alphae)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()                 # perform fit
kplot = kafe.Plot(kfit)       # create plot object
kplot.axis_labels = [r'$B_z$ in nT$', r'Ablesewert in Skt']
kplot.plot_all()           # make plots






kplot.show()               # Show the plots
