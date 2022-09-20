# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:40:59 2022
@Homework2 (OPTI 574)
@author: cwchan
"""

import numpy as np
import matplotlib.pyplot as plt
#%% number of pixels vs IFOV
ifov = np.linspace(1,4.5,36)
n_pixels = 30/(ifov/60)
plt.figure(dpi=300,figsize=(5,5))
plt.plot(ifov,n_pixels,'k')
plt.title('The number of horizontal/vertical pixels vs IFOV')
plt.xlabel('Angular Resolution (arc minutes)')
plt.ylabel('number of pixels')
plt.xlim([1,4.5])
plt.xticks([1,2,3,4])
plt.grid()
plt.legend(['number of pixels'])

#%% Calculate 1920x1080 Full High Detinition Resolution
ifov_H = 1800/1920 # in degrees
ifov_V = 1800/1080 # in degrees


#%% focal length vs IFOV
p = 4*10**-3  # Pixel size in mm

ifov = np.linspace(1,4.5,36)
f = p/np.tan(np.deg2rad(ifov/60))
plt.figure(dpi=300,figsize=(5,5))
plt.plot(ifov,f,'g')
plt.title('focal length vs IFOV')
plt.xlabel('Angular Resolution (arc minutes)')
plt.ylabel('focal length (mm)')
plt.xlim([1,4.5])
plt.ylim([1,15])
plt.xticks([1,2,3,4])
plt.grid()
plt.legend(['focal length'])


#%% f/# vs IFOV
p = 4*10**-3  # Pixel size in mm
d = 3 # Pupil Diameter in mm

ifov = np.linspace(1,4.5,36)
f = p/np.tan(np.deg2rad(ifov/60))
fnumber = f/d
plt.figure(dpi=300,figsize=(5,5))
plt.plot(ifov,fnumber,'r')
plt.title('f/# vs IFOV')
plt.xlabel('Angular Resolution (arc minutes)')
plt.ylabel('f/#')
plt.xlim([1,4.5])
plt.ylim([0,5])
plt.xticks([1,2,3,4])
plt.yticks(np.linspace(0,5,11))
plt.grid()
plt.legend(['f/#'])


#%% Collection Efficiency vs IFOV
p = 4*10**-3  # Pixel size in mm
d = 3 # Pupil Diameter in mm
b = 0 # Lambertian emitters

ifov = np.linspace(1,4.5,36)
f = p/np.tan(np.deg2rad(ifov/60))
fnumber = f/d
collection_angle = np.arcsin(1/(2*fnumber))
collection_efficiency = 1-np.cos(collection_angle)**(b+2)
plt.figure(dpi=300,figsize=(5,5))
plt.plot(ifov,collection_efficiency,'b')
plt.title('Collection Efficiency vs IFOV')
plt.xlabel('Angular Resolution (arc minutes)')
plt.ylabel('collection efficiency (fractional)')
plt.xlim([1,4.5])
plt.xticks([1,2,3,4])
plt.ylim([0,0.3])
plt.grid()
plt.legend(['collection efficiency'])

#%%

#%%
# fov_degree = np.linspace(0,30,31)

d = 3 # Pupil Diameter in mm
p = 4*10**-3  # Pixel size in mm
fov = np.deg2rad(30) # FOV 30 deg
f = d/(2*np.sin(fov)) # focal length in mm
fnumber = f/d 
ifov = np.arctan(p/f) 

plt.plot(fov,ifov)

#%%

plt.figure(dpi=300)
plt.plot(x, mtf_500um)
plt.title('')
plt.xlabel('Line Density X (cycles/mm)')
plt.ylabel('MTF (normalized)')
plt.grid()

#%%




