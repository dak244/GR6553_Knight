# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 11:14:39 2025

@author: desit
"""

import matplotlib.pyplot as plt
import numpy as np
import netCDF4
import cartopy #import cartopy library
import cartopy.feature as cf
import cartopy.crs as ccrs
import metpy



data235=netCDF4.Dataset('SM_D2017235_Map_SATSSS_data_3days.nc')
data238=netCDF4.Dataset('SM_D2017238_Map_SATSSS_data_3days.nc')
#data74=netCDF4.Dataset('SM_D2024184_Map_SATSSS_data_3days.nc')

#print(data628.variables.keys())

lats235= data235.variables['latitude'][:]
lons235= data235.variables['longitude'][:]
sss235= data235.variables['sss'][:]
sssunits=data235.variables['sss'].units
lats238= data238.variables['latitude'][:]
lons238= data238.variables['longitude'][:]
sss235=sss235[0,0,:,:]
# #time=data628.variables['time'][:]
sss238=data238.variables['sss'][:]
sss238=sss238[0,0,:,:]
# lats74= data74.variables['latitude'][:]
# lons74= data74.variables['longitude'][:]
# sss74=data74.variables['sss'][:]
# sss74=sss74[0,0,:,:]

#print(time)

plt.figure(figsize=(8,6))
proj=ccrs.LambertConformal(central_longitude=-95.,central_latitude=25.,standard_parallels=(30.,30.))
ax= plt.axes(projection=proj)
ax.set_extent([-100, -80, 20, 35])
ax.add_feature(cf.LAKES,color='white')
ax.add_feature(cf.OCEAN,color='white')
ax.add_feature(cf.STATES,edgecolor='grey')
ax.add_feature(cf.BORDERS,edgecolor='grey')
ax.add_feature(cf.COASTLINE,edgecolor='grey')
ax.add_feature(cf.LAND,color='papayawhip')
ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False,linewidth=1,color='white',alpha=0.5,linestyle='dashed')


plt.contourf(lons235,lats235,sss235, cmap='jet',transform=ccrs.PlateCarree())
plt.colorbar(orientation='horizontal',label='psu')
plt.title('Ocean Salinity Before Hurricane Harvey 8/25/17')
plt.show()

#plot for 7/1
plt.figure(figsize=(8,6))
proj=ccrs.LambertConformal(central_longitude=-95.,central_latitude=25.,standard_parallels=(30.,30.))
ax= plt.axes(projection=proj)
ax.set_extent([-100, -80, 20, 35])
ax.add_feature(cf.LAKES,color='white')
ax.add_feature(cf.OCEAN,color='white')
ax.add_feature(cf.STATES,edgecolor='grey')
ax.add_feature(cf.BORDERS,edgecolor='grey')
ax.add_feature(cf.COASTLINE,edgecolor='grey')
ax.add_feature(cf.LAND,color='papayawhip')
ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False,linewidth=1,color='white',alpha=0.5,linestyle='dashed')


plt.contourf(lons238,lats238,sss238, cmap='jet',transform=ccrs.PlateCarree())
plt.colorbar(orientation='horizontal',label='psu')
plt.title('Ocean Salinity During Hurricane Harvey on 8/25/17')
plt.show()


# #plot for SSS for 7/4
# plt.figure(figsize=(8,6))
# proj=ccrs.LambertConformal(central_longitude=-75.,central_latitude=10.,standard_parallels=(30.,30.))
# ax= plt.axes(projection=proj)
# ax.set_extent([-90.,-40.,5.,23.])
# ax.add_feature(cf.LAKES,color='white')
# ax.add_feature(cf.OCEAN,color='white')
# ax.add_feature(cf.STATES,edgecolor='grey')
# ax.add_feature(cf.BORDERS,edgecolor='grey')
# ax.add_feature(cf.COASTLINE,edgecolor='grey')
# ax.add_feature(cf.LAND,color='papayawhip')
# ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=False,linewidth=1,color='white',alpha=0.5,linestyle='dashed')


# plt.contourf(lons74,lats74,sss74, cmap='jet',transform=ccrs.PlateCarree())
# plt.colorbar(orientation='horizontal',label='psu')
# plt.title('Ocean Salinity During Hurricane Beryl on 7/4/24')

