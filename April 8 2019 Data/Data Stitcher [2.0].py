# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 17:25:51 2019

@author: Andre
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as it
import scipy.signal as signal
from mpl_toolkits import mplot3d 

#==============================================================================
# File under analysis.
#==============================================================================
filename = 'Bigfieldsquare.csv'

#==============================================================================
# Data preparation
#==============================================================================
print('\n *** FILE METRICS ***')
print(filename, 'is being analyzed')
allData = pd.read_csv(filename)
xAcc = allData.loc[:, 'x-axis (g)'].values
yAcc = allData.loc[:, 'y-axis (g)'].values
zAcc = allData.loc[:, 'z-axis (g)'].values
for i in range(len(zAcc)):
    zAcc[i] = 0
time = allData.loc[:, 'elapsed (s)'].values

#==============================================================================
# File metrics
#==============================================================================
fileStats = os.stat(filename)
fileSize = fileStats.st_size/(1e6) # file size in MB
print('File size:', '%.2f' %fileSize, 'MB')
print('Samples:', len(allData))
print('Time elapsed:', time[-1], 's')

#==============================================================================
# Plotting X Acceleration
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1)
plt.title('X Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Plotting Y Acceleration
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, yAcc, color = 'g', linewidth = 1)
plt.title('Y Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Plotting Z Acceleration
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, zAcc, color = 'b', linewidth = 1)
plt.title('Z Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Plotting all accelerations
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1, alpha = 0.6)
plt.plot(time, yAcc, label = 'Y', color = 'g', linewidth = 1, alpha = 0.6)
plt.plot(time, zAcc, label = 'Z', color = 'b', linewidth = 2, alpha = 0.6)
plt.title('X, Y, and Z Acceleration')
plt.legend(loc = 'upper left')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Butterworth Filtering X and Y Acceleration
#==============================================================================
N = 2 # Filter order
Wn = 0.001 # Cutoff frequency 0 < Wn < 1
B, A = signal.butter(N, Wn, output = 'ba')
#xAcc[:] = signal.filtfilt(B, A, xAcc[:])
#yAcc[:] = signal.filtfilt(B, A, yAcc[:])
N = 2
Wn = 0.03
B, A = signal.butter(N, Wn, output = 'ba')
xAcc = signal.filtfilt(B, A, xAcc)
yAcc = signal.filtfilt(B, A, yAcc)
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, linewidth = 1, color = 'r')
plt.plot(time, yAcc, linewidth = 1, color = 'g')
plt.title('X and Y Acceleration Denoised')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Removing offsets
# The values used to remove offset are determined by 10 stationary tests 
# which study the variance in X and Y offset and determine the mean offset 
# to apply to the signals for most truthful results
#==============================================================================
xAcc = xAcc - 0.02371321966479816
yAcc = yAcc - 0.11895615670204282

#==============================================================================
# Plotting offset removal
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1, alpha = 0.6)
plt.plot(time, yAcc, label = 'Y', color = 'g', linewidth = 1, alpha = 0.6)
plt.plot(time, zAcc, label = 'Z', color = 'b', linewidth = 2, alpha = 0.6)
plt.title('X, Y, and Z Acceleration with Offset Removed')
plt.legend(loc = 'upper left')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.xlim()
plt.ylim(-1, 1)
plt.grid()
plt.show()

#==============================================================================
# Conditional Data Stitching Sequence
# 1. Target first 5 seconds of acceleration data
# 2. Integrate for velocity
# 3. Integrate for displacement
# 4. Store data into target list
# 4. Target next 5 seconds of acceleration data
# 5. Repeat steps 2-4 until data is finished
#==============================================================================
targetX = []
xVel = []
yVel = []
xDis = []
yDis = []
xDisi = []
yDisi = []
indexTargets = []
# Rounding time values to enhance modulo division
for i in range(len(time)):
    time[i] = round(time[i], 1)
# extracting 5 second interval indices
for idx, i in enumerate(time):
    if (time[idx] % 5 == 0.):
        #print('index:', idx, 'time:', time[idx])
        indexTargets.append(idx)
# filtering targeted indices
for idx, i in enumerate(indexTargets):
    try:
        curr = indexTargets[idx]
        nexti = indexTargets[idx + 1]
        if curr == nexti - 1:
            indexTargets.remove(indexTargets[idx + 1])
    except IndexError:
        pass
# filtering targeted indices
for idx, i in enumerate(indexTargets):
    try:
        curr = indexTargets[idx]
        nexti = indexTargets[idx + 1]
        if curr == nexti - 2:
            indexTargets.remove(indexTargets[idx + 1])
    except IndexError:
        pass
# filtering targeted indices
for idx, i in enumerate(indexTargets):
    try: 
        curr = indexTargets[idx]
        nexti = indexTargets[idx + 1]
        if curr == nexti - 4:
            indexTargets.remove(indexTargets[idx + 1])
    except IndexError:
        pass
# filtering targeted indices
for idx, i in enumerate(indexTargets):
    try: 
        curr = indexTargets[idx]
        nexti = indexTargets[idx + 1]
        if curr == nexti - 8:
            indexTargets.remove(indexTargets[idx + 1])
    except IndexError:
        pass
# extracting index values and applying integration
for idx, i in enumerate(indexTargets):
    try:
        xVel.append(it.cumtrapz(xAcc[indexTargets[idx]:indexTargets[idx+1]]
        , time[indexTargets[idx]:indexTargets[idx+1]]))
        yVel.append(it.cumtrapz(yAcc[indexTargets[idx]:indexTargets[idx+1]]
        , time[indexTargets[idx]:indexTargets[idx+1]]))
    except IndexError:
        pass
# extracting list of lists for X Velocity
flatVelX = []
for sublist in xVel:
    for item in sublist:
        flatVelX.append(item)
# extracting list of lists for Y Velocity
flatVelY = []
for sublist in yVel:
    for item in sublist:
        flatVelY.append(item)
# extracting index values and applying integration again
padVal = len(time) - len(flatVelX)
for i in range(padVal):
    flatVelX.append(0)
    flatVelY.append(0)
for idx, i in enumerate(indexTargets):
    try:
        xDisi.append(it.cumtrapz(flatVelX[indexTargets[idx]:indexTargets[idx+1]]
        , time[indexTargets[idx]:indexTargets[idx+1]]))
        yDisi.append(it.cumtrapz(flatVelY[indexTargets[idx]:indexTargets[idx+1]]
        , time[indexTargets[idx]:indexTargets[idx+1]]))
    except IndexError:
        pass
# extracting list of lists for X displacement
flatDisX = []
for sublist in xDisi:
    for item in sublist:
        flatDisX.append(item)
# extracting list of lists for Y displacement
flatDisY = []
for sublist in yDisi:
    for item in sublist:
        flatDisY.append(item)

#==============================================================================
# Plotting data stitched velocity
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(flatVelX)
plt.plot(flatVelY)
plt.title('Velocity with data stitching at 5s intervals')
plt.ylabel('m/s')
plt.xlabel('index of velocity vectors')
plt.ylim(-3, 3)
plt.show()
        
#==============================================================================
# Integrating flat velocity to generate displacement/position - no data stitch
#==============================================================================
xDis = it.cumtrapz(flatVelX)
yDis = it.cumtrapz(flatVelY)

#==============================================================================
# Integrating flat velocity via data stitching with correction methods
# 1. create a list to store sum offsets
# 2. create a list to copy flatDisX and flatDisY
# 3. apply offset to each interval using indexTargets on flatDisX and flatDisY
#==============================================================================
offsetsX = []
offsetsY = []
correctedX = []
correctedY = []
for idx, i in enumerate(flatDisX):
    try:
        offsetsX.append(sum(flatDisX[indexTargets[idx]:indexTargets[idx+1]]))
    except IndexError:
        pass
for idx, i in enumerate(flatDisY):
    try:
        offsetsY.append(sum(flatDisY[indexTargets[idx]:indexTargets[idx+1]]))
    except IndexError:
        pass
for idx, i in enumerate(offsetsX):
    try:
        correctedX.append(flatDisX[indexTargets[idx]:indexTargets[idx+1]] + 
                          offsetsX[idx])
    except IndexError:
        pass
correctedX_ = []
for sublist in correctedX:
    for item in sublist:
        correctedX_.append(item)
for idx, i in enumerate(offsetsY):
    try:
        correctedY.append(flatDisY[indexTargets[idx]:indexTargets[idx+1]] + 
                          offsetsY[idx])
    except IndexError:
        pass
correctedY_ = []
for sublist in correctedY:
    for item in sublist:
        correctedY_.append(item)

#==============================================================================
# Plotting displacements and position with comparisons of data stitching
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(xDis, label = 'X')
plt.plot(yDis, label = 'Y')
plt.title('Displacement without data stitching on velocity')
plt.xlabel('index value')
plt.ylabel('Distance (m)')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()

plt.figure(figsize = (10, 6))
plt.plot(xDis, yDis)
plt.title('2D path without stitching on velocity')
plt.xlabel('x pos (m)')
plt.ylabel('y pos (m)')
plt.grid()
plt.show()

plt.figure(figsize = (10, 6))
plt.plot(flatDisX, label = 'X')
plt.plot(flatDisY, label = 'Y')
plt.title('Displacement with data stitching on velocity')
plt.xlabel('index value')
plt.ylabel('Distance (m)')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()

# Checking corrected values for data stitching
plt.figure(figsize = (10, 6))
plt.plot(correctedX_, label = 'CorrectedX_')
plt.plot(correctedY_, label = 'CorrectedY_')
plt.title('Validating CorrectedX_ and CorrectedY_ vectors')
plt.xlabel('index value')
plt.ylabel('Distance (m)')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()

# plotting corrected values via data stitching
plt.figure(figsize = (10, 6))
plt.plot(correctedX_, correctedY_)
plt.title('2D path with data stitching on velocity')
plt.xlabel('x pos (m)')
plt.ylabel('y pos (m)')
plt.grid()
plt.show()

#==============================================================================
# Generating .csv files for Team 38 to conduct further analytics in Excel
#==============================================================================
import csv
from itertools import zip_longest
d = [time, xAcc, yAcc, zAcc, flatVelX, flatVelY, flatDisX, flatDisY]
export_data = zip_longest(*d, fillvalue = '')
with open('Bigfieldsquare_Integrated.csv', 'w', newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(('time', 'x Accel', 'y Accel', 'z Accel', 'x Vel', 'y Vel', 
                   'x Dis', 'y Dis'))
      wr.writerows(export_data)
myfile.close()

"""
#==============================================================================
# Extracting GPS for Comparison
#==============================================================================
gpsFile = 'Square 3.xlsx'
gpsData = pd.read_excel(gpsFile)
xPos = gpsData.loc[:, 'X(m)']
yPos = gpsData.loc[:, 'Y(M)']
xPos = np.abs(xPos)
yPos = np.abs(yPos)

#==============================================================================
# GPS and accelerometer comparison plot
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(xPos, yPos, linewidth = 2, alpha = 1, label = 'gps. coord', color = 'black')
plt.plot(flatDisX, flatDisY, linewidth = 2, alpha = 1, label = 'accel. coord', color = 'r')
plt.title('GPS and Acceleration Trajectories compared [Cartesian]')
plt.xlabel('Distance in X (m)')
plt.ylabel('Distance in Y (m)')
plt.legend(loc = 'upper left')
plt.xlim()
plt.ylim()
plt.grid()
plt.show()
"""