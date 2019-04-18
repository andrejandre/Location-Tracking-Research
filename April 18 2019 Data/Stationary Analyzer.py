# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:43:45 2019

@author: Andre
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#==============================================================================
# File under analysis.
#==============================================================================
filename1 = 'Stat1.csv'
filename2 = 'Stat2.csv'
filename3 = 'Stat3.csv'
filename4 = 'Stat4.csv'
filename5 = 'Stat5.csv'
filename6 = 'Stat6.csv'
filename7 = 'Stat7.csv'
filename8 = 'Stat8.csv'
filename9 = 'Stat9.csv'
filename10 = 'Stat10.csv'
#==============================================================================
# Data preparation
#==============================================================================
print('\n *** FILE METRICS ***')
print(filename1, filename2, filename3, filename4,
      filename5, filename6, filename7, filename8, filename9,
      filename10, 'are being analyzed')
allData1 = pd.read_csv(filename1)
allData2 = pd.read_csv(filename2)
allData3 = pd.read_csv(filename3)
allData4 = pd.read_csv(filename4)
allData5 = pd.read_csv(filename5)
allData6 = pd.read_csv(filename6)
allData7 = pd.read_csv(filename7)
allData8 = pd.read_csv(filename8)
allData9 = pd.read_csv(filename9)
allData10 = pd.read_csv(filename10)
xAcc1 = allData1.loc[:, 'x-axis (g)'].values
yAcc1 = allData1.loc[:, 'y-axis (g)'].values
time1 = allData1.loc[:, 'elapsed (s)'].values
xAcc2 = allData2.loc[:, 'x-axis (g)'].values
yAcc2 = allData2.loc[:, 'y-axis (g)'].values
time2 = allData2.loc[:, 'elapsed (s)'].values
xAcc3 = allData3.loc[:, 'x-axis (g)'].values
yAcc3 = allData3.loc[:, 'y-axis (g)'].values
time3 = allData3.loc[:, 'elapsed (s)'].values
xAcc4 = allData4.loc[:, 'x-axis (g)'].values
yAcc4 = allData4.loc[:, 'y-axis (g)'].values
time4 = allData4.loc[:, 'elapsed (s)'].values
xAcc5 = allData5.loc[:, 'x-axis (g)'].values
yAcc5 = allData5.loc[:, 'y-axis (g)'].values
time5 = allData5.loc[:, 'elapsed (s)'].values
xAcc6 = allData6.loc[:, 'x-axis (g)'].values
yAcc6 = allData6.loc[:, 'y-axis (g)'].values
time6 = allData6.loc[:, 'elapsed (s)'].values
xAcc7 = allData7.loc[:, 'x-axis (g)'].values
yAcc7 = allData7.loc[:, 'y-axis (g)'].values
time7 = allData7.loc[:, 'elapsed (s)'].values
xAcc8 = allData8.loc[:, 'x-axis (g)'].values
yAcc8 = allData8.loc[:, 'y-axis (g)'].values
time8 = allData8.loc[:, 'elapsed (s)'].values
xAcc9 = allData9.loc[:, 'x-axis (g)'].values
yAcc9 = allData9.loc[:, 'y-axis (g)'].values
time9 = allData9.loc[:, 'elapsed (s)'].values
xAcc10 = allData10.loc[:, 'x-axis (g)'].values
yAcc10 = allData10.loc[:, 'y-axis (g)'].values
time10 = allData10.loc[:, 'elapsed (s)'].values
for i in range(len(time1)):
    if time1[i] >= 100.:
        time1[i] = 0
for i in range(len(time2)):
    if time2[i] >= 100.:
        time2[i] = 0
for i in range(len(time3)):
    if time3[i] >= 100.:
        time3[i] = 0
for i in range(len(time4)):
    if time4[i] >= 100.:
        time4[i] = 0
for i in range(len(time5)):
    if time5[i] >= 100.:
        time5[i] = 0
for i in range(len(time6)):
    if time6[i] >= 100.:
        time6[i] = 0
for i in range(len(time7)):
    if time7[i] >= 100.:
        time7[i] = 0
for i in range(len(time8)):
    if time8[i] >= 100.:
        time8[i] = 0
for i in range(len(time9)):
    if time9[i] >= 100.:
        time9[i] = 0
for i in range(len(time10)):
    if time10[i] >= 100.:
        time10[i] = 0
#==============================================================================
# Stationary Analytics
#==============================================================================
plt.plot(time1, xAcc1)
plt.title('xAcc1')
plt.show()
plt.plot(time1, yAcc1)
plt.title('yAcc1')
plt.show()
plt.plot(time2, xAcc2)
plt.title('xAcc2')
plt.show()
plt.plot(time2, yAcc2)
plt.title('yAcc2')
plt.show()
plt.plot(time3, xAcc3)
plt.title('xAcc3')
plt.show()
plt.plot(time3, yAcc3)
plt.title('yAcc3')
plt.show()
plt.plot(time4, xAcc4)
plt.title('xAcc4')
plt.show()
plt.plot(time4, yAcc4)
plt.title('yAcc4')
plt.show()
plt.plot(time5, xAcc5)
plt.title('xAcc5')
plt.show()
plt.plot(time5, yAcc5)
plt.title('yAcc5')
plt.show()
plt.plot(time6, xAcc6)
plt.title('xAcc6')
plt.show()
plt.plot(time6, yAcc6)
plt.title('yAcc6')
plt.show()
plt.plot(time7, xAcc7)
plt.title('xAcc7')
plt.show()
plt.plot(time7, yAcc7)
plt.title('yAcc7')
plt.show()
plt.plot(time8, xAcc8)
plt.title('xAcc8')
plt.show()
plt.plot(time8, yAcc8)
plt.title('yAcc8')
plt.show()
plt.plot(time9, xAcc9)
plt.title('xAcc9')
plt.show()
plt.plot(time9, yAcc9)
plt.title('yAcc9')
plt.show()
plt.plot(time10, xAcc10)
plt.title('xAcc10')
plt.show()
plt.plot(time10, yAcc10)
plt.title('yAcc10')
plt.show()
offx1 = np.mean(xAcc1)
offx2 = np.mean(xAcc2)
offx3 = np.mean(xAcc3)
offx4 = np.mean(xAcc4)
offx5 = np.mean(xAcc5)
offx6 = np.mean(xAcc6)
offx7 = np.mean(xAcc7)
offx8 = np.mean(xAcc8)
offx9 = np.mean(xAcc9)
offx10 = np.mean(xAcc10)
offy1 = np.mean(yAcc1)
offy2 = np.mean(yAcc2)
offy3 = np.mean(yAcc3)
offy4 = np.mean(yAcc4)
offy5 = np.mean(yAcc5)
offy6 = np.mean(yAcc6)
offy7 = np.mean(yAcc7)
offy8 = np.mean(yAcc8)
offy9 = np.mean(yAcc9)
offy10 = np.mean(yAcc10)
print("1 - OFFSET X: ", offx1)
print("1 - OFFSET Y: ", offy1)
print("2 - OFFSET X: ", offx2)
print("2 - OFFSET Y: ", offy2)
print("3 - OFFSET X: ", offx3)
print("3 - OFFSET Y: ", offy3)
print("4 - OFFSET X: ", offx4)
print("4 - OFFSET Y: ", offy4)
print("5 - OFFSET X: ", offx5)
print("5 - OFFSET Y: ", offy5)
print("6 - OFFSET X: ", offx6)
print("6 - OFFSET Y: ", offy6)
print("7 - OFFSET X: ", offx7)
print("7 - OFFSET Y: ", offy7)
print("8 - OFFSET X: ", offx8)
print("8 - OFFSET Y: ", offy8)
print("9 - OFFSET X: ", offx9)
print("9 - OFFSET Y: ", offy9)
print("10 - OFFSET X:", offx10)
print("10 - OFFSET Y:", offy10)
print("MEAN OFFSET X:", (offx1+offx2+offx3+offx4+offx5
                                +offx6+offx7+offx8+offx9+offx10)/10)
print("MEAN OFFSET Y:", (offy1+offy2+offy3+offy4+offy5
                                +offy6+offy7+offy8+offy9+offy10)/10)
    