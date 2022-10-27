#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

OPTI 574 Homework 6

Created on Wed Oct 26 22:37:07 2022
@author: cwchan
"""
import numpy as np
from matplotlib import pyplot as plt

w = 640                 # wavelength in nm
n = 1.5                 # mean index
n_delta = 0.05          # maximum index modulation
theta = np.deg2rad(10)  # angle of incidence
phi = np.deg2rad(90)    # slant angle
d = 10000               # thickness in nm
# d = np.arange(10000,20000+100,100)


c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k# grating period  

c_S = np.cos(theta)-k*np.cos(phi)/beta
angle_of_output_ray_s = np.rad2deg(np.arccos(c_S))

v = np.pi*n_delta*d/(w*np.sqrt(c_R*c_S))

"""problem 1-d"""
theta_delta = np.deg2rad(np.arange(5,16,0.1))
xi = theta_delta*k*d*np.sin(phi-theta)/(2*c_S)
eta = np.sin(np.sqrt(v**2+xi**2))**2/(1+(xi**2/v**2))

plt.figure(dpi=300)
plt.plot(np.rad2deg(theta_delta),eta,'ro')
plt.title('The Efficiency vs. Angle of Incidence')
plt.xlabel('Angle of Incidence θ (deg)')
plt.ylabel('Efficiency η ')
plt.legend(['η'])
plt.xlim(5,15)
plt.xticks(np.arange(5,16,1))
plt.grid()

#%%
"""problem 1-c"""
w_delta = np.arange(620,661,1)
xi = -w_delta*k**2*d/(8*np.pi*n*c_S)
eta = np.sin(np.sqrt(v**2+xi**2))**2/(1+(xi**2/v**2))

plt.figure(dpi=300)
plt.plot(w_delta,eta,'-gs')
plt.title('The Efficiency vs. Wavelength')
plt.xlabel('Wavelength λ (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η'])
plt.xlim(620,660)
plt.xticks(np.arange(620,665,5))
plt.grid()


#%%
"""problem 1-b"""
xi = 0
eta = np.sin(np.sqrt(v**2+xi**2))**2/(1+(xi**2/v**2))

plt.figure(dpi=300)
plt.plot(d,eta)
plt.title('The Efficiency vs. Thickness')
plt.xlabel('Thickness d (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η'])
# plt.xlim((350,850))
# plt.xticks(np.linspace(350,850,11))
# plt.ylim(((0,1)))
plt.grid()

#%%
xi_angle = 
xi_wavelength = 

