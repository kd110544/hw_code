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

import numpy as np
import matplotlib.pyplot as plt

# Input system spec here
fov_x = 24 # in degree
fov_y = 18 # in degree
points = 9 # number of points at each side
substrate_index = 1.8
max_angle_allowed_inside_waveguide = np.deg2rad(80)
wavelength = 532 # in nm

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

def point_removal_check(kx,ky):
    kx_chopped = []
    ky_chopped = []
    for i in range(0,len(kx)):
        if kx[i]**2 + ky[i] **2 >= 1:
            kx_chopped.append(kx[i])
            ky_chopped.append(ky[i])
        else: 
            pass
    return kx_chopped,ky_chopped
    
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
    

# get x/y Cartesian data points
hfov, vfov = set_data_points(fov_x, fov_y, points)

# Convert x/y Cartesian data points into k-space
kx,ky = cartesian_to_k_space(hfov, vfov)

## IG (Iput grating vector)
kx_after_IG, ky_after_IG = model_the_grating(kx, ky, m=1, lambda_grating=wavelength, pitch=380, rotation_angle=-90)
kx_after_IG, ky_after_IG = point_removal_check(kx_after_IG, ky_after_IG)

## EG (Expansion grating vector)
kx_after_EG, ky_after_EG = model_the_grating(kx_after_IG, ky_after_IG, m=1, lambda_grating=wavelength, pitch=268.7, rotation_angle=45)
kx_after_EG, ky_after_EG = point_removal_check(kx_after_EG, ky_after_EG)

## OG (Output grating vector)
kx_after_OG, ky_after_OG = model_the_grating(kx_after_EG, ky_after_EG, m=1, lambda_grating=wavelength, pitch=380, rotation_angle=-180)

## k-space to cartesian
hfov_after_OG, vfov_after_OG = k_space_to_cartesian(kx_after_OG,ky_after_OG)

# =============================================================================
# plot #1 setting
# =============================================================================
plt.figure(dpi=600)
plt_cartesian_space(hfov,vfov,style='s-b')
plt_cartesian_space(hfov_after_OG,vfov_after_OG,style='s-r')
plt_cartesian_space(hfov_after_OG,vfov_after_OG,style='s-r')
plt.legend(['input','output'],loc='upper right',fontsize=9)

# =============================================================================
#  plot #2 setting
# =============================================================================
plt.figure(dpi=600)
# plot grating vector
plt.plot(kx,ky,'s-b',markersize='2')
plt.plot(kx_after_IG,ky_after_IG,'s-y',markersize='2')
plt.plot(kx_after_EG,ky_after_EG,'s-g',markersize='2')
plt.plot(kx_after_OG,ky_after_OG,'s-r',markersize='2')
# plot inner TIR limit circle
plt_circle(radius = 1)
# plot outer limit circle
plt_circle(radius = substrate_index * np.sin(max_angle_allowed_inside_waveguide))
plt.title(f'k-space (λ={wavelength}nm)',fontsize='12')
plt.xlabel('kx',fontsize='12')
plt.ylabel('ky',fontsize='12')
plt.xticks(np.arange(-2,2+.5,.5),fontsize='8')
plt.yticks(np.arange(-2,2+.5,.5),fontsize='8')
plt.xlim([-2,2])
plt.ylim([-2,2])
plt.legend(['input','after IG','after EG','after OG','inner TIR limit','outer limit'],loc='upper right',fontsize=6)
plt.gca().set_aspect('equal','box')
