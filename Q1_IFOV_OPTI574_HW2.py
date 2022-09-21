# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 00:40:59 2022
@Homework2 (OPTI 574)
@author: cwchan
"""

import numpy as np
import matplotlib.pyplot as plt

f1 = 3 # mm
f2 = -1000 # mm
t = 25 # mm (Distance to negative lens) 
t = np.arange(10, 51 ,1)
n = 1 # refractive index in Air

power1 = 1/f1
power2 = 1/f2
tau = t/n
power_total = power1 + power2 + power1*power2*tau
f_total = 1/power_total

d_front = (power2/power_total)*t
d_rear = (power1/power_total)*t

s_object = -f1 - d_front
s_image = f_total*s_object/(f_total+s_object)

# (a) Magnification
m = s_image/s_object

# (b) Virtual image size
display_pixels = 4*10**-3 # mm
display_h = 1920*display_pixels
display_v = 1080*display_pixels

virtaul_image_h = m * display_h
virtual_image_v = m * display_v

plt.figure(dpi=300,figsize=(4,4))
plt.plot(t,f_total,'r')
plt.title('Focal length vs Distance to negative lens')
plt.xlabel('t (mm)')
plt.xlim([max(t),min(t)])
plt.ylabel('system focal length (mm)')
plt.grid()

plt.figure(dpi=300,figsize=(4,4))
plt.plot(t, m,'m')
plt.title('Magnification vs Distance to negative lens')
plt.xlabel('t (mm)')
plt.xlim([max(t),min(t)])
plt.ylabel('m')
plt.grid()

plt.figure(dpi=300,figsize=(4,4))
plt.plot(t, virtaul_image_h,'g')
plt.title('Virtual Image Height vs Distance to negative lens')
plt.xlabel('t (mm)')
plt.xlim([max(t),min(t)])
plt.ylabel('virtual image height (mm)')
plt.grid()

plt.figure(dpi=300,figsize=(4,4))
plt.plot(t, s_image,'deepskyblue')
plt.title("s' vs t")
plt.xlabel('t (mm)')
plt.xlim([40,min(t)])
plt.ylabel('The distance to the resulting image (mm)')
plt.ylim([max(s_image),min(s_image)])
plt.grid()


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
