"""

# =============================================================================
# Diffraction Grating k-space analysis tool
# =============================================================================

OPTI 574 Physical Optics Modeling 
Homework #3 
Due: 2022/10/04
Instructor: Dr. Eric Fest (Optical Scientist at Meta Inc.)
@author: Jeff Ching-wen Chan
@studentID: 23550910

"""
#%%
import numpy as np
import matplotlib.pyplot as plt

def set_data_points(fov_x,fov_y,points):
    interval = points - 1
    cx= np.arange(-fov_x/2,fov_x/2+fov_x/interval,fov_x/interval)
    cy = np.arange(-fov_y/2,fov_y/2+fov_y/interval,fov_y/interval)
    x = []
    y = []
    
    for i in range(0,points):
        x.append(cx[i])
        y.append(cy[0])
    for i in range(0,points):
        x.append(cx[-1])
        y.append(cy[i])
    for i in range(0,points):
        x.append(cx[len(cx)-1-i])
        y.append(cy[-1])
    for i in range(0,points):
        x.append(cx[0])
        y.append(cy[len(cy)-1-i])

    return x,y 

def plot_cartesian_space(hfov,vfov,half_fov=15,legend='input',style='s-b'):
    # default axis limit = 30 deg, default legend = 'input'
    plt.figure(dpi=300)
    plt.plot(hfov,vfov,style,markersize='4')
    plt.title('x/y Cartesian space',fontsize='12')
    plt.xlabel('Cartesian x angle (deg)',fontsize='12')
    plt.ylabel('Cartesian y angle (deg)',fontsize='12')
    plt.xlim([-half_fov,half_fov])
    plt.ylim([-half_fov,half_fov])
    plt.legend([str(legend)])
    plt.gca().set_aspect('equal','box')
    

fov_x = 30
fov_y = 18
points = 5

hfov, vfov = set_data_points(fov_x, fov_y, points)
plot_cartesian_space(hfov,vfov,legend = 'input')

#%%
azimuth = 45 # in degree
kx = []
ky = []
for i in range(0,len(hfov)):
    phi = np.deg2rad(azimuth)
    theta_x = np.deg2rad(hfov[i])
    theta_y = np.deg2rad(vfov[i])
    tan_theta_x = np.tan(theta_x)
    tan_theta_y = np.tan(theta_y)
    theta = np.rad2deg(np.arctan(np.sqrt((tan_theta_x**2)+(tan_theta_y**2))))
    if tan_theta_x == 0:
        if tan_theta_y > 0:
            phi = 90
        else: 
            phi = -90
    else:
        phi = np.rad2deg(np.arctan2(tan_theta_y,tan_theta_x))
    # print(f'phi_{i} = {phi}')
    # print(f'theta_{i} = {theta}')
    # print(f'tan_theta_x_{i} = {tan_theta_x}')
    # print(f'tan_theta_y_{i} = {tan_theta_y}')
    kx.append(np.cos(np.deg2rad(phi)) * np.sin(np.deg2rad(theta)))
    ky.append(np.sin(np.deg2rad(phi)) * np.sin(np.deg2rad(theta)))
    
plt.figure(dpi=300)
plt.plot(kx,ky,'s-b',markersize='2')
plt.title('k-space',fontsize='12')
plt.xlabel('kx',fontsize='12')
plt.ylabel('ky',fontsize='12')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend(['input'],loc='upper right')
plt.gca().set_aspect('equal','box')

# plot the circles (waveguide)
for i in range(1,3):
    angle = np.linspace(0, 2*np.pi, 100) 
    radius = i
    a = radius * np.cos(angle) 
    b = radius * np.sin(angle) 
    plt.plot(a,b,'black',linewidth='1')


#%%

fov_x = 30
fov_y = 18
points = 5
interval = points - 1
cx = np.arange(-fov_x/2,fov_x/2+fov_x/interval,fov_x/interval)
cy = np.arange(-fov_y/2,fov_y/2+fov_y/interval,fov_y/interval)

x = []
y = []

for i in range(0,points):
    x.append(cx[i])
    y.append(cy[0])
for i in range(0,points):
    x.append(cx[-1])
    y.append(cy[i])
for i in range(0,points):
    x.append(cx[len(cx)-1-i])
    y.append(cy[-1])
for i in range(0,points):
    x.append(cx[0])
    y.append(cy[len(cy)-1-i])


plt.figure(dpi=300)
plt.plot(x,y,'s-r')

plt.title('x/y Cartesian space')
plt.xlabel('Cartesian x angle (deg)')
plt.ylabel('Cartesian y angle (deg)')
plt.xlim([-15,15])
plt.ylim([-15,15])
plt.legend(['input'])
plt.gca().set_aspect('equal', adjustable='box')

#%%


x = [-15,-7.5,0,7.5,15]
x_right = [15,15,15,15,15]
x_left = [-x for x in x_right]

y = [-9,-4.5,0,4.5,9]
y_top = [9,9,9,9,9]
y_buttom = [-x for x in y_top]
# c = [-9,-4.5,0,4.5,9]
# b = [-15,-15,-15,-15,-15]
# c = [15,15,15,15,15]
plt.figure(dpi=300)
plt.plot(x,y_top,'s-r')
plt.plot(x,y_buttom,'s-r')
plt.plot(x_right,y,'s-r')
plt.plot(x_left,y,'s-r')
plt.title('x/y Cartesian space')
plt.xlabel('Cartesian x angle (deg)')
plt.ylabel('Cartesian y angle (deg)')
plt.xlim([-15,15])
plt.ylim([-15,15])
plt.legend('input')
plt.gca().set_aspect('equal', adjustable='box')

#%%

x = 30
y = 18
pts = 5 

interval = pts-1
cx = np.arange(-x/2,x/2+x/interval,x/interval)
cy = np.arange(-y/2,y/2+y/interval,y/interval)


edge_of_space = []
for i, j in zip(range(0,len(cx)),range(0,len(cy))):
    edge_of_space.append([cx[0],cy[j]])

plt.plot(edge_of_space[0],edge_of_space[1])

#%%
def set_data_points(x,y,pts):
    interval = pts-1
    cx = np.arange(-x/2,x/2+x/interval,x/interval)
    cy = np.arange(-y/2,y/2+y/interval,y/interval)
    
    edge_of_space = []
    for i in cx:
        edge_of_space.append(cx[i])
    
    return cx,cy,edge_of_space

cartesian_x, cattesian_y,edge_of_space = set_data_points(30,18,5)


#%%

def cartesian_to_k_space(elevation_x, elevation_y, azimuth, number_of_points=5):
    theta_x = np.arange(-elevation_x/2, elevation_x/2, (elevation_x/number_of_points))
    theta_y = np.arange(-elevation_y/2, elevation_y/2, elevation_y/number_of_points)
    phi = azimuth
    kx = np.cos(phi) * np.sin(theta_x)
    ky = np.sin(phi) * np.cos(theta_y)
    return theta_x, theta_y, kx, ky
    
rotation_angle = -90
fov_x = 30
fov_y = 18



theta_x, theta_y, kx, ky = cartesian_to_k_space(fov_x, fov_y, rotation_angle)

plt.figure(dpi=300)
plt.plot(theta_x, theta_y ,'r')
plt.plot(kx,ky,'blue')
plt.title('x/y Cartesian space')
plt.xlabel('Cartesian x angle (deg)')
plt.ylabel('Cartesian y angle (deg)')

# plt.figure(dpi=300,figsize=(4,4))
# plt.plot(t,f_total,'r')
# plt.title('Focal length vs Distance to negative lens')
# plt.xlabel('t (mm)')
# plt.xlim([max(t),min(t)])
# plt.ylabel('system focal length (mm)')
# plt.grid()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:18:27 2022

@author: cwchan
"""

