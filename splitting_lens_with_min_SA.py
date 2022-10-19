# -*- coding: utf-8 -*-
"""
SPHERICAL ABERRATION: EFFECT OF SPLITTING LENS

Program of designing a lens with minimum SA elements 

@author: Jeff Ching-wen Chan
@Created on Mon Oct 17 15:54:34 2022
"""

# debug = 1/True for debug mode; debug = 0/False for release mode
debug = 1 

if debug == True:
    print(f"The script is running in debug mode. \n")
else:
    print(f"The script is running in release mode. \n")

print("num: # of lens elements ")
print("f:   focal length in mm")
print("n:   refractive index (ex: NBK7 = 1.5168)")

if debug == True:
    system_spec = [3, 100, 1.5168] # NBK7
    # system_spec = [3, 100, 1.8830] # LAH58
else:
    system_spec = input("\n Enter num, f, and n: \n (Ex: 3 100 1.5168)\n      ").split()

num = int(system_spec[0])  # Number of lens elements
f = float(system_spec[1])  # Focal length in mm
n = float(system_spec[2])  # Glass material

print(f"\n You enter the system spec: num={num}, f={f}, n={n} ")
print("\n------------------------------")
print(f"Design table for {num} element lens system with minimum SA ")
print("------------------------------")

print("System Power\n")
power_sys = 1/f   # System power 
power = []          # power of each element 
for i in range(0,num):
    power.append(power_sys/num)
    print(f"L{i+1}_power = {power[i]}")
print("------------------------------")

"""Step1: Calculate paraxial marginal ray slopes"""
print("Paraxial Marginal Ray Slopes\n")
h = 1 # Assume the margianl ray heigth in the object space is 1mm
u = []
u_tilt = []
u.append(0) # Object is located at infinity
for i in range(0,num):
    u_tilt.append(u[i]-h*power[i])
    u.append(u_tilt[i])
    print(f"u{i+1}  = {u[i]}")
    print(f"u{i+1}' = {u_tilt[i]}")
u.remove(u[-1])
print("------------------------------")

"""Step2: Calculate conjugate factors"""
print("Conjugate Factors\n")
c = []
for i in range(0,num):
    c.append((u[i]+u_tilt[i])/(u[i]-u_tilt[i]))
    print(f"C{i+1} = {c[i]}")
print("------------------------------")

"""Step3: Calculate the optimum shape factors"""
print("Optimum Shape Factors\n")
b_opt = []
for i in range(0,num):
    b_opt.append(-2*(n**2-1)*c[i]/(n+2))
    print(f"B{i+1}_opt = {b_opt[i]}")
print("------------------------------")

"""Step4: Calculate radius of surfaces"""
print("Radius of Surfaces\n")
r = []
for i in range(0,num):
    r.append(2*(n-1)/(power[i]*(b_opt[i]+1)))
    print(f"R{2*i+1} = {r[2*i]}")
    r.append(2*(n-1)/(power[i]*(b_opt[i]-1)))
    print(f"R{2*i+2} = {r[2*i+1]}")

print("------------------------------")
print("CodeV Command:\n")
print("LEN NEW")
if n == 1.5168:
    glass_material = str('NBK7')
elif n == 1.883:
    glass_material = str('LAH58')
else:
    glass_material = str(n)

for i in range(0,num):
    print(f"INS S{2*i+1}")
    print(f"RDY S{2*i+1} {r[2*i]:4g}")
    print(f"GL1 S{2*i+1} {glass_material}")
    print(f"INS S{2*i+2}")
    print(f"RDY S{2*i+2} {r[2*i+1]:4g}")

# Set STOP surface
print()
print(f"STO S1")
print(f"DEL S{int(2*num+1)}")
print()

"""Add theickness and 0.5mm air spacing"""

for i in range(0,num):
    print(f"THI S{2*i+1} 2") # Lens thickness
    print(f"THI S{2*i+2} 0.5") # Air spacing
print("PIM")
print("------------------------------")
#  Show lens layout
print("Show Lens Layout:\n")
f_number = 5
sys_dimension = str("MM") # in MM or IN
layout_scale = 0
num_of_rays = 7
print(f"FNO {f_number};DIM MM;YAN 0;VIE;RAT DEF;FAN 0 {num_of_rays};SSI {layout_scale};GO")

print("------------------------------")
#  Set Y Angle Field
print("Set Y Angle Field (FOV: 0, 1, and 2 degs):\n")
print(f"FNO {f_number};DIM MM;YAN 0 1 2;VIE;RAT DEF;FAN 0 {num_of_rays};SSI {layout_scale};GO")

print("------------------------------")
# Plot Third Orders Aberrations Chart
print("Plot Third Orders Aberrations Chart:\n")
print("in cv_macro:PlotTho.seq  SO..I")

print("------------------------------")
# Use Radii as variables to constrain EFL to [?]mm
print(f"Use Radii as variables to constrain EFL to {f:g}mm :\n")
for i in range(0,num):
    print(f"CCY S{2*i+1} 0")
    print(f"CCY S{2*i+2} 0")
print("aut;efl=100;go")

print("------------------------------")
print("End of the design table")
print("------------------------------\n\n\n")

print("Calcualte Error Function")
if debug == True:
    rms = [0.005, 0.011, 0.029] 
else:
    rms = input(" Enter RMS_i: \n (RMS_i is the spot diameter at i [deg] of object field angle.) \n (Ex: 0.005 0.011 0.029)\n      ").split()

rms_sum = 0
for j in range(0,len(rms)):
    rms_sum = rms_sum + float(rms[j])**2
erf = rms_sum**0.5
print(f"\n ERF = {erf:.6g} [mm]")

