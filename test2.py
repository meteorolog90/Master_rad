import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import NearestNDInterpolator


y = np.arange(44, 50, 0.1)
x = np.arange(17, 27, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
#z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
#h = plt.contourf(x,y,z)



