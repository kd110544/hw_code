# -*- coding: utf-8 -*-
"""
OPTI 574 HW0
Date: 2022/09/06
@author: Jeff Ching-wen Chan
@Student ID: 23550910
"""

#%% HW0-2c
import numpy as np
fnumber = 2
projected_solid_angle_from_Fnumber = np.pi/(4*fnumber**2)
source_flux = 10 # lumens
source_area = 10*1e-6# meters (10mm square)
Lambertian_solid_angle = np.pi
source_luminance = source_flux/(source_area*Lambertian_solid_angle) # nits
illuminance_c = source_luminance * projected_solid_angle_from_Fnumber

#%% HW0-2b
import numpy as np
sun_luminance = 1.6*10**9 # nits = lm/(m^2*sr)
angular_subtense = np.deg2rad(32/60) # 32 arc minutes
sun_solid_angle =  np.pi*(np.sin(angular_subtense/2))**2
illuminance_b = sun_luminance * sun_solid_angle # lux

#%% HW0-2a
import numpy as np
r = 0.025 # diameter = 0.05m
thetac_in_radian = np.arctan(r/2) # radian
# thetac = np.rad2deg(np.arctan(r/2)) # degree
projeted_solid_angle = np.pi*(np.sin(thetac_in_radian))**2
source_flux = 1000 #lumens
source_area = np.pi*r**2
Lambertian_solid_angle = np.pi
source_luminance = source_flux/(source_area*Lambertian_solid_angle) # nits
illuminance_a = source_luminance * projeted_solid_angle * np.cos(0)

#%% HW0-3
import numpy as np
tis = 0.99 # TIS=Total Integrated Scatter, which is the fraction of flux incident on the surface that’s scattered
brdf = tis/np.pi # Bidirectional Reflectance Distribution Function (BRDF)
luminance_a = brdf * illuminance_a
luminance_b = brdf * illuminance_b
luminance_c = brdf * illuminance_c

#%% HW0-4
import numpy as np
import matplotlib.pyplot as plt

d65 = np.loadtxt("d65.txt")
d65wavelength = []
d65flux = []

for i in range(0,len(d65)):
    d65wavelength.append(d65[i][0])
    d65flux.append(d65[i][1])
    
plt.figure(dpi=300)
plt.plot(d65wavelength,d65flux)
plt.title('D65 spectrum')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Flux (Watts/nm)')
plt.xlim((350,850))
plt.xticks(np.linspace(350,850,11))
plt.ylim(((0,1)))
plt.grid()
plt.savefig('q4_D65_Spectrum.png')

cie = np.loadtxt("cie1931xyz.txt")
ciewavelength = []
ciex = []
ciey = []
ciez = []

for j in range(0,len(cie)):
    ciewavelength.append(cie[j][0])
    ciex.append(cie[j][1])
    ciey.append(cie[j][2])
    ciez.append(cie[j][3])

plt.figure(dpi=300)
plt.plot(ciewavelength,ciex)
plt.plot(ciewavelength,ciey)
plt.plot(ciewavelength,ciez)
plt.title('CIE 1931 Tristimulus Curves')
plt.xlabel('Wavelength (nm)')
plt.legend(["x","y","z",])
plt.savefig('q4_Tristimulus_Curves.png')

# correct for d65 range
d65flux_start_from360 = d65flux.copy()
for k in d65flux[0:10]:
    d65flux_start_from360.remove(k)
for l in d65flux[411::]:   
    # print(l) 
    d65flux_start_from360.remove(l)
# correct for cie range
ciewavelength_start_from360nm = ciewavelength.copy()
for n in ciewavelength_start_from360nm[401::]:
    # print(n)
    ciewavelength_start_from360nm.remove(n)
    
X = []
Y = []
Z = []
x = []
y = []

for m in range(0,len(d65flux_start_from360)):
    
    X.append(ciex[m] * d65flux_start_from360[m])
    Y.append(ciey[m] * d65flux_start_from360[m])
    Z.append(ciez[m] * d65flux_start_from360[m])
    x.append(X[m]/(X[m]+Y[m]+Z[m]))
    y.append(Y[m]/(X[m]+Y[m]+Z[m]))

sum_X = sum(X)    
sum_Y = sum(Y)
sum_Z = sum(Z)
sum_all = sum_X+sum_Y+sum_Z

normalized_X = sum_X/sum_Y
normalized_Y = sum_Y/sum_Y
normalized_Z = sum_Z/sum_Y
normalized_sum = normalized_X+normalized_Y+normalized_Z

X_coordinate = normalized_X/normalized_sum
Y_coordinate = normalized_Y/normalized_sum

plt.figure(figsize=(6,5),dpi=300)
plt.plot(x,y,'ro')
plt.plot(X_coordinate,Y_coordinate,"s",color='Black')
white_point_location = 'D65 White Points (' + '{:.2f},'.format(X_coordinate) + '{:.2f})'.format(Y_coordinate) 
plt.annotate(white_point_location,(X_coordinate,Y_coordinate),(X_coordinate-0.1,Y_coordinate-0.06))
plt.title('1931 CIE Chromaticity Diagram')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('q4_CIE_Chromaticity_Diagram.png')
answer_q4 = [normalized_X,normalized_Y,normalized_Z]

print('[X,Y,Z]='+str(answer_q4))

#%%




#%% TODO:



plt.figure(figsize=(6,5),dpi=300)
plt.plot(x,y,'ro')
plt.plot(X_coordinate,Y_coordinate,"s",color='Black')
white_point_location = 'White Points (' + '{:.2f},'.format(X_coordinate) + '{:.2f})'.format(Y_coordinate) 
plt.annotate(white_point_location,(X_coordinate,Y_coordinate),(X_coordinate-0.1,Y_coordinate-0.06))
plt.xlabel('x')
plt.ylabel('y')


#%% HW0-5a
import numpy as np
import matplotlib.pyplot as plt

fwhm = 40
rau = fwhm/2.355
x = np.linspace(360,760,401)
y_red = np.exp(-(x-650)**2/(2*rau**2))
y_green = np.exp(-(x-550)**2/(2*rau**2))
y_blue = np.exp(-(x-450)**2/(2*rau**2))
plt.figure(dpi=300)
plt.plot(x,y_red,'r')
plt.plot(x,y_green,'g')
plt.plot(x,y_blue,'b')
plt.legend(['Red','Green','Blue'])
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Flux (Watts/nm)')
plt.savefig('q5a_gaussian_rgb.png')

power_red = sum(y_red)*1
power_green = sum(y_green)*1
power_blue = sum(y_blue)*1

power_all = [['red','green','blue'],[power_red,power_green,power_blue]]
print(str(power_all[0])+'='+str(power_all[1]))
#%% HW0-5b
# cie tristimulus spectrum
import numpy as np
import matplotlib.pyplot as plt

cie = np.loadtxt("cie1931xyz.txt")
ciewavelength = []
ciex = []
ciey = []
ciez = []

for j in range(0,len(cie)):
    ciewavelength.append(cie[j][0])
    ciex.append(cie[j][1])
    ciey.append(cie[j][2])
    ciez.append(cie[j][3])

ciewavelength = ciewavelength[0:401]
ciex = ciex[0:401]
ciey = ciey[0:401]
ciez = ciez[0:401]


X_red = []
Y_red = []
Z_red = []
for k in range(0,len(ciewavelength)):
    X_red.append(ciex[k] * y_red[k])
    Y_red.append(ciey[k] * y_red[k])
    Z_red.append(ciez[k] * y_red[k])
    
X_red_sum = sum(X_red)
Y_red_sum = sum(Y_red)
Z_red_sum = sum(Z_red)
# red_all = X_red_sum+Y_red_sum+Z_red_sum

answer_q5b_red = [X_red_sum/Y_red_sum,Y_red_sum/Y_red_sum,Z_red_sum/Y_red_sum]
print(answer_q5b_red)


X_green = []
Y_green = []
Z_green = []
for k in range(0,len(ciewavelength)):
    X_green.append(ciex[k] * y_green[k])
    Y_green.append(ciey[k] * y_green[k])
    Z_green.append(ciez[k] * y_green[k])
    
X_green_sum = sum(X_green)
Y_green_sum = sum(Y_green)
Z_green_sum = sum(Z_green)

answer_q5b_green = [X_green_sum/Y_green_sum,Y_green_sum/Y_green_sum,Z_green_sum/Y_green_sum]
print(answer_q5b_green)

X_blue = []
Y_blue = []
Z_blue = []
for k in range(0,len(ciewavelength)):
    X_blue.append(ciex[k] * y_blue[k])
    Y_blue.append(ciey[k] * y_blue[k])
    Z_blue.append(ciez[k] * y_blue[k])
    
X_blue_sum = sum(X_blue)
Y_blue_sum = sum(Y_blue)
Z_blue_sum = sum(Z_blue)

answer_q5b_blue = [X_blue_sum/Y_blue_sum,Y_blue_sum/Y_blue_sum,Z_blue_sum/Y_blue_sum]
print(answer_q5b_blue)

#%% HW0-5c CIELAB
cal_red = answer_q5b_blue
ref_white = [0.95047, 1, 1.08883]
tx = (cal_red[0]/ref_white[0])
ty = (cal_red[1]/ref_white[1])
tz = (cal_red[2]/ref_white[2])
fx = tx/(3*(6/29)**2)+(4/29)
fy = ty/(3*(6/29)**2)+(4/29)
fz = tz/(3*(6/29)**2)+(4/29)
L = 116*fy-16
a = 500*(fx-fy)
b = 200*(fy-fz)

print(f'L: {L} \na: {a} \nb: {b}')

#%% HW0-5d CIELUV
cal_color = [0.95047, 1, 1.08883]
ref_white = [0.95047, 1, 1.08883]
Y_Yn = cal_color[1]/ref_white[1]
L = 116*Y_Yn**(1/3)-16
denominator = cal_color[0]+15*cal_color[1]+3*cal_color[2]
denominator_ref = ref_white[0]+15*ref_white[1]+3*ref_white[2]

u_bar = 4*cal_color[0]/denominator
u_bar_ref = 4*ref_white[0]/denominator_ref
u = 13*L*(u_bar-u_bar_ref)

v_bar = 9*cal_color[1]/denominator
v_bar_ref = 9*ref_white[1]/denominator_ref
v = 13*L*(v_bar-v_bar_ref) 

print(f'L: {L} \nu: {u} \nv: {v}')
print(f"u': {u_bar} \nv': {v_bar}")

#%% CIELUV Plot

import numpy as np
import matplotlib.pyplot as plt

d65 = np.loadtxt("d65.txt")
d65wavelength = []
d65flux = []

for i in range(0,len(d65)):
    d65wavelength.append(d65[i][0])
    d65flux.append(d65[i][1])
    
plt.figure(dpi=300)
plt.plot(d65wavelength,d65flux)
plt.title('D65 spectrum')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Flux (Watts/nm)')
plt.xlim((350,850))
plt.xticks(np.linspace(350,850,11))
plt.ylim(((0,1)))
plt.grid()

cie = np.loadtxt("cie1931xyz.txt")
ciewavelength = []
ciex = []
ciey = []
ciez = []

for j in range(0,len(cie)):
    ciewavelength.append(cie[j][0])
    ciex.append(cie[j][1])
    ciey.append(cie[j][2])
    ciez.append(cie[j][3])

plt.figure(dpi=300)
plt.plot(ciewavelength,ciex)
plt.plot(ciewavelength,ciey)
plt.plot(ciewavelength,ciez)
plt.title('CIE 1931 Tristimulus Curves')
plt.xlabel('Wavelength (nm)')
plt.legend(["x","y","z",])

# correct for d65 range
d65flux_start_from360 = d65flux.copy()
for k in d65flux[0:10]:
    d65flux_start_from360.remove(k)
for l in d65flux[411::]:   
    # print(l) 
    d65flux_start_from360.remove(l)
# correct for cie range
ciewavelength_start_from360nm = ciewavelength.copy()
for n in ciewavelength_start_from360nm[401::]:
    # print(n)
    ciewavelength_start_from360nm.remove(n)
    
X = []
Y = []
Z = []
x = []
y = []

for m in range(0,len(d65flux_start_from360)):
    
    X.append(ciex[m] * d65flux_start_from360[m])
    Y.append(ciey[m] * d65flux_start_from360[m])
    Z.append(ciez[m] * d65flux_start_from360[m])
    x.append(4*X[m]/(X[m]+15*Y[m]+3*Z[m]))
    y.append(9*Y[m]/(X[m]+15*Y[m]+3*Z[m]))

sum_X = sum(X)    
sum_Y = sum(Y)
sum_Z = sum(Z)
sum_all = sum_X+sum_Y+sum_Z

normalized_X = sum_X/sum_Y
normalized_Y = sum_Y/sum_Y
normalized_Z = sum_Z/sum_Y
normalized_sum = normalized_X+normalized_Y+normalized_Z


X_coordinate = 4*normalized_X/(normalized_X+15*normalized_Y+3*normalized_Z)
Y_coordinate = 9*normalized_Y/(normalized_X+15*normalized_Y+3*normalized_Z)

RED = [2.473562011839831, 1.0, 0.00020110704560175643]
GREEN = [0.4862204717395029, 1.0, 0.020843550427069965]
BLUE = [5.6282116190086615, 1.0, 30.56178762666784]

X_RED = 4*RED[0]/(RED[0]+15*RED[1]+3*RED[2]) 
X_GREEN = 4*GREEN[0]/(GREEN[0]+15*GREEN[1]+3*GREEN[2]) 
X_BLUE = 4*BLUE[0]/(BLUE[0]+15*BLUE[1]+3*BLUE[2]) 
Y_RED = 9*RED[1]/(RED[0]+15*RED[1]+3*RED[2]) 
Y_GREEN = 9*GREEN[1]/(GREEN[0]+15*GREEN[1]+3*GREEN[2]) 
Y_BLUE = 9*BLUE[1]/(BLUE[0]+15*BLUE[1]+3*BLUE[2]) 

plt.figure(figsize=(5,5),dpi=300)
plt.plot(x,y,'o',color='RED')
plt.plot(X_coordinate,Y_coordinate,"s",color='Black')
plt.plot([X_RED,X_GREEN],[Y_RED,Y_GREEN],'bo-')
plt.plot([X_GREEN,X_BLUE],[Y_GREEN,Y_BLUE],'bo-')
plt.plot([X_BLUE,X_RED],[Y_BLUE,Y_RED],'bo-')
white_point_location = 'D65 White Points (' + '{:.2f},'.format(X_coordinate) + '{:.2f})'.format(Y_coordinate) 
plt.annotate(white_point_location,(X_coordinate,Y_coordinate),(X_coordinate-0.02,Y_coordinate+0.025))
plt.title('1976 Universal Chromaticity Scale (UCS)')
plt.xlabel("u'")
plt.ylabel("v'")
plt.grid()
plt.savefig('q5d_CIELUC_Plot.png')

#%% HW0-5e
# Luminous Efficacy of Radiation (LER)
import numpy as np
import matplotlib.pyplot as plt

cie = np.loadtxt("cie1931xyz.txt")
ciewavelength = []
ciex = []
ciey = []
ciez = []

for j in range(0,len(cie)):
    ciewavelength.append(cie[j][0])
    ciex.append(cie[j][1])
    ciey.append(cie[j][2])
    ciez.append(cie[j][3])

ciewavelength = ciewavelength[0:401]
ciex = ciex[0:401]
ciey = ciey[0:401]
ciez = ciez[0:401]

fwhm = 40
rau = fwhm/2.355
x = np.linspace(360,760,401)
y_red = np.exp(-(x-650)**2/(2*rau**2))
y_green = np.exp(-(x-550)**2/(2*rau**2))
y_blue = np.exp(-(x-450)**2/(2*rau**2))

power_red = sum(y_red)*1
power_green = sum(y_green)*1
power_blue = sum(y_blue)*1

#Red
y_list = y_red.tolist()
numerator = []
for j in range(0,len(ciewavelength)):
    numerator.append(y_list[j]*ciey[j])
    
LER_lm = 683*sum(numerator)  
LER_w = power_red

LER_red = LER_lm/LER_w # unit: (lm/W)
print(LER_red)

# same as green & blue


#%% HW0-5f
answer_q5f_all = np.array([answer_q5b_red,answer_q5b_green, answer_q5b_blue]).transpose()
answer_q5f_all_trans = answer_q5f_all.transpose()
d65_metrix = np.array([0.95047,1,1.08883])
color_reproduction = np.matmul(answer_q5f_all_trans,d65_metrix)
Mr = color_reproduction[0]/sum(color_reproduction)
Mg = color_reproduction[1]/sum(color_reproduction)
Mb = color_reproduction[2]/sum(color_reproduction)
Mi = [Mr,Mg,Mb]
print(Mi)
    








#%%
answer_q5b_all = np.array([answer_q5b_red,answer_q5b_green, answer_q5b_blue])
answer_q5b_all = answer_q5b_all.transpose()
answer_q5b_all = np.array([['red','green','blue'],answer_q5b_all[0],answer_q5b_all[1],answer_q5b_all[2]])
print(answer_q5b_all)
#%%

# for k in ciewavelength[401::]:
    # ciewavelength.remove(k)
    # ciex.remove(ciex[k])
    # ciey.remove(k)
    # ciez.remove(k)
    # print(k)
    
# plt.figure(dpi=300)
# plt.plot(ciewavelength,ciex)
# plt.plot(ciewavelength,ciey)
# plt.plot(ciewavelength,ciez)
# plt.title('CIE 1931 Tristimulus Curves')
# plt.xlabel('Wavelength (nm)')
# plt.legend(["x","y","z",])


