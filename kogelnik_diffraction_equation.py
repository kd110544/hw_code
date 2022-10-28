#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

OPTI 574 Homework 6

Created on Wed Oct 26 22:37:07 2022
@author: cwchan
"""
import numpy as np
from matplotlib import pyplot as plt
import cmath
#%%
"""problem 2-d stacked plot"""
w = 640                 # wavelength in nm
n = 1.5                 # mean index
n_delta = 0.05          # maximum index modulation
theta = np.deg2rad(10)  # angle of incidence
d = 10000               # thickness in nm

# Variable
theta_range = np.deg2rad(np.arange(5,15.1,0.1))
theta_delta = theta-theta_range

# for lossless transmission grating 
phi = np.deg2rad(90)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
print(f"Transmission grating period Λ = {period:.3f} nm")
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_tranmission = c_S

v = (np.pi * n_delta * d) / (w * np.sqrt( c_R * c_S ))
xi = (theta_delta * k * d * np.sin(phi-theta)) / (2*c_S)
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

# for lossless reflection grating
phi = np.deg2rad(0)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
print(f"Reflection grating period Λ = {period:.3f} nm")
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_refelction = c_S

eta_real = []
for theta_single in theta_delta:  
    V = np.real(1j*(np.pi * n_delta * d) / (w * cmath.sqrt( c_R * c_S )))
    XI = (theta_single * k * d * np.sin(phi-theta)) / (2*c_S)
    ETA = 1/( 1+((1-XI**2/V**2)/(np.sinh(np.sqrt(V**2-XI**2))**2)) )
    eta_real.append(ETA)


plt.figure(dpi=300)
plt.plot(np.rad2deg(theta_range),eta,'-bo')
plt.plot(np.rad2deg(theta_range),eta_real,'-ro')
plt.title(f'The Efficiency vs. Angle of Incidence\n(d={d}nm, λ={w}nm)')
plt.xlabel('Angle of Incidence θ (deg)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating','η_reflection grating'],loc='best')
plt.xlim(5,15)
plt.xticks(np.arange(5,16,1))
plt.grid()

angle_s_transmission = np.rad2deg(np.arccos(c_S_tranmission))
angle_s_reflection = np.rad2deg(np.arccos(c_S_refelction))
print(f"Angle of the output ray s relative to the surface normal is:\n{angle_s_transmission:.2f} (transmission)\n{angle_s_reflection:.2f} (reflection)")



#%%
"""problem 2-c stacked plot"""
w = 640                 # wavelength in nm
n = 1.5                 # mean index
n_delta = 0.05          # maximum index modulation
theta = np.deg2rad(10)  # angle of incidence
d = 10000               # thickness in nm

# Variable
w_range = np.arange(620,660.5,0.5)
w_delta = w-w_range

# for lossless transmission grating 
phi = np.deg2rad(90)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_tranmission = c_S
v = (np.pi * n_delta * d) / (w * np.sqrt( c_R * c_S ))
xi = (-w_delta * k**2 * d) / (8 * np.pi * n * c_S)
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

# for lossless reflection grating
phi = np.deg2rad(0)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_refelction = c_S
eta_real = []
for w_single in w_delta:  
    V = np.real(1j*(np.pi * n_delta * d) / (w * cmath.sqrt( c_R * c_S )))
    XI = (-w_single * k**2 * d) / (8 * np.pi * n * c_S)
    ETA = 1/( 1+((1-XI**2/V**2)/(np.real(cmath.sinh(cmath.sqrt(V**2-XI**2))**2))) )
    eta_real.append(ETA)

plt.figure(dpi=300)
plt.plot(w_range,eta,'-bo')
plt.plot(w_range,eta_real,'-ro')
plt.title(f'The Efficiency vs. Wavelength (d={d}nm)')
plt.xlabel('Wavelength λ (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating','η_reflection grating'],loc='best')
plt.xlim(620,660)
plt.xticks(np.arange(620,665,5))
plt.grid()

#%%
"""problem 2-b stacked plot"""

w = 640                 # wavelength in nm
n = 1.5                 # mean index
n_delta = 0.05          # maximum index modulation
theta = np.deg2rad(10)  # angle of incidence

# Variable
d = np.arange(10000,20000+200,200)

# for lossless transmission grating 
phi = np.deg2rad(90)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_tranmission = c_S
v = (np.pi * n_delta * d) / (w * np.sqrt( c_R * c_S ))
xi = 0
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

# for lossless reflection grating
phi = np.deg2rad(0)
c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k
c_S = np.cos(theta)-k*np.cos(phi)/beta
c_S_refelction = c_S
eta_real = []
for D in d:
    V = np.real(1j*(np.pi * n_delta * D) / (w * cmath.sqrt( c_R * c_S )))
    XI = 0
    ETA = 1/( 1+((1-XI**2/V**2)/(np.sinh(np.sqrt(V**2-XI**2))**2)) )
    eta_real.append(ETA)

plt.figure(dpi=300)
plt.plot(d,eta,'-bo')
plt.plot(d,eta_real,'-ro')
plt.title(f'The Efficiency vs. Thickness (λ={w}nm)')
plt.xlabel('Thickness d (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating','η_reflection grating'])
plt.xlim((10000,20000))
plt.grid()


#%% Problem 1
import numpy as np
from matplotlib import pyplot as plt

w = 640                 # wavelength in nm
n = 1.5                 # mean index
n_delta = 0.05          # maximum index modulation
theta = np.deg2rad(10)  # angle of incidence
phi = np.deg2rad(90)    # slant angle
d = 10000               # thickness in nm

c_R = np.cos(theta)
beta = 2*np.pi*n/w
k = 2*beta*np.cos(phi-theta)
period = 2*np.pi/k      # grating period  

c_S = np.cos(theta)-k*np.cos(phi)/beta
angle_of_output_ray_s = np.rad2deg(np.arccos(c_S))

v = (np.pi * n_delta * d) / (w * np.sqrt( c_R * c_S ))


"""problem 1-d"""
theta_range = np.deg2rad(np.arange(5,16,0.1))
theta_delta = theta-theta_range
xi = (theta_delta * k * d * np.sin(phi-theta)) / (2*c_S)
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

plt.figure(dpi=300)
plt.plot(np.rad2deg(theta_range),eta,'-bo')
plt.title(f'The Efficiency vs. Angle of Incidence\n(d={d}nm, λ={w}nm)')
plt.xlabel('Angle of Incidence θ (deg)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating'])
plt.xlim(5,15)
plt.xticks(np.arange(5,16,1))
plt.grid()

#%%
"""problem 1-c"""
w_range = np.arange(620,661,1)
w_delta = w-w_range
xi = (-w_delta * k**2 * d) / (8 * np.pi * n * c_S)
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

plt.figure(dpi=300)
plt.plot(w_range,eta,'-bo')
plt.title(f'The Efficiency vs. Wavelength (d={d}nm)')
plt.xlabel('Wavelength λ (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating'])
plt.xlim(620,660)
plt.xticks(np.arange(620,665,5))
plt.grid()


#%%
"""problem 1-b"""
d = np.arange(10000,20000+200,200)
v = (np.pi * n_delta * d) / (w * np.sqrt( c_R * c_S ))
xi = 0
eta = (np.sin(np.sqrt(v**2+xi**2))**2) / (1 + (xi**2 / v**2))

plt.figure(dpi=300)
plt.plot(d,eta,'-bo')
plt.title(f'The Efficiency vs. Thickness (λ={w}nm)')
plt.xlabel('Thickness d (nm)')
plt.ylabel('Efficiency η ')
plt.legend(['η_transmission grating'])
plt.xlim((10000,20000))
plt.grid()
