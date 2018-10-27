#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 11:59:25 2018

@author: andreunsal
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate as integrate

# FUNCTION
    # INTEGRATES X, Y, AND Z DATA TWICE
def DoubleIntegration(xAcc, yAcc, zAcc):

    return

# FUNCTION
    # GENERATES MEAN OFFSET VALUES
def MeanValues(xAcc, yAcc, zAcc):
    xMean = np.mean(xAcc)
    yMean = np.mean(yAcc)
    zMean = np.mean(zAcc)
    print('\nMean Offset X:', '%.10f' %xMean)
    print('Mean Offset Y:', '%.10f' %yMean)
    print('Mean Offset Z:', '%.10f' %(1-zMean)) # Z is offset by +1 originally
    return

# FUNCTION
    # GENERATES RMS VALUES
def RMSValues(xAcc, yAcc, zAcc):
    Xrms = np.sqrt(np.mean(xAcc))
    Yrms = np.sqrt(np.mean(yAcc))
    Zrms = np.sqrt(np.mean(zAcc))
    print('\nRMS X:', '%.5f' %Xrms)
    print('RMS Y:', '%.5f' %Yrms)
    print('RMS Z:', '%.5f' %Zrms)
    return

# FUNCTION
    # PLOTS ACCELERATION IN X, Y, AND Z
def XYZAcceleration(time, xAcc, yAcc, zAcc):
    plt.plot(time, xAcc, label= 'X')
    plt.plot(time, yAcc, label = 'Y')
    plt.plot(time, zAcc, label = 'Z')
    plt.title('Acceleration in X, Y, and Z Domains')
    plt.xlabel('time (min)')
    plt.ylabel('Acceleration (g)')
    plt.legend(loc='lower left')
    plt.grid()
    plt.xlim() # May change depending on situation
    plt.ylim() # May change depending on situation
    plt.show()
    return

# FUNCTION
    # HIGH RES X DOMAIN SIGNAL
def XAcceleration(time, xAcc):
    plt.plot(time, xAcc, label = 'X')
    plt.title('Acceleration in X Domain, Zoomed')
    plt.xlabel('time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim() # May change depending on situation
    plt.ylim()
    plt.show()
    return

# FUNCTION
    # HIGH RES Y DOMAIN SIGNAL
def YAcceleration(time, yAcc):
    plt.plot(time, yAcc, label = 'Y')
    plt.title('Acceleration in Y Domain, Zoomed')
    plt.xlabel('time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim() # May change depending on situation
    plt.ylim()
    plt.show()
    return

# FUNCTION
    # HIGH RES Z DOMAIN SIGNAL
def ZAcceleration(time, zAcc):
    plt.plot(time, zAcc, label = 'Z')
    plt.title('Acceleration in Z Domain, Zoomed')
    plt.xlabel('time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim() # May change depending on situation
    plt.ylim() # May change depending on situation
    plt.show()
    return

# FUNCTION
    # READS DATA AND CALLS OTHER FUNCTIONS FOR PROCESSING AND ANALYSIS
def Main(filename):
    
    # Data preparation
    allData = pd.read_csv(filename)
    xAcc = allData.loc[:, 'x-axis (g)'].values
    yAcc = allData.loc[:, 'y-axis (g)'].values
    zAcc = allData.loc[:, 'z-axis (g)'].values
    time = allData.loc[:, 'elapsed (s)'].values
    time = time / 60 # convert to minutes
        
    # Check file size, sample count, and report time
    fileStats = os.stat(filename)
    fileSize = fileStats.st_size/(1e6) # file size in MB
    print('\nData Size:', '%.2f' %fileSize, 'MB')
    print('Samples:', len(allData))
    print('Time measured:', int(time[-1]),':', '%.2f' %((time[-1] - int(time[-1]))*60), 's')
    
    # Function call sequence before offset adjustment
    XAcceleration(time, xAcc)
    YAcceleration(time, yAcc)
    ZAcceleration(time, zAcc)
    XYZAcceleration(time, xAcc, yAcc, zAcc)
    MeanValues(xAcc, yAcc, zAcc)
    RMSValues(xAcc, yAcc, zAcc)
    
    # Removing the offsets
    xAcc = xAcc - 0.0115489292
    yAcc = yAcc - 0.1096326890
    zAcc = zAcc + 0.0100208415
    print('\nTHE DATA FOLLOWING THIS LINE IS WITH OFFSETS REMOVED')
    
    # Function call sequence after offset adjustment
    XYZAcceleration(time, xAcc, yAcc, zAcc)
    MeanValues(xAcc, yAcc, zAcc)
    RMSValues(xAcc, yAcc, zAcc)
    DoubleIntegration(xAcc, yAcc, zAcc)
    return
    
# Program triggers from this line
    # edit argument for other .csv data files
Main('Stationary3 100Hz +- 16Gs October 26 2018.csv')





