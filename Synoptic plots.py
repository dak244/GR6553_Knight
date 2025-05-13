# -*- coding: utf-8 -*-
"""
Created on Mon May 12 23:17:02 2025

@author: desit
"""


import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
from metpy.units import units
import numpy as np
import xarray as xr



ds = xr.open_dataset('https://thredds.ucar.edu/thredds/dodsC/casestudies/'
                     'harvey/model/gfs_ana/GFS_Global_0p5deg_ana_20170826_0000.grib2').metpy.parse_cf()

#ds = xr.open_dataset('https://thredds.ucar.edu/thredds/dodsC/casestudies/'
#                     'harvey/model/gfs_ana/GFS_Global_0p5deg_ana_20170825_1200.grib2').metpy.parse_cf()


# Set subset slice for the geographic extent of data to limit download
lon_slice = slice(200, 350)
lat_slice = slice(50, 5)

# Grab lat/lon values (GFS will be 1D)
lats = ds.lat.sel(lat=lat_slice).values
lons = ds.lon.sel(lon=lon_slice).values

# Set level to plot/analyze
level = 925 * units.hPa

uwnd_925 = ds['u-component_of_wind_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze().metpy.unit_array
vwnd_925 = ds['v-component_of_wind_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze().metpy.unit_array
mslp= (ds['MSLP_Eta_model_reduction_msl'].metpy.sel(lat=lat_slice, lon=lon_slice).squeeze().metpy.unit_array)/100

rh925=ds['Relative_humidity_isobaric'].metpy.sel(
    vertical=level, lat=lat_slice, lon=lon_slice).squeeze().metpy.unit_array

vtime = ds.time.data[0].astype('datetime64[ms]').astype('O')


# Set output projection
mapcrs = ccrs.LambertConformal(
    central_longitude=-95, central_latitude=25, standard_parallels=(20, 40))

# Set projection of data (so we can transform for the figure)
datacrs = ccrs.PlateCarree()

# Start figure and set extent to be over CONUS
fig = plt.figure(1, figsize=(12,14))
ax = plt.subplot(111, projection=mapcrs)
ax.set_extent([-105, -90, 20, 35], ccrs.PlateCarree())

# Add coastline and state map features
ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
ax.add_feature(cfeature.STATES.with_scale('50m'))

rhvals=np.arange(10,100,5)
cf= ax.contourf(lons,lats,rh925,rhvals, cmap=plt.cm.Greens, transform=datacrs)
cb=plt.colorbar(cf,orientation='horizontal', pad=0.01, aspect=30)
cb.set_label('Relative Humidity (%)',fontsize=16)


mslp_hght = np.arange(950, 1050,4)
cs = ax.contour(lons, lats, mslp, mslp_hght, colors='black',linewidth=1.5, transform=datacrs)
plt.clabel(cs, fmt='%d')


# Plot wind barbs every fifth element
wind_slice = (slice(None, None, 3), slice(None, None, 3))
ax.barbs(lons[wind_slice[0]], lats[wind_slice[1]],
         uwnd_925[wind_slice[0], wind_slice[1]].to('kt').m,
         vwnd_925[wind_slice[0], wind_slice[1]].to('kt').m,
         pivot='middle', color='red', transform=datacrs)

plt.title('Mean Sea level Pressure(mb), 925mb Relative Humidity(%) '
          'and Wind Barbs (kt)\nValid Time: {}'.format(vtime),fontsize=18)


plt.show()











