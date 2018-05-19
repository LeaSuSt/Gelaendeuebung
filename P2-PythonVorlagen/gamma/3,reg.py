''' general example for fitting with kafe
      - read datafile fitexample.dat
      - perform fit (2nd orfer polynomial)
      - show and save output
'''

import kafe
from kafe.function_tools import FitFunction, LaTeX, ASCII
from kafe.function_library import quadratic_3par


# ---- fit function definition in kafe style
#         (decorators for nice output not mandatory)
@ASCII(expression='a * x + b')
@LaTeX(name='f', parameter_names=('a', 'b'), expression=r'a\,x+ b')
@FitFunction
def poly2(x, a=1.0, b=0.0):
    return a * x + b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition

ym = [32.7, 74.1, 58.8, 57.7, 68]
xm = [3136,  6724, 5476, 5329, 6241]


kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='Messdaten')
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r'Z*Z', r'Energie in keV']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

