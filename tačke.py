import pandas as pd
import numpy as np
    

s = pd.read_csv('/home/meteorolog/Documents/Master_rad/CARPATGRID_TA_M.ser',sep ='\s+')
d = pd.read_csv('/home/meteorolog/Documents/Master_rad/PredtandfilaGrid.dat', sep ='\s+')

y = int(input('Unesite godinu: ' ' '))
m = int(input('Unesite mesec:' ' '))


x1 = s.loc[y,m]

d1 = d.drop(['index'],axis=1)
a = d1.set_index(['lon','lat'])


#y = int(input('Unesite godinu:'))
#m = int(input('Unesite mesec:'))
#d = int(input('Unesite dan:'))
#print (s.loc[y,m,d])


#izdvajanje vrednosti
lon = d1['lon'].values
lat = d1['lat'].values
country = d1['country'].values
altitude = d1['altitude'].values
temp = x1.values

#pravljenje DataFrame oblika
r = { 'lon': lon, 'lat':lat, 'country':country,'altitude':altitude, 'temp':temp}
podaci = pd.DataFrame(r,columns=['lon','lat','temp','country','altitude'])
indexi = podaci.set_index(['lon','lat'])

xx = float(input('Unesite longitudu u rasponu od 17.0-27.0:'))
yy = float(input('Unesite latitudu u rasponu od 50.0-44.0:'))


print (indexi.loc[xx,yy])
