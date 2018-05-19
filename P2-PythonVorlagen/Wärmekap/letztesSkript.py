import matplotlib.pyplot as plt
import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *

x=22

c=19.76/(0.338*(1.05855*0.6592 *((x-197.07083)/1.05855)**(1-1/0.6592)-5.01602*10**(-5)*(22.7228-x)))

print c
