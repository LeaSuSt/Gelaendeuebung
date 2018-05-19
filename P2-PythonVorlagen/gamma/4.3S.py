'''
Plotting a Gaussian curve without data points
---------------------------------------------
 
This example creates a dummy Dataset object whose points lie exactly
on a Gaussian curve. The Fit will then converge toward that very same
Gaussian. When plotting, the data points used to "support" the curve
can be omitted.
This example shows how to use matplotlib further to annotate plots.
 
'''
 
###########
# Imports #
###########
 
# import everything we need from kafe
import kafe
from kafe import ASCII, LaTeX, FitFunction
 
# some additional things we'll need
from numpy import sqrt, pi, exp, linspace
import matplotlib.pyplot as plt
import numpy as np
###########################
# Fit function definition #
###########################
 
 
# Set an ASCII expression for this function
@ASCII(expression="1/(sqrt(2*pi)*sigma)*exp(-(x-mu)^2/(2*sigma^2))")
# Set some LaTeX-related parameters for this function
@LaTeX(name='\mathcal{N}', parameter_names=('\mu{}', '\sigma{}'),
       expression="\\frac{1}{\\sigma\\sqrt{2\\pi}}\\exp"
                  "(-\\frac{(x-\\mu)^2}{2\\sigma^2})")
# Declare that this is a fit function
@FitFunction
def gauss_2par(x, mu=0.0, sigma=1.0):
    '''Gaussian distribution'''
    norm_factor = 1.0 / (sqrt(2 * pi) * sigma)
    return exp(-((x - mu)**2 / (2 * sigma**2))) * norm_factor
 
############
# Workflow #
############
 

xm = np.linspace(0, 150, 150)
 
# Generate y-axis data from model
ym =[2 ,1 ,1, 6, 4, 5, 4, 3, 2, 0, 1, 3, 4, 1, 1, 3, 4, 5, 2, 2, 2, 5, 1, 1, 4, 2, 4, 0, 3, 2, 0, 3, 2, 3, 2, 2, 2, 0, 6, 2, 2, 2, 5, 2, 4, 3, 4, 1, 3, 2, 3, 1, 1, 2, 0, 2, 2, 2, 0, 0, 2, 1, 2, 1, 0, 3, 3, 1, 3, 1, 2, 1, 3, 1, 2, 1, 2, 4, 2, 3, 2, 0, 3, 1, 1, 0, 2, 1, 4, 1, 1, 4, 1, 3, 2, 0, 2, 6, 1, 1, 1, 0, 2, 0, 1, 5, 3, 3, 3, 4, 5, 3, 2, 1, 1, 1, 0, 1, 1, 0, 6, 1, 2, 3, 1, 2, 3, 1, 1, 1, 2, 2, 3, 5, 3, 5, 2, 3, 2, 3, 4, 0, 2, 2, 5, 2, 3, 1,3, 3, ]
 
# Construct the Datasets
my_dataset = kafe.Dataset(data=(xm, ym),
                          title="Standard-Normalverteilung")
 
# Fit the model to the data
my_fit = kafe.Fit(my_dataset, gauss_2par,
                  fit_label='Standard-Normalverteilung')
 
# Don't call do_fit for this Fit.
 
# Plot the Fit
my_plot = kafe.Plot(my_fit, show_legend=True)
 
# Instruct LaTeX to use the EulerVM package (optional, uncomment if needed)
#plt.rcParams.update({'text.latex.preamble': ['\\usepackage{eulervm}']})
 
# Draw the Plots
my_plot.plot_all(show_info_for='all',  # include every fit in the info box
                 show_data_for=None)   # don't show the points, just the curve
 
kdata = kafe.Dataset(data=(xm, ym), basename='kData',
                     title='Messdaten')
my_fit.do_fit()               # perform fit
kplot = kafe.Plot(my_fit)     # create plot object
kplot.axis_labels = [r'Z*Z', r'Energie in keV']
kplot.plot_all()            # make plots
#kfit.plot_correlations()    # eventually, produce contour plots
kplot.show()                # Show the plots






