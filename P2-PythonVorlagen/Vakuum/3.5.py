''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par
import numpy as np

# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression=' a * x^{-1} + b')
@LaTeX(name='f', parameter_names=('a', 'b'), expression=r'a\,x^(-1)+b')
@FitFunction
def poly2(x, a=0.0, b=0.0):
    return a * x**(-1) + b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition

x = np.array([0.063, 0.2, 0.63, 2, 6.3, 20, 63])
y = np.array([5.72, 36.48, 53.07, 65.77, 79.72, 100, 100])
#ye = [x * 0.1 for x in ym]
#xe = [x * 0.1 for x in xm]


kdata = kafe.Dataset(data=(x, y), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = ['$Wellenl\ddot{a}nge in nm$', r'$Spannung in V$']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

