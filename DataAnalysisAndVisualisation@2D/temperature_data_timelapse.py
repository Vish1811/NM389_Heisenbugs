from netCDF4 import Dataset

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

data=Dataset(r'C:/Users/codev/Desktop/SIHFinale2020/SAC_WRF_FCST_5KM_20200720(2).nc') 
#print(data)

# displayimg the names of the variables
#print(data.variables.keys())

lons=data.variables['lon'][:]
lats=data.variables['lat'][:]
time=data.variables['time'][:]
t2=data.variables['t2'][:]

mp=Basemap(projection ='merc',
           llcrnrlon=42.8,
           llcrnrlat=-2,
           urcrnrlon=105.37,
           urcrnrlat=38.78,
           resolution='i')
lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)

days=np.arange(0,24)
for i in days:
    c_scheme = mp.pcolor(x,y,np.squeeze(t2[i,:,:,:]),cmap='jet')
    mp.drawcoastlines()
    mp.drawstates()
    mp.drawcountries()
    cbar=mp.colorbar(c_scheme,location='right',pad='10%')
    day=i+1
    plt.title("Temperature:DayTime"+str(day)+'hr')
    plt.savefig(r'C:\Users\codev\Desktop\Automate\temp_jpegs'+'\\'+str(day)+'.jpg')
    plt.clf()