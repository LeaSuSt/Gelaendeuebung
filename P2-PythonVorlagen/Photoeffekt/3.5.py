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
@ASCII(expression=' a * x^{-1} + b')
@LaTeX(name='f', parameter_names=('a', 'b'), expression=r'a\,x^(-1)+b')
@FitFunction
def poly2(x, a=0.0, b=0.0):
    return a * x**(-1) + b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition

xm = [360, 400, 440, 490, 540, 590]
ym = [-1.13, -0.93, -0.76, -0.65, -0.54, -0.53]
#ye = [x * 0.1 for x in ym]
#xe = [x * 0.1 for x in xm]

kdata = kafe.Dataset(data=(xm, ym), basename='kData',
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

