# -*- coding: utf-8 -*-
"""
THREE ELEMENT LENS DESIGN

Design a three element lens system for which spherical aberration is 
individually minimized at each of the element.

System requirement:
    F/number:5
    f = 100 mm
    Wavelength:587 nm (d-line)
    FOV: 0, 1, and 2 degs
    Object: at infinity
    Glass material: NBK7
    # of lens elements = 3

@author: Jeff Ching-wen Chan
@Created on Mon Oct 17 13:06:30 2022
"""

#%% Step by step
n = 1.5168  # Glass material = NBK7
f = 100     # Focal length in mm
power_sys = 1/f   # System power 
power_L1 = power_sys/3
power_L2 = power_sys/3
power_L3 = power_sys/3

# =============================================================================
# Step1: Calculate paraxial marginal ray slopes, u1, u1',u2, u2', u3, and u3'. 
# Assume the margianl ray heigth in the object space is 1mm. 
# =============================================================================
h1 = 1
u1 = 0
u1_tilt = u1-h1*power_L1
u2 = u1_tilt
u2_tilt = u2-h1*power_L2
u3 = u2_tilt
u3_tilt = u3-h1*power_L3

# =============================================================================
# Step2: Calculate conjugate factors C1, C2, and C3 for Lens #1, #2, and #3.
# =============================================================================
c1 = (u1+u1_tilt)/(u1-u1_tilt)
c2 = (u2+u2_tilt)/(u2-u2_tilt)
c3 = (u3+u3_tilt)/(u3-u3_tilt)

# =============================================================================
# Step3: Calculate the optimum shape factor b1_opt, b2_opt, and b3_opt
# =============================================================================
b1_opt = -2*(n**2-1)*c1/(n+2)
b2_opt = -2*(n**2-1)*c2/(n+2)
b3_opt = -2*(n**2-1)*c3/(n+2)

# =============================================================================
# Step4: Based on optimum value and refractive index, calculate r1, r2, r3, and r4 by using the procedure for singlet.
# =============================================================================
r1 = 2*(n-1)/(power_L1*(b1_opt+1))
r2 = 2*(n-1)/(power_L1*(b1_opt-1))
r3 = 2*(n-1)/(power_L2*(b2_opt+1))
r4 = 2*(n-1)/(power_L2*(b2_opt-1))
r5 = 2*(n-1)/(power_L3*(b3_opt+1))
r6 = 2*(n-1)/(power_L3*(b3_opt-1))




#%% Calculator
n = 1.5168  # Glass material = NBK7
f = 100    # Focal length in mm
number_of_element = 3

power_sys = 1/f   # System power 
phi = []          # power of each element       
for i in range(0,number_of_element):
    phi.append(power_sys/number_of_element)

"""Step1: Calculate paraxial marginal ray slopes"""
h = 1 # Assume the margianl ray heigth in the object space is 1mm
u = []
u_tilt = []
u.append(0) # Object is located at infinity
for i in range(0,number_of_element):
    u_tilt.append(u[i]-h*phi[i])
    u.append(u_tilt[i])
u.remove(u[-1])

"""Step2: Calculate conjugate factors"""
c = []
for i in range(0,number_of_element):
    c.append((u[i]+u_tilt[i])/(u[i]-u_tilt[i]))

"""Step3: Calculate the optimum shape factors"""
b_opt = []
for i in range(0,number_of_element):
    b_opt.append(-2*(n**2-1)*c[i]/(n+2))

"""Step4: Calculate radius of surfaces"""
r = []
for i in range(0,number_of_element):
    r.append(2*(n-1)/(phi[i]*(b_opt[i]+1)))
    r.append(2*(n-1)/(phi[i]*(b_opt[i]-1)))

