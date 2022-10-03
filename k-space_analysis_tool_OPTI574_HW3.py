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

def cartesian_to_k_space(hfov,vfov):
    kx = []
    ky = []
    for i in range(0,len(hfov)):
        # Define θ (theta)
        theta_x = np.deg2rad(hfov[i])
        theta_y = np.deg2rad(vfov[i])
        tan_theta_x = np.tan(theta_x)
        tan_theta_y = np.tan(theta_y)
        theta = np.rad2deg(np.arctan(np.sqrt((tan_theta_x**2)+(tan_theta_y**2))))
        # Define φ (phi)
        if tan_theta_x == 0:
            if tan_theta_y > 0:
                phi = 90
            else: 
                phi = -90
        else:
            phi = np.rad2deg(np.arctan2(tan_theta_y,tan_theta_x))
        # Convert to kx & ky
        kx.append(np.cos(np.deg2rad(phi)) * np.sin(np.deg2rad(theta)))
        ky.append(np.sin(np.deg2rad(phi)) * np.sin(np.deg2rad(theta)))
    
    return kx,ky

def k_space_to_cartesian(kx,ky):
    kz = []
    hfov = []
    vfov = []
    for i in range(0,len(kx_after_OG)):
        # Define kz 
        kz.append(np.sqrt(1-kx_after_OG[i]**2-ky_after_OG[i]**2))
        hfov.append(np.rad2deg(np.arctan2(kx[i],kz[i])))
        vfov.append(np.rad2deg(np.arctan2(ky[i],kz[i])))
    
    return hfov,vfov

def model_the_grating(kx, ky, m, lambda_grating, pitch, rotation_angle):
    m = m # diffacted order
    lambda_grating = lambda_grating # in nm
    pitch = pitch # in nm (input grating)
    rotation_angle = np.deg2rad(rotation_angle)
    kx_unit_vector = 1
    ky_unit_vector = 1
    k1_x = (m*lambda_grating/pitch)*(np.cos(rotation_angle)*kx_unit_vector)
    k1_y = (m*lambda_grating/pitch)*(np.sin(rotation_angle)*ky_unit_vector)
    
    kx_after_grating = []
    ky_after_grating = []
    for i in range(0,len(kx)):
        kx_after_grating.append(kx[i]+k1_x)
        ky_after_grating.append(ky[i]+k1_y)
    
    return kx_after_grating, ky_after_grating
  
def plt_cartesian_space(hfov,vfov,half_fov=15,style='s-b'):
    # default axis limit = 30 deg, default legend = 'input'
    plt.plot(hfov,vfov,style,markersize='4')
    plt.title('x/y Cartesian space',fontsize='12')
    plt.xlabel('Cartesian x angle (deg)',fontsize='12')
    plt.ylabel('Cartesian y angle (deg)',fontsize='12')
    plt.xlim([-half_fov,half_fov])
    plt.ylim([-half_fov,half_fov])
    plt.gca().set_aspect('equal','box')
    
def plt_circle(radius=1):
    radius = radius # radius = 1 in air
    angle = np.linspace(0, 2*np.pi, 100) 
    a = radius * np.cos(angle) 
    b = radius * np.sin(angle) 
    plt.plot(a,b,linewidth='1')
    

# Input system spec here
fov_x = 30
fov_y = 18
points = 5
substrate_index = 2
max_angle_allowed_inside_waveguide = np.deg2rad(80)

# get x/y Cartesian data points
hfov, vfov = set_data_points(fov_x, fov_y, points)

# make a figure
plt.figure(dpi=600)

# Convert x/y Cartesian data points into k-space
kx,ky = cartesian_to_k_space(hfov, vfov)
plt.plot(kx,ky,'s-b',markersize='2')

## IG (Iput grating vector)
kx_after_IG, ky_after_IG = model_the_grating(kx, ky, m=1, lambda_grating=640, pitch=380, rotation_angle=-90)
## EG (Expansion grating vector)
kx_after_EG, ky_after_EG = model_the_grating(kx_after_IG, ky_after_IG, m=1, lambda_grating=640, pitch=268.7, rotation_angle=45)
## OG (Output grating vector)
kx_after_OG, ky_after_OG = model_the_grating(kx_after_EG, ky_after_EG, m=1, lambda_grating=640, pitch=380, rotation_angle=-180)

## k-space to cartesian
hfov_after_OG, vfov_after_OG = k_space_to_cartesian(kx_after_OG,ky_after_OG)
  
# plot grating vector
plt.plot(kx_after_IG,ky_after_IG,'s-y',markersize='2')
plt.plot(kx_after_EG,ky_after_EG,'s-g',markersize='2')
plt.plot(kx_after_OG,ky_after_OG,'s-r',markersize='2')
# plot inner TIR limit circle
plt_circle()
# plot outer limit circle
plt_circle(radius = substrate_index * np.sin(max_angle_allowed_inside_waveguide))

# =============================================================================
#  plot #2 setting
# =============================================================================
plt.title('k-space',fontsize='12')
plt.xlabel('kx',fontsize='12')
plt.ylabel('ky',fontsize='12')
plt.xticks(np.arange(-2,2+.5,.5),fontsize='8')
plt.yticks(np.arange(-2,2+.5,.5),fontsize='8')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend(['input','after IG','after EG','after OG','inner TIR limit','outer limit'],loc='upper right',fontsize=6)
plt.gca().set_aspect('equal','box')

# =============================================================================
# plot #1 setting
# =============================================================================
plt.figure(dpi=600)
plt_cartesian_space(hfov,vfov,style='s-b')
plt_cartesian_space(hfov_after_OG,vfov_after_OG,style='s-r')
plt.legend(['input','output'])

#%%

"""
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

"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:18:27 2022

@author: cwchan
"""
