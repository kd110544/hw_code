# -*- coding: utf-8 -*-
"""
SPHERICAL ABERRATION: EFFECT OF SPLITTING LENS

Program of designing a lens with minimum SA elements 

@author: Jeff Ching-wen Chan
@Created on Mon Oct 17 15:54:34 2022
"""
print()
print("num: # of lens elements ")
print("f:   focal length in mm")
print("n:   refractive index (ex: NBK7 = 1.5168)")

system_spec = input("\n Enter num, f, and n: \n (Ex: 3 100 1.5168)\n      ").split()
num = int(system_spec[0])
f = float(system_spec[1])  # Focal length in mm
n = float(system_spec[2])  # Glass material

print(f"\n You enter the system spec: num={num}, f={f}, n={n} ")
print("\n------------------------------")
print(f"Design table for {num} element lens system with minimum SA: ")
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
print("End of the design table")
print("------------------------------\n")


