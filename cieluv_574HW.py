#%% HW0-4

import numpy as np
import matplotlib.pyplot as plt

# d65 = np.loadtxt("d65.txt")
d65 = np.loadtxt("/Users/cwchan/code/hw_code/d65.txt")
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

# cie = np.loadtxt("cie1931xyz.txt")
cie = np.loadtxt("/Users/cwchan/code/hw_code/cie1931xyz.txt")
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




#%% CIELUV Plot
# Author: Jeff Chan
# Date: 2023/09/27
# Email: kd110544@gmail.com

import numpy as np
import matplotlib.pyplot as plt

# d65 = np.loadtxt("d65.txt")
d65 = np.loadtxt("/Users/cwchan/code/hw_code/d65.txt")

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

# cie = np.loadtxt("cie1931xyz.txt")
cie = np.loadtxt("/Users/cwchan/code/hw_code/cie1931xyz.txt")

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
# plt.savefig('q5d_CIELUC_Plot.png')