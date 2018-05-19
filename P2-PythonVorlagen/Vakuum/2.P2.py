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

xm = [55, 60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 520]
y = np.array([1000, 1000, 900, 750, 600, 510, 420, 360, 274, 223, 187, 162, 140, 124, 110, 98.2, 87, 78.2, 72, 66.6, 61.7, 57.4, 52.9, 49.2, 46.6, 44, 42, 40, 38.2, 36.4, 34.3, 32.6, 31.1, 30.3, 29.1, 28, 27.2, 26.4, 25.6, 24.7, 23.9, 23.1, 21.7, 21.1, 20.5, 19.8, 19.4, 18.9, 18, 17.3, 16.9, 16.6 ])
ym = np.log(y)
#ye = [x * 0.1 for x in ym]
#xe = [x * 0.1 for x in xm]

kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = ['$Zeit\, in \, s$', r'$Spannung\, ln(P_2)\, in\, V $']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

