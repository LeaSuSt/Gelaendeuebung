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

xm = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 520]
y = np.array([600, 500, 400, 320, 270, 230, 200, 170, 150, 130, 115, 104, 78, 67, 61, 54, 46, 42, 34.6, 27.9, 23.2, 19.2, 16.3, 14, 11.5, 10.1, 9.62, 7.51, 6.6, 5.77, 5, 4.52, 4.03, 3.6, 3.25, 2.92, 2.67, 2.45, 2.22, 2.06, 1.89, 1.75, 1.64, 1.54, 1.44, 1.35, 1.27, 1.2, 1.14, 1.07, 1.0, 0.95, 0.85, 0.81, 0.783, 0.747, 0.712, 0.674, 0.618, 0.573, 0.546, 0.529])
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
kplot.axis_labels = ['$Zeit\, in \, s$', r'$Spannung\, ln(P_1)\, in\, V $']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

