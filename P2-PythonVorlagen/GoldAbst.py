import numpy as np
import matplotlib.pyplot as plt

y = [(3.36+0.15)*10**(-10), (5-0.15)*10**(-10),  (1.1-0.297)*10**(-9), (2.9+0.225)*10**(-10), (1.5-0.712)*10**(-9), (0.712-0.4)*10**(-9)]

print y

plt.hist(y)
plt.show()
