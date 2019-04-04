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
filename = 'Stat3.csv'

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


#==============================================================================
# 
#==============================================================================
plt.plot(flatVelX)
plt.plot(flatVelY)
plt.title('Velocity with data stitching at 5s intervals')
plt.ylabel('m/s')
plt.xlabel('index of velocity vectors')
plt.ylim(-3, 3)
plt.show()
        
#xVel = it.cumtrapz(xAcc, time)
#yVel = it.cumtrapz(yAcc, time)
        


    
































