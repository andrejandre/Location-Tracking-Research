#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 14:01:33 2019

@author: andreunsal
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as it
import scipy.signal as signal
from mpl_toolkits import mplot3d 

filename = 'GPS_Tests_Walking_in_Meters.xlsx'
gpsData = pd.read_excel(filename)

xGPSDis = []
yGPSDis = []
zGPSDis = []

xChange = gpsData['Change X (m)']
yChange = gpsData['Change Y (m)']
zChange = gpsData['Change Z (m)']

plt.plot(xChange, yChange)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(num = None, figsize=(10, 8), dpi=80, facecolor = 'w', edgecolor='b')
ax = plt.axes(projection = '3d')
ax.plot3D(xChange, yChange, zChange, 'blue', label = 'Trajectory', linewidth = 2)
ax.set_xlabel('X DISTANCE [M]', fontsize = 12)
ax.set_ylabel('Y DISTANCE [M]', fontsize = 12)
ax.set_zlabel('Z DISTANCE [M]', fontsize = 12)
ax.set_xlim3d(-10, 10)
ax.set_ylim3d(-10, 10)
ax.set_zlim3d(-10, 10)
plt.legend(loc = 'upper left')
plt.title('Location Trajectory (GPS)')
plt.show()
