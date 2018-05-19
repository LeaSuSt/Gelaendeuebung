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
    return m* x + b

# ---- begin of fit ---
# set the function
fitf = poly2             # own definition

V = 10.51
t = [ 195, 210, 225, 240, 250, 260, 270, 280, 290, 310, 320, 330, 340, 350, 360, 370, 380,  390, 400]
x = np.array([ 0.0513, 0.0494, 0.045, 0.042, 0.0395, 0.038, 0.0369, 0.0357, 0.035, 0.0342, 0.0335, 0.0329, 0.0322, 0.0317, 0.0313, 0.0310, 0.0306, 0.0303, 0.0299])
s = - V *np.log(x/1000) * 1/t

p= np.log(x)



kdata = kafe.Dataset(data=(t, p), basename='kData',
                     title='Messdaten')
#kdata.add_error_source('y', 'simple', ye)
#kdata.add_error_source('x', 'simple', xe)
kfit = kafe.Fit(kdata, fitf)  # create the fit
kfit.do_fit()               # perform fit
kplot = kafe.Plot(kfit)     # create plot object
kplot.axis_labels = [r't', r'ln(P)']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots

