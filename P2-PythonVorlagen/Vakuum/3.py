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
@ASCII(expression=' a * x + b')
@LaTeX(name='f', parameter_names=('a', 'b'), expression=r'a\,x+b')
@FitFunction
def poly2(x, a=0.0, b=0.0):
    return a * x + b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition
V = 10.51
t = [ 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 195, 210, 225, 240, 250, 260, 270, 280, 290, 310, 320, 330, 340, 350, 360, 370, 380,  390, 400]
x = np.array([400, 219, 219, 81.2, 56.2, 36.6, 25.1, 16.9, 11.5, 8.10, 6, 4.14, 2.99, 2.09, 1.52, 1.13, 0.825, 0.621, 0.502, 0.374, 0.303, 0.252, 0.206, 0.178, 0.148, 0.13, 0.117, 0.104, 0.092, 0.0844, 0.0789, 0.073, 0.0682, 0.0632, 0.06, 0.0513, 0.0494, 0.045, 0.042, 0.0395, 0.038, 0.0369, 0.0357, 0.035, 0.0342, 0.0335, 0.0329, 0.0322, 0.0317, 0.0313, 0.0310, 0.0306, 0.0303, 0.0299])
s = - V *np.log(x/1000) * 1/t
#ye = [x * 0.1 for x in ym]
#xe = [x * 0.1 for x in xm]

kdata = kafe.Dataset(data=(x, s), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = ['$Zeit\, in \, s$', r'$Spannung\, ln(P_1)\, in\, V $']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

