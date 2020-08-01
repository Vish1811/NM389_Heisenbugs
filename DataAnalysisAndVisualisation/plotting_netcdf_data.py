#importing the important libraries 

#netCDF4 for dealing with netcdf file
from netCDF4 import Dataset

#for dealing with data
import numpy as np

#for plotting the data on a map
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

#loading the data
data=Dataset(r'C:/Users/codev/Desktop/SIHFinale2020/SAC_WRF_FCST_5KM_20200720(2).nc') 
print(data)

# displayimg the names of the variables
print(data.variables.keys())

# Acessing the required variables
lons=data.variables['lon'][:]
lats=data.variables['lat'][:]
time=data.variables['time'][:]
t2=data.variables['t2'][:]

#making a map 
mp=Basemap(projection ='merc',
           llcrnrlon=42.8,
           llcrnrlat=-2,
           urcrnrlon=105.37,
           urcrnrlat=38.78,
           resolution='i')
lon,lat=np.meshgrid(lons,lats)
x,y=mp(lon,lat)
c_scheme = mp.pcolor(x,y,np.squeeze(t2[0,:,:,:]),cmap='jet')
mp.drawcoastlines()
mp.drawstates()
mp.drawcountries()
cbar=mp.colorbar(c_scheme,location='right',pad='10%')

plt.title("Heisenbugs")
plt.show()