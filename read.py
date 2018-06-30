import numpy as np
import pandas as pd
from scipy.interpolate import NearestNDInterpolator


data = np.loadtxt("PredtandfilaGrid.dat")

index = data[:,0]
lon = data[:,1]
lat = data[:,2]
country = data [:,3]
altitude = data [:,4]


xx,yy = np.mgrid[lon,lat]

#myInterpolator= NearestNDInterpolator (lon,index)



#data1 =np.loadtxt("CARPATGRID_WS10_M.ser")
#god =data1[:,0]

