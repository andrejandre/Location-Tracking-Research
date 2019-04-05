# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:28:48 2019

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
filename = 'Stat2.csv'

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
timeMin = time / 60 # Conversion to minutes

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
# First integration: generating velocity
#==============================================================================
xVel = it.cumtrapz(xAcc, time)
yVel = it.cumtrapz(yAcc, time)
zVel = it.cumtrapz(zAcc, time)

#==============================================================================
# Plotting the velocities
#==============================================================================
time = np.resize(time, time.size - 1)
plt.figure(figsize = (10, 6))
plt.plot(time, xVel, linewidth = 2, alpha = 0.7, label = 'X', color = 'r')
plt.plot(time, yVel, linewidth = 2, alpha = 0.7, label = 'Y', color = 'g')
plt.plot(time, zVel, linewidth = 2, alpha = 0.7, label = 'Z', color = 'b')
plt.title('X, Y, and Z Velocities')
plt.xlabel('Time (s)')
plt.ylabel('Velocity (m/s)')
plt.legend(loc = 'upper left')
plt.grid()
plt.show()

#==============================================================================
# Second integration: generating displacement
#==============================================================================
xDis = it.cumtrapz(xVel, time)
yDis = it.cumtrapz(yVel, time)
zDis = it.cumtrapz(zVel, time)

#==============================================================================
# 3D Trajectory Plotting
#==============================================================================
plt.figure(num = None, figsize=(10, 8), dpi=80, facecolor = 'w', edgecolor='b')
ax = plt.axes(projection = '3d')
ax.plot3D(xDis, yDis, zDis, 'red', label = 'Trajectory', linewidth = 2)
ax.set_xlabel('X DISTANCE [M]', fontsize = 12)
ax.set_ylabel('Y DISTANCE [M]', fontsize = 12)
ax.set_zlabel('Z DISTANCE [M]', fontsize = 12)
ax.set_xlim3d()
ax.set_ylim3d()
ax.set_zlim3d()
plt.legend(loc = 'upper left')
plt.title('Location Trajectory (Accelerometer)')
plt.show()

#==============================================================================
# 2D Trajectory Plotting
#==============================================================================
plt.figure(figsize = (10, 6))
plt.scatter(xDis, yDis, linewidth = 0.1, alpha = 0.7, label = 'XY Coord.', color = 'r')
plt.title('2D Trajectory ((X, Y) Coordinates))')
plt.xlabel('X Distance (m)')
plt.ylabel('Y Distance (m)')
plt.xlim()
plt.ylim()
plt.grid()
plt.show()

#==============================================================================
# Single variable displacement plot
#==============================================================================
time = np.resize(time, time.size - 1)
plt.figure(figsize = (10, 6))
plt.plot(time, xDis, linewidth = 3, alpha = 0.7, label = 'X vs. Time', color = 'b')
plt.plot(time, yDis, linewidth = 3, alpha = 0.7, label = 'Y vs. Time', color = 'g')
plt.title('X and Y Single Variable Displacement and Drift')
plt.xlabel('Time (s)')
plt.ylabel('Meters')
plt.legend(loc = 'upper left')
plt.xlim() 
plt.ylim()
plt.grid()
plt.show()

#==============================================================================
# Extracting GPS for Comparison
#==============================================================================
"""
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
plt.plot(xPos, yPos, linewidth = 2, alpha = 1, label = 'gps. coord', color = 'b')
plt.plot(xDis, yDis, linewidth = 2, alpha = 1, label = 'accel. coord', color = 'r')
plt.title('GPS and Acceleration Trajectories compared [Cartesian]')
plt.xlabel('Distance in X (m)')
plt.ylabel('Distance in Y (m)')
plt.legend(loc = 'upper left')
plt.xlim()
plt.ylim()
plt.grid()
plt.show()
"""





