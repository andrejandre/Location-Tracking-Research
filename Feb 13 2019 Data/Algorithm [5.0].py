#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 23:00:52 2019

@author: andreunsal
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as it
import scipy.signal as signal
from mpl_toolkits import mplot3d 

# File under analysis.
filename = 'trial 13_MetaWear_2019-02-13T12.37.03.209_DF111CDFC80D_Accelerometer_1.4.4.csv'

# Data preparation
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

# File metrics
fileStats = os.stat(filename)
fileSize = fileStats.st_size/(1e6) # file size in MB
print('File size:', '%.2f' %fileSize, 'MB')
print('Samples:', len(allData))
print('Time elapsed:', time[-1], 's')

# Plotting X Acceleration
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1)
plt.title('X Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-0.5, 0.5)
plt.grid()
plt.show()

# Plotting Y Acceleration
plt.figure(figsize = (10, 6))
plt.plot(time, yAcc, color = 'g', linewidth = 1)
plt.title('Y Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-0.5, 0.5)
plt.grid()
plt.show()

# Plotting Z Acceleration
plt.figure(figsize = (10, 6))
plt.plot(time, zAcc, color = 'b', linewidth = 1)
plt.title('Z Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-0.5, 0.5)
plt.grid()
plt.show()

# Plotting all accelerations
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1, alpha = 0.6)
plt.plot(time, yAcc, label = 'Y', color = 'g', linewidth = 1, alpha = 0.6)
plt.plot(time, zAcc, label = 'Z', color = 'b', linewidth = 2, alpha = 0.6)
plt.title('X, Y, and Z Acceleration')
plt.legend(loc = 'upper left')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (g)')
plt.xlim()
plt.ylim(-0.5, 0.5)
plt.grid()
plt.show()

# Calculating Mean and Offsets
xMean = np.mean(xAcc)
yMean = np.mean(yAcc)
zMean = np.mean(zAcc)
print('Avg X:', '%.4f' %xMean)
print('Avg Y:', '%.4f' %yMean)
print('Avg Z:', '%.4f' %zMean)

# First integration: generating velocity
xVel = it.cumtrapz(xAcc, time)
yVel = it.cumtrapz(yAcc, time)
zVel = it.cumtrapz(zAcc, time)

# Plotting the velocities
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

# Second integration: generating displacement
xDis = it.cumtrapz(xVel, time)
yDis = it.cumtrapz(yVel, time)
zDis = it.cumtrapz(zVel, time)

# 3D Trajectory Plotting
plt.figure(num = None, figsize=(10, 8), dpi=80, facecolor = 'w', edgecolor='b')
ax = plt.axes(projection = '3d')
ax.plot3D(xDis, yDis, zDis, 'red', label = 'Trajectory', linewidth = 4)
ax.set_xlabel('X DISTANCE [M]', fontsize = 12)
ax.set_ylabel('Y DISTANCE [M]', fontsize = 12)
ax.set_zlabel('Z DISTANCE [M]', fontsize = 12)
ax.set_xlim3d(0, 100)
ax.set_ylim3d(-50, 50)
ax.set_zlim3d(0, 100)
plt.legend(loc = 'upper left')
plt.title('Location Trajectory (Accelerometer)')
plt.show()

# 2D Trajectory Plotting
plt.figure(figsize = (10, 6))
plt.plot(xDis, yDis, linewidth = 3, alpha = 0.7, label = 'XY Coord.', color = 'r')
plt.title('2D Trajectory ((X, Y) Coordinates))')
plt.xlabel('X Distance (m)')
plt.ylabel('Y Distance (m)')
plt.xlim(0, 100)
plt.ylim(-50, 50)
plt.grid()
plt.show()

# Single variable displacement plot
time = np.resize(time, time.size - 1)
plt.figure(figsize = (10, 6))
plt.plot(time, xDis, linewidth = 3, alpha = 0.7, label = 'X vs. Time', color = 'b')
plt.plot(time, yDis, linewidth = 3, alpha = 0.7, label = 'Y vs. Time', color = 'g')
plt.title('X and Y Single Variable Displacement and Drift')
plt.xlabel('Time (s)')
plt.ylabel('Meters')
plt.legend(loc = 'upper left')
plt.xlim() 
plt.ylim(-100, 100)
plt.grid()
plt.show()

# Plotting 2D Map
plt.figure(figsize = (10, 6))
plt.plot(xDis, yDis, linewidth = 3, alpha = 0.7, label = 'XY Coord.', color = 'r')
im = plt.imread('Map.png')
implot = plt.imshow(im)
plt.ylim(0, 200)
plt.xlim(0, 200)
plt.show()



