import numpy as np
import matplotlib.pyplot as plt

xx,yy = np.mgrid[17:27:0.1,44:50:0.1]


plt.figure(num=None, figsize=(10, 8), dpi=50, facecolor='w', edgecolor='k')

#plt.figure(num=None, figsize=(20, 18), dpi=200, facecolor='w', edgecolor='k')
plt.title('mgrid (dense meshgrid)')
plt.grid()
plt.xticks(xx[0]) #izmedju 17-28 imamo 100 tacaka
plt.yticks(yy[:,0]) #izmedju 44-50 imam 60 tacaka
plt.scatter(xx, yy, color="red", marker="x")

#print(xx[0])

