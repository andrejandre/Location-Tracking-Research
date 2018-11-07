import os
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import scipy.integrate as it 
from scipy import integrate
#from mpl_toolkits import mplot3d 

def DataPrep(filename):
    print(filename, 'is being analyzed...')
    allData = pd.read_csv(filename)
    xAcc = allData.loc[:, 'x-axis (g)'].values
    yAcc = allData.loc[:, 'y-axis (g)'].values
    zAcc = allData.loc[:, 'z-axis (g)'].values
    timeSeconds = allData.loc[:, 'elapsed (s)'].values
    time = timeSeconds / 60
    fileStats = os.stat(filename)
    fileSize = fileStats.st_size/(1e6) # file size in MB
    DataSet = {
               "File Size (MB)": fileSize, 
               "Time (s)": timeSeconds[-1], 
               "Time (min)": time[-1],
               "Time (all)": timeSeconds,
               "Sample Count": len(allData),
               "X Accel. (g)": xAcc,
               "Y Accel. (g)": yAcc,
               "Z Accel. (g)": zAcc
               }
    return(DataSet)

def Plotter(DataSet):
    time = DataSet["Time (all)"]
    xAcc = DataSet["X Accel. (g)"]
    yAcc = DataSet["Y Accel. (g)"]
    zAcc = DataSet["Z Accel. (g)"]
    plt.plot(time, xAcc, label = 'X')
    plt.title('Acceleration in X Domain, Zoomed')
    plt.xlabel('time (s)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim() # May change depending on situation
    plt.ylim(-0.1, 0.1)
    plt.show()
    plt.plot(time, yAcc, label = 'Y')
    plt.title('Acceleration in Y Domain, Zoomed')
    plt.xlabel('time (s)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim()
    plt.ylim(-0.1, 0.1)
    plt.show()
    plt.plot(time, zAcc, label = 'Z')
    plt.xlabel('time (s)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim()
    plt.ylim(0.9, 1.1)
    plt.show()
    plt.plot(time, xAcc, label = 'X')
    plt.plot(time, yAcc, label = 'Y')
    plt.plot(time, zAcc, label = 'Z')
    plt.title('Acceleration in X, Y, and Z Domains')
    plt.xlabel('Time (min)')
    plt.ylabel('Acceleration (g)')
    plt.legend(loc = 'lower left')
    plt.grid()
    plt.xlim()
    plt.ylim()
    plt.show()
    return

def OffsetCorrection(DataSet):
    xAcc = DataSet["X Accel. (g)"]
    yAcc = DataSet["Y Accel. (g)"]
    zAcc = DataSet["Z Accel. (g)"]
    xMean = np.mean(xAcc)
    yMean = np.mean(yAcc)
    zMean = np.mean(zAcc)
    print('Mean Offset X:', '%.10f' %xMean)
    print('Mean Offset Y:', '%.10f' %yMean)
    print('Mean Offset Z:', '%.10f' %(1-zMean))
    DataSet["Mean Offset X"] = xMean
    DataSet["Mean Offset Y"] = yMean
    DataSet["Mean Offset Z"] = zMean
    xRMS = np.sqrt(xMean)
    yRMS = np.sqrt(yMean)
    zRMS = np.sqrt(zMean)
    print('RMS X:', '%.5f' %xRMS)
    print('RMS Y:', '%.5f' %yRMS)
    print('RMS Z:', '%.5f' %zRMS)
    DataSet["RMS X"] = xRMS
    DataSet["RMS Y"] = yRMS
    DataSet["RMS Z"] = zRMS
    xAcc_ = xAcc - xMean
    yAcc_ = yAcc - yMean
    zAcc_ = zAcc - zMean
    DataSet["Corrected X Accel. (g)"] = xAcc_
    DataSet["Corrected Y Accel. (g)"] = yAcc_
    DataSet["Corrected Z Accel. (g)"] = zAcc_
    return(DataSet)

def NoiseRemoval(DataSet):
    xAcc_ = DataSet["Corrected X Accel. (g)"]
    yAcc_ = DataSet["Corrected Y Accel. (g)"]
    zAcc_ = DataSet["Corrected Z Accel. (g)"]
    margin = 0.02 # CHANGE THIS VALUE TO ALTER NOISE CHARACTERISTICS
    for i in range(len(xAcc_)):
        if abs(xAcc_[i]) < margin:
            xAcc_[i] = 0
    for i in range(len(yAcc_)):
        if abs(yAcc_[i]) < margin:
            yAcc_[i] = 0
    for i in range(len(zAcc_)):
        if abs(zAcc_[i]) < margin:
            zAcc_[i] = 0
    DataSet["Corrected X Accel. (g)"] = xAcc_
    DataSet["Corrected Y Accel. (g)"] = yAcc_
    DataSet["Corrected Z Accel. (g)"] = zAcc_
    return(DataSet)
    
def CorrectedPlotter(DataSet):
    time = DataSet["Time (all)"]
    xAcc_ = DataSet["Corrected X Accel. (g)"]
    yAcc_ = DataSet["Corrected Y Accel. (g)"]
    zAcc_ = DataSet["Corrected Z Accel. (g)"]
    plt.plot(time, xAcc_)
    plt.title('Noise and Offset Removed: X Domain Zoomed')
    plt.xlabel('Time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim()
    plt.ylim(-0.1, 0.1)
    plt.show()
    plt.plot(time, yAcc_)
    plt.title('Noise and Offset Removed: Y Domain Zoomed')
    plt.xlabel('Time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim()
    plt.ylim(-0.1, 0.1)
    plt.show()
    plt.plot(time, zAcc_)
    plt.title('Noise and Offset Removed: Y Domain Zoomed')
    plt.xlabel('Time (min)')
    plt.ylabel('Acceleration (g)')
    plt.grid()
    plt.xlim()
    plt.ylim(-0.1, 0.1)
    plt.show()
    plt.plot(time, xAcc_, label = 'X')
    plt.plot(time, yAcc_, label = 'Y')
    plt.plot(time, zAcc_, label = 'Z')
    plt.title('Noise and Offset Removed:  X, Y, and Z Domains')
    plt.xlabel('Time (min')
    plt.ylabel('Acceleration (g)')
    plt.legend(loc = 'lower left')
    plt.grid()
    plt.xlim()
    plt.ylim()
    plt.show()
    return(DataSet)

def Validator(DataSet):
    xMean = DataSet["Mean Offset X"]
    yMean = DataSet["Mean Offset Y"]
    zMean = DataSet["Mean Offset Z"]
    xAcc_ = DataSet["Corrected X Accel. (g)"]
    yAcc_ = DataSet["Corrected Y Accel. (g)"]
    zAcc_ = DataSet["Corrected Z Accel. (g)"]
    xMean_ = np.mean(xAcc_)
    yMean_ = np.mean(yAcc_)
    zMean_ = np.mean(zAcc_)
    DataSet["Corrected Mean Offset X"] = xMean_
    DataSet["Corrected Mean Offset Y"] = yMean_
    DataSet["Corrected Mean Offset Z"] = zMean_
    xRMS_ = np.sqrt(xMean_)
    yRMS_ = np.sqrt(yMean_)
    zRMS_ = np.sqrt(zMean_)
    DataSet["Corrected RMS X"] = xRMS_
    DataSet["Corrected RMS Y"] = yRMS_
    DataSet["Corrected RMS Z"] = zRMS_
    xMeanError = (str(abs(xMean)*100) + "%")
    DataSet["X Mean Offset Error"] = xMeanError
    yMeanError = (str(abs(yMean)*100) + "%")
    DataSet["Y Mean Offset Error"] = yMeanError
    zMeanError = (str(abs(zMean - 1)*100) + "%")
    DataSet["Z Mean Offset Error"] = zMeanError
    xMeanError_ = (str(abs(xMean_)*100) + "%")
    DataSet["X Corrected Mean Offset Error"] = xMeanError_
    yMeanError_ = (str(abs(yMean_)*100) + "%")
    DataSet["Y Corrected Mean Offset Error"] = yMeanError_
    zMeanError_ = (str(abs(zMean_)*100) + "%")
    DataSet["Z Corrected Mean Offset Error"] = zMeanError_
    return(DataSet)
    
def Integrator(DataSet):
    
    # Assigning acceleration and time variables
    xAcc_ = DataSet["Corrected X Accel. (g)"]
    yAcc_ = DataSet["Corrected Y Accel. (g)"]
    zAcc_ = DataSet["Corrected Z Accel. (g)"]
    time = DataSet["Time (all)"]
    
    # Integrating the acceleration vectors
    xVelocity = it.cumtrapz(xAcc_, time)
    yVelocity = it.cumtrapz(yAcc_, time)
    zVelocity = it.cumtrapz(zAcc_, time)
    
    # Plotting Velocities in X, Y, and Z
    time = np.resize(time, time.size - 1)
    plt.plot(time, xVelocity, label = 'x')
    plt.plot(time, yVelocity, label = 'y')
    plt.plot(time, zVelocity, label = 'z')
    plt.title('Velocities in X, Y, and Z')
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()
    
    # Creating new dictionary data for velocities
    DataSet["Velocity: X"] = xVelocity
    DataSet["Velocity: Y"] = yVelocity
    DataSet["Velocity: Z"] = zVelocity
    
    # Integrating the velocity vectors
    xLocation = it.cumtrapz(xVelocity, time)
    yLocation = it.cumtrapz(yVelocity, time)
    zLocation = it.cumtrapz(zVelocity, time)
    
    
    # Plotting the location trajectories
    time = np.resize(time, time.size - 1)
    plt.plot(time, xLocation, label = 'x')
    plt.plot(time, yLocation, label = 'y')
    plt.plot(time, zLocation, label = 'z')
    plt.plot(xLocation, yLocation, label = 'xy')
    plt.title('Location Trajectory data')
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.show()
    
    # Creating new dictionary data for trajectories
    DataSet["Location: X"] = xLocation
    DataSet["Location: Y"] = yLocation
    DataSet["Location: Z"] = zLocation
    
    # 3D Trajectory Plotting
    plt.figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
    ax = plt.axes(projection = '3d')
    ax.plot3D(xLocation, yLocation, zLocation, 'red', label = 'Trajectory')
    ax.set_xlabel('X DISTANCE [M]', fontsize = 12)
    ax.set_ylabel('Y DISTANCE [M]', fontsize = 12)
    ax.set_zlabel('Z DISTANCE [M]', fontsize = 12)
    plt.ylabel('Y Distance [m]')
    plt.legend(loc = 'upper left')
    plt.title('Location Trajectory')
    plt.show()

    return(DataSet)
    
#Stationary3 100Hz +- 16Gs October 26 2018.csv
#TestData.csv
#walk around room.csv
#waving it around.csv
DataSet = DataPrep('Stationary3 100Hz +- 16Gs October 26 2018.csv')

print('\n RAW SIGNAL ANALYSIS')
Plotter(DataSet)
DataSet = OffsetCorrection(DataSet)
DataSet = NoiseRemoval(DataSet)

print('\n CORRECTED SIGNAL ANALYSIS')
CorrectedPlotter(DataSet)

print('\n DATA VALIDATION')
Validator(DataSet)

Integrator(DataSet)








