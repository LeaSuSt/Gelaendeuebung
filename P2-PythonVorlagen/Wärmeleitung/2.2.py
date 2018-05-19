''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''

import kafe # must be imported first to set backend

from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par
from kafe.function_library import linear_2par
import numpy as np, matplotlib.pyplot as plt


from numpy import exp, sqrt, pi
from scipy.special import gamma, wofz

# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression='exp(growth * x) * constant_factor')
@LaTeX(name='f', parameter_names=('\\lambda{}', 'a_0'),
       expression='a_0\\,\\exp(\\lambda x)')
@FitFunction
def exp_2par(x, growth=1.0, constant_factor=1.0):
    return exp(growth * x) * constant_factor

# ---- begin of fit ---
# set the function
fitf = exp_2par           # own definition

xm = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5]
ym = [5.5, 5.5, 6, 6, 6, 11, 11, 11.5, 12, 11, 17, 17, 17, 17.5, 17, 22, 22, 23, 23, 22.5, 28, 28, 28,      28, 29]


kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r'$I_P \, in \,A$', r'$\epsilon$']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

