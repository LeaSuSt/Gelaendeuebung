''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''
import numpy as np
import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par


# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression='m * x + b')
@LaTeX(name='f', parameter_names=('m', 'b'), expression=r'm\,x + b')
@FitFunction
def poly2(x, m=1.0, b=0.0):
    return m* x +b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition

xm = [0, 2, 4, 6, 8]
ym = [19.8, 21.2, 22.4, 23.6, 24.9]
ye = [0.1, 0.1, 0.1, 0.1, 0.1]
xe = [0.5, 0.5, 0.5, 0.5, 0.5]

kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='Messdaten')
kdata.add_error_source('y', 'simple', ye)
kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r'Abstand in cm', r'Temperatur in Grad Celsius']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

