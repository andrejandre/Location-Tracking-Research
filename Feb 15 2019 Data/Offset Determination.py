#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 14:02:47 2019

@author: andreunsal
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as it
import scipy.signal as signal
from mpl_toolkits import mplot3d 

filename = 'Semester 2 Stationary Test1 100Hz +- 2Gs Feb 2 2019.csv'

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
# Plotting X Acceleration and reporting offset
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, xAcc, label = 'X', color = 'r', linewidth = 1)
plt.title('X Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-0.2, 0.2)
plt.grid()
plt.show()
print('Offset X:', np.mean(xAcc))

#==============================================================================
# Plotting Y Acceleration and reporting offset
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, yAcc, color = 'g', linewidth = 1)
plt.title('Y Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim(-0.2, 0.2)
plt.grid()
plt.show()
print('Offset Y:', np.mean(yAcc))

#==============================================================================
# Plotting Z Acceleration and reporting offset
#==============================================================================
plt.figure(figsize = (10, 6))
plt.plot(time, zAcc, color = 'b', linewidth = 1)
plt.title('Z Acceleration')
plt.ylabel('Acceleration (g)')
plt.xlabel('Time (s)')
plt.xlim()
plt.ylim()
plt.grid()
plt.show()
print('Offset Z:', np.mean(zAcc))

