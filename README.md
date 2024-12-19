# MetaMotionR-Accelerometer-Research

Table of Contents
=================
* [Getting Started](#Getting-started)
* [Jan 29 2019](#Jan-29-2019)
* [Feb 1 2019](#Feb-1-2019)
* [Feb 2 2019](#Feb-2-2019)
* [Feb 5 2019](#Feb-5-2019)
* [Feb 7 2019](#Feb-7-2019)
* [Feb 13 2019](#Feb-13-2019)
* [Feb 15 2019](#Feb-15-2019)
* [Feb 22 2019](#Feb-22-2019)
* [March 26 2019](#March-26-2019)
* [April 1 2019](#April-1-2019)
* [April 8 2019)(#April-8-2019)

## Getting started

This research project is focused on 3-axis data produced from a MetaMotionR device to explore the capabilities of accelerometer hardware. The motive for this research is to implement a data fusion application using 3-axis GPS data to couple together into a predictive Kalman filter. The device can be found at https://mbientlab.com/metamotionr/.

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/metamotionr.PNG)


The best tool to do heavy data analytics and processing is Anaconda's Spyder. Please refer to https://www.anaconda.com/ for installing an anaconda distribution, or a miniconda distribution. It is a great package manager that comes with Spyder and comes prepackaged with many scientific, data science, and machine-learning libraries. It also comes with a powerful variable exploration utility.

In order to begin analysis with python on 3-axis acceleration data, the following libraries were used:

    # Necessary libraries with subroutines and functions
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.integrate as it
    import scipy.signal as signal
    
To get access to the data from a .csv file, the following routine can be used:
    
    filename = 'fileName.csv'
    # Variable preparation, print analysis to console
    print('\n *** FILE METRICS ***')
    print(filename, 'is being analyzed')
    allData = pd.read_csv(filename)
    xAcc = allData.loc[:, 'x-axis (g)'].values
    yAcc = allData.loc[:, 'y-axis (g)'].values
    zAcc = allData.loc[:, 'z-axis (g)'].values
    time = allData.loc[:, 'elapsed (s)'].values
    timeMin = time / 60 # convert to minutes
    
## Jan 29 2019

We ran tests with our newtonian setup on an even surface at 0 degrees offset. A mass of 70g was attached to the cart to ensure a theoretical force of 0.5g to be generated. We ran 2 tests in -X, 2 tests in -Y, and 1 test in +X. A test in -X, and in -Y failed due to erroneous communication between the device and iPhone. Tests were ran at 800Hz +- 4Gs. Additionally, our test in the +X direction was sliced and we focused on the window of data where the cart accelerated (so we deleted the portion of data after the crash) to observe any changes on accurac in 3D trajectories. In the velocity plots it is possible to see a moment of constant acceleration as the slope of the velocity curves suggest there may be a constant gravitational force.

Our results and data can be reviewed in the corresponding Jan 29 2019 Data folder in this repository. PDF files have been generated for each dataset.

Questions:

- is our butterworth (lowpass filter) distorting our data, or helping it?
- should we remove the filter and run the analyzer without any filters? will this be more accurate?
- should we write our own filter? is a windowing average all we need?

The butterworth filter in question is:

    # Setting up Butterworth lowpass filter (windowing average function)
    N = 2 # Filter order
    Wn = 0.4 # Cutoff frequency 0 < Wn < 1
    B, A = signal.butter(N, Wn, output = "ba")

    # Apply filter and plot X signal
    xMean = []
    for i in range(len(xAcc_)):
        xMean.append(np.mean(xAcc_))
    xAcc_ = signal.filtfilt(B, A, xAcc_)
    plt.figure(figsize = (10, 6))
    plt.plot(time, xAcc_, label = "smooth", linewidth = 2.25)
    plt.plot(time, xAcc, label = "raw", linewidth = 1.5, alpha = 0.5, color = "r")
    plt.plot(time, xMean, label = "avg offset", linewidth = 2, color = "black")
    plt.legend(loc = "upper left")
    plt.grid()
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (g)")
    plt.title("Denoised X Acceleration")
    plt.show()

The same routine can be used for the Y and Z axis signals.

## Feb 1 2019

We determined that we need to zoom in on the data where our accelerometer is actually undergoing newtonian motion in our setup. A lot of our datasets from Jan 29, 2019 showcase what happened in acceleration over a very long time interval. We need to cut out the 0.5s window of time where the action happened and apply our signal processing exactly to that section of data. This will require manipulating our algorithm and slicing up the raw data to generate the analytics we are after.

We also intend to perform some more stationary tests at lower data rates, as well as continue to test the track upcoming on Feb 5, 2019. With the new insights from the meeting today, we hope to accelerate our preparation for kalman filter research and implementation.

Update:

- the algorithm has been edited to edition 4.0 which is more suitable for editing variables and data in spyder
- some data has been sliced to isolate the interval in which the newtonian motion occurs on the track
- the trajectories produced by this isolated interval isn't succesful in showcasing movement as expected on the track
- the z axes have been zeroed out since we are mainly interested in x and y
- the x velocity has a behaviour as expected in most tests, but does not seem to be great enough to generate trajectories
- THE LOWPASS FILTER HAS BEEN REMOVED
    - the lowpass filter was preventing the expected behavior in velocity being shown, the filter has been deprecated and commented out for potential use later if necessary
    
## Feb 2 2019

One more stationary test was conducted and the results show that drift occurs over time. This allows us to determine how long we are willing to utilize the accelerometer before resetting it with GPS data as we go forward. In addition, the test ran last week in the -X direction produced quality data, and so that was processed again today without a lowpass filter and the Z axis was zeroed as well. This showed that we had a small portion in time where acceleration was as expected, however the output in trajectory is confusing as it shows that no motion occured. Acceleration and velocity seem to behave as expected, but not the location trajectory.

- Stationary test velocity drift

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%202%202019%20Data/Semester%202%20Stationary%20Test1%20Velocity.PNG)

- Stationary test trajectory drift

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%202%202019%20Data/Semester%202%20Stationary%20Test1%20Trajectory.PNG)

- -X direction test acceleration

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%202%202019%20Data/Semester%202%20-X%20Test%20X%20Acceleration.PNG)

- -X direction test velocity

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%202%202019%20Data/Semester%202%20-X%20Test%20Velocities.PNG)

- -X direction test trajectory

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%202%202019%20Data/Semester%202%20-X%20Test%20Trajectory.PNG)

To Review:
- the integration performed in the algorithm
- more newtonian tests with different masses (to test for accelerometer sensitivity)
- come up with simple kalman filter examples https://filterpy.readthedocs.io/en/latest/kalman/KalmanFilter.html https://pykalman.github.io/ https://www.mathworks.com/help/control/ug/kalman-filtering.html

## Feb 5 2019

Since the group could not meet in the lab today, I ran a quick test with the accelerometer at home. The goal was to try and prove that the device and algorithm could produce a result that showed the device moved in the +X direction as seen in reality. I swung the accelerometer approximately 0.5m (by eyeballing) in the +X direction while trying to minimize movement in Y and Z. The tests showed an initial +-2G spike, and then a realistic 2s interval where 0-0.5G forces were detected. The whole dataset was pumped through the algorithm and the trajectory showed a total movement in +X by about 0.5m. There was some movement in Y and Z, which was later ignored by setting the Y and Z axes to zero, and also slicing down to the interval in time where relevant motion occured. After, the location trajectory produced seemed accurate and showed that I moved the device by ~0.5m by swinging my arm. This confirms that it is possible that our newtonian setup isn't configured to succesfully collect data from the device for a number of hypotheses. Some of these are:

1. Is our track too short?
2. Do we have too much mass attached to the cart?
3. Are we recording for too short a period?
4. Is the device not sensitive enough for our test?

Some considerations for future testing:
- slow down the cart by adding mass to the cart, or reducing the mass on the string
- increase the length of the track
- collect video footage of the test and setup to study when comparing to signals of gravitational force

Below are results pertaining to the test proving truthful location tracking:

- Velocity of edited data:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%205%202019%20Data/velocity%20of%20sliced%20data.png)

- Trajectory of edited data:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%205%202019%20Data/location%20trajectory%20of%20sliced%20data.png)

## Feb 7 2019

Seven tests were conducted today to collect more data for processing and analysis. The goal was to produce data under a controlled newtonian setup to prove truthful location tracking, as opposed to moving the device in my hand arbitrarily. Unfortunately, the data collected was not conclusive since there were no observable constant forces or sensible velocities derived from any of the datasets. In addition, the tests were slowed down by adding a 40g mass to the cart in most of the tests and this still did not result in analytics that make sense. 

One test in the positive X direction, with a 40g mass attached to the cart was inspected further. I zoomed sliced the dataset down to the time interval of interest and zeroed out the z-axis. It showed that the device moved less than 20cm, which does not makes sense since the track is 140cm in length. This means that we are still relying on the data generated from the movement of my arm on Feb 5 2019 (see above). 

These findings lead to two possibilities
- the newtonian setup is still not optimized to collect controlled data 
- the device produces error so quickly that we only achieve about 10-20cm of accurate location tracking
    - if this is true, then we can continue to develop a new script that will fuse GPS data in a kalman filter. However, this conclusion is a hypothesis and will require further investigation to prove

To be thorough, below are a few screenshots highlighting the data that was edited and sliced for further inspection (positive X direction test with 40g mass on the cart to slow it down):

- Original accelerations:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/original%20accelerations.png)

- Original velocities:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/original%20velocities.png)

- Original trajectory:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/original%20trajectory.png)

- Sliced interval X Acceleration:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/sliced%20interval%20x%20acceleration.png)

- Sliced interval velocities:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/sliced%20interval%20velocities.png)

- Sliced interval trajectory:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%207%202019%20Data/sliced%20interval%20trajectory.png)

## Feb 13 2019

It was determined in the latest meeting that the newtonian setup in lab is not optimal for data collection with the accelerometer, and that the test conducted on Feb 5 is enough proof that the device and algorithm are ready for new milestones. This is due to the fact that the track and cart used in the setup introduce a lot of random jitter that masks the acceleration we are seeking.

Our tests today involved walking in a straight line outdoors, accounting for X and Y axes data and zeroing out Z. We are attaching the accelerometer to a mobile device to log GPS and acceleration data simultaneously. 

A total of 12 trials were performed, and the behavior observed in each of them was rather consistent. However, inspection with Anaconda's Spyder led me to the conclusion that the first trial was the best trial to showcase results with. The other trials had some anomalies in their acceleration that suggests we may need to re-evaluate how we conduct our field tests.

Ultimately, in trial 1, the accelerations appear as:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial%201%20accelerations.png)

Note that the X acceleration resembles behaviour of a human walking at a steady pace. The device was oriented in +X propagation, so it is also good news that the Y acceleration hovers around 0 and contributes less to the integration (which will be shown below). 

Here is the result of velocity after performing integration (remember that Z is zeroed out):

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial%201%20velocities.png)

It is unrealistic that the velocity reaches up to and above 5 (m/s). This suggests that there is significant error propagation, and therefore a large drift in the final data. This means we need to be resetting the algorithm in intervals to prevent large error propagation and retain the validity of the displacement we are seeking. Below, is the location trajectory, 2d trajectory, and displacement.

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial1%20location%20trajectory.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial%201%202d%20trajectory.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial%201%20displacement.png)

Finally, it should be noted that the location in which this test was conducted was a pavement right next to the Goldwater Center at Arizona State University. For the record, this plot is not final and is a work in progress (the plot is not to scale, and is not oriented as such to map the location trajectory in 2D properly - this is another coding challenge to be tackled in the future). 

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2013%202019%20Data/trial%201%20map%20-%20work%20in%20progress.png)

Considerations for the next week:
- Should we filter the data in X or Y, or both?
    - Are we ready to conditionally reset the integration process by intervals?
- Do we need to observe stationary data to determine our time intervals for resetting the integration?
- How long (distance) is the path we conducted our trials upon?
    - we showed 100m of drift in our first trial, this is a lot and potentially double the distance we covered
- How well does our data match up with GPS coordinates (or GPS coordinates converted to meters of displacement)
- How can we scale a map for our data to be plotted upon (final product/demo considerations)
- Why is our initial and ending points not at 0G? Why are they constant and hovering above 0?
- Do we need to worry about offset removal?
- Will lowpass filtering help or corrupt our new data?
    - Our lowpass filter was previously deprecated, but these new field tests indicate potential for improved data by way of filtering/denoising
        
## Feb 15 2019

In the meeting today, it was determined that we need to sort out the following items:
- determine the offset values from the accelerometer by stationary tests
- remove the offset and ensure we generate a truthful trajectory
- make comparisons to GPS data and validate our coordinate conversions

Tests were run on 3 stationary tests and I found that the offset values in each axis vary. This means that using one stationary test is not a deterministic method for removing offsets from field tests. Since we are not tracking location in Z, we are ignoring Z offsets.

#### Stationay Test Results (No Time Variance)

| Test          | Data Rate     |  X Offset     |  Y Offset     |  
| ------------- | ------------- | ------------- | ------------- |
| 1             | 800 Hz        | -0.0183406    | 0.0897763     |        
| 2             | 100 Hz        | -0.0054300    | 0.0447664     |          
| 3             | 50 Hz         | 0.0318137     | 0.0915871     |      

Removing the offsets in our first trial's dataset using the values from Test 1, 2, and 3 do not yield results that are promising. They do not alter the data as such to show that a distance of 20 meters was walked in the +X direction. It seems that offset values are unique to the datasets and that we cannot rely on stationary tests to determine offset corrections.

That being said, I performed analytics with the dataset of Trial 1 from Feb 13, and found that by applying an offset correction of -0.13 in X, and -0.02 in Y yielded a trajectory that showed roughly 20 meters of movement in +X, and a drift of about 5 meters in +Y. This is much more representative of reality, but since this was achieved by eyeballing an offset value it will require further inspection (it is possible that this is an inconclusive result). Moreover, the offset values to be used in new field tests will also vary, so a method to determine these values will need to be developed in the future.

For now, the results achieved by eyeball and trial and error are shown below:

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/accelerations.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/offsets%20removed.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/velocities.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/2d%20trajectory.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/displacement.png)

With further inspection I then determined that an offset removal of 0.12 in X and 0.03 in Y yielded even better results. I then also applied a lowpass filter to the initial and tail end of the waveforms, as well as to the whole waveform. Both of these filters are a lowpass filter that acts as a windowing average and aims to denoise the signals. The improved results are shown below, along with a snippet showcasing the filter (the algorithm can be viewed in the Feb 15 2019 Data folder):

    #==============================================================================
    # Butterworth Filtering X and Y Acceleration
    #==============================================================================
    N = 2 # Filter order
    Wn = 0.001 # Cutoff frequency 0 < Wn < 1
    B, A = signal.butter(N, Wn, output = 'ba')
    xAcc[:2000] = signal.filtfilt(B, A, xAcc[:2000])
    yAcc[:2000] = signal.filtfilt(B, A, yAcc[:2000])
    xAcc[29000:] = signal.filtfilt(B, A, xAcc[29000:])
    yAcc[29000:] = signal.filtfilt(B, A, yAcc[29000:])
    N = 2
    Wn = 0.01
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
    plt.ylim(-0.3, 0.3)
    plt.grid()
    plt.show()

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/denoised.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/denoised%20with%20offset.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/denoised%20velocities.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/denoised%20trajectory.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/denoised%20displacement.png)

Finally, attempts were made to compare the accelerometer results to that of the GPS data. Unfortunately the conversion of the results gave data in the form of change in distance at each iteration, and therefore are not plottable coordinates. Below is a preview of the format of the GPS data that has been provided. More work will have to be done to ensure we can develop plottable coordinates. 

<img src="https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%2015%202019%20Data/Screen%20Shot%202019-02-16%20at%204.31.55%20PM.png" width="200" height="400">

Goals for the next week:
- obtain more GPS data and develop plottable coordinates
- run comparisons to accelerometer results and GPS data
- determine if more revisions need to be done on our signal processing or algorithm

## March 26 2019
Field tests were conducted today where the accelerometer device logs data along with a GPS mobile application for the purpose of cross-checking trajectory results. The GPS application's repository is available for further investigation at:

https://github.com/andrejandre/Custom-GPS-Logger

The GPS mobile application allowed for GPS coordinates to be logged at a custom frequency. Later, the .csv logs generated from the application were taken into Excel and transformed into displacement and position data via Polar and Cartesian relationships.

Analysis of one trial showed that the accelerometer roughly shows behaviour of the expected trajectory, but is still drfting far away from the GPS. Below are plots showcasing proof of this. Further analytics are included in the corresponding March 26 2019 Data folder.

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/March%2026%202019%20Data/X%20and%20Y%20Accel.%20Denoised.PNG)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/March%2026%202019%20Data/X%20and%20Y%20Accel.%20Offset%20Removeed.PNG)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/March%2026%202019%20Data/X%20and%20Y%20Velocities.PNG)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/March%2026%202019%20Data/Final%20Trajectories.PNG)

## April 1 2019
The goal of today was to take a step back and determine a truthful offset value by conducting 10 trials using stationary tests. This was run through a quick script to handle a mean calculation and compile offsets from each trial. The table below highlights the significant results of these tests, and showcases the value being used for further testing. After this stationary offset analysis was performed, the offset values for X and Y were used again in the original algorithm to reproduce field tests with the confidence that new results are truthful.

Note: all tests were normalized to 100s time intervals to remove time variance.

| Trial         | Data Rate     |  X Offset     |  Y Offset     | 
| ------------- | ------------- | ------------- | ------------- |
| 1             | 100 Hz        |0.01642661141804789|0.1268228360957643               |        
| 2             | 100 Hz        |0.018451633279191484               | 0.1177041147807255               |          
| 3             | 100 Hz        | 0.014438678305233375              |0.13036274861493086               | 
| 4             | 100 Hz        |0.018654079461365013               |  0.1309286689744974             | 
| 5             | 100 Hz        | 0.01305516395954643              |0.125916717744407               | 
| 6             | 100 Hz        | 0.035122338807785904              |  0.10392883211678834              | 
| 7             | 100 Hz        |   0.03539309699214458             | 0.10671879197362531              | 
| 8             | 100 Hz        |0.035679390279947654               |  0.10667736350969052             | 
| 9             | 100 Hz        | 0.027462606013878187              |0.1206620406065279               | 
| 10            | 100 Hz        |     0.022448598130841123           | 0.11983945260347129              | 

To further validate these tests, the pdf files and screenshots can be viewed for each corresponding stationary trial to observe the signal characteristics (see the corresponding April 1 2019 data folder in the main branch).

The table below shows the mean offset values for both domains derived from the 10 trials conducted above. These values are what are being used in all future data analytics.

| Mean Offset X | Mean Offset Y |
| ------------- | ------------- |
| 0.02371321966479816 | 0.11895615670204282 |

asdasdasd
asdasdasd
asdasdasd

Now, the portion of code in the algorithm applying offset removal appears as follows:

    #==============================================================================
    # Removing offsets
    # The values used to remove offset are determined by 10 stationary tests 
    # which study the variance in X and Y offset and determine the mean offset 
    # to apply to the signals for most truthful results
    #==============================================================================
    xAcc = xAcc - 0.02371321966479816
    yAcc = yAcc - 0.11895615670204282


In addition to studying the mechanical offsets of the device, an innovative idea was developed to begin further improving upon the resutls of the accelerometer trajectories. The current understanding is that the accelerometer can reliably report about 5 seconds worth of meaningful location data, however the integration in the algorithm is sweeping the whole range of acceleration data and propagating massive amounts of exponential drift. To avoid this, an algorithm is being scripted to integrate the acceleration in 5 second intervals. The integration for velocity is reset every 5 seconds, and the integration for position/displacement will be reset every 5 seconds as well. The goal is to remove the long term propagation of drift error in the results and showcase a trajectory path that could potentially be better than GPS (especially if lowpass filtering is applied on the final data).

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
    # Integrating flat velocity to generat displacement/position
    #==============================================================================
    xDis = it.cumtrapz(flatVelX)
    yDis = it.cumtrapz(flatVelY)

This algorithm will be built upon, optimized, and refined going forward. It is still incomplete and more trials and analytics need to be done to validate results being obtained with the script.

## April 8 2019
