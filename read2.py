#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:25:43 2018

@author: meteo
"""
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from matplotlib.colors import BoundaryNorm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from metpy.interpolate import interpolate_to_grid, remove_nan_observations


to_proj = ccrs.AlbersEqualArea(central_longitude=-1., central_latitude=10.)

#load cordinates
fname = 'PredtandfilaGrid.dat'
#col_names = ['index','lon','lat','country','altitude'] ovo koristimo ako nemama definisane imena kolona
#load temp
df = pd.read_fwf(fname,na_values='MM')

#names = col_names
lon = df['lon'].values
lat = df['lat'].values
xp, yp, _ = to_proj.transform_points(ccrs.Geodetic(), lon, lat).T

#data1 = pd.read_fwf("CARPATGRID_TA_M.ser")
#data1.rename( columns={'Unnamed: 0':'Year','Unnamed: 1':'Month'}, inplace=True )
#xx = data1.drop(['Year','Month'], axis=1)

#x1= xx.loc[0]
data1 = pd.read_csv('/home/meteo/Documents/Master_rad/CARPATGRID_TA_M.ser',sep ='\s+')
#y = int(input('Unesite godinu:'))
#m = int(input('Unesite mesec:'))

y=2000
m=3
x1 = data1.loc[y,m]

x_masked, y_masked, t = remove_nan_observations(xp, yp, x1.values)
tempx, tempy, temp = interpolate_to_grid(x_masked, y_masked, t, interp_type='cressman',
                                 minimum_neighbors=8, search_radius=150000, hres=50000)

temp = np.ma.masked_where(np.isnan(temp), temp)

levels = list(range(-20, 20, 1))
cmap = plt.get_cmap('viridis')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

fig = plt.figure(figsize=(20, 10))
view = fig.add_subplot(1, 1, 1, projection=to_proj)

view.set_extent([22.7,19,46.6,44.1])
view.add_feature(cfeature.STATES.with_scale('50m'))
view.add_feature(cfeature.OCEAN)
view.add_feature(cfeature.COASTLINE.with_scale('50m'))
view.add_feature(cfeature.BORDERS, linestyle=':')


mmb = view.pcolormesh(tempx, tempy, temp, cmap=cmap, norm=norm)
fig.colorbar(mmb, shrink=.4, pad=0.02, boundaries=levels)



view.set_title('Srednja temperatura')

plt.show()








