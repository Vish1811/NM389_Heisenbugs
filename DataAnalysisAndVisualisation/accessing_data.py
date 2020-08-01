from netCDF4 import Dataset
import numpy as np

#Reading in the netcdf file
data=Dataset(r'C:/Users/codev/Desktop/SIHFinale2020/SAC_WRF_FCST_5KM_20200720(2).nc') 
#print(data)

# displayimg the names of the variables
print(data.variables.keys())

print()
print()
print()

#accessing the variables
lon = data.variables['lon']
print(lon)

print()
print()
print()

lat = data.variables['lat']
print(lat)

print()
print()
print()

lev_2 = data.variables['lev_2']
print(lev_2)

print()
print()
print()


time = data.variables['time']
print(time)

print()
print()
print()

t2 = data.variables['t2']
print(t2)
print()
print()
print()
psfc = data.variables['psfc']
print(psfc)

print()
print()
print()

rainnc = data.variables['rainnc']
print(rainnc)

print()
print()
print()

clflo = data.variables['clflo']
print(clflo)

print()
print()
print()

# accessing the data from the variables
time_data=data.variables['time'][:]
print(time_data)

lon_data=data.variables['lon'][:]
print(lon_data)

lat_data=data.variables['lat'][:]
print(lat_data)