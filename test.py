import numpy as np
import matplotlib.pyplot as plt

x1,x2 = np.mgrid[17:27:0.1,50:44:0.1]


plt.title('mgrid (dense meshgrid)')
plt.grid()
plt.xticks(xx[99])
plt.yticks(yy[:, 59])
plt.scatter(xx, yy, color="red", marker="x")
plt.figure()


