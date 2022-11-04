#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 17:26:55 2022

@author: cwchan
"""
import numpy as np
from matplotlib import pyplot as plt

A_bin = 26.6666*16.6666
A_pupil =np.pi*(2/2)**2
E_IG = 9 # (V/m)**2
d = 101
x = 26.667
y = 16.667

theta_x = np.deg2rad(32)
theta_y = np.deg2rad(18)


E = 5.5925E-07

pupil_efficiency = (E/E_IG)*(A_bin/A_pupil)

projected_solid_angle = 2*(np.sin(theta_x/2)*np.arctan(np.tan(theta_y/2)*np.cos(theta_x/2)) + np.sin(theta_y/2)*np.arctan(np.tan(theta_x/2)*np.cos(theta_y/2)))

nits_per_lumen = pupil_efficiency/(A_pupil * projected_solid_angle)


#%%
d = 101
x = 26.667
y = 16.667
theta_x1 = np.degrees(np.arctan(-x/d))
theta_x2 = np.degrees(np.arctan(0/d))
theta_x3 = np.degrees(np.arctan(x/d))
theta_y1 = np.degrees(np.arctan(-y/d))
theta_y2 = np.degrees(np.arctan(0/d))
theta_y3 = np.degrees(np.arctan(y/d))


#%%
A_bin = 26.6666*16.6666
A_pupil =np.pi*(2/2)**2
E_IG = 9 # (V/m)**2

E = 5.5925E-07

pupil_efficiency = (E/E_IG)*(A_bin/A_pupil)
