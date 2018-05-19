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

V = 10.51
t = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 110, 100, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]
x = np.array([2.7, 2.44, 2.2, 2.08, 1.97, 1.89, 1.82, 1.77, 1.72, 1.68, 1.63, 1.61, 1.57, 1.55, 1.52, 1.5,1.48, 1.46, 1.44, 1.42, 1.41, 1.39, 1.38, 1.36, 1.35, 1.34, 1.32, 1.31, 1.3, 1.29])
x = x* 10**(-4)
s = - V *np.log(x/1000) * 1/t

p= np.log(x)






kdata = kafe.Dataset(data=(t, p), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r'ln(P)', r't']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

