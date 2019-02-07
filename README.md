# MetaMotionR-Accelerometer-Research

# Getting started

The best tool to do heavy data analytics and processing is Anaconda's Spyder. Please refer to https://www.anaconda.com/ for installing an anaconda distribution, or a miniconda distribution. It is a great package manager that comes with Spyder and comes prepackaged with many scientific, data science, and machine-learning libraries. It also comes with a powerful variable exploration utility.

In order to begin analysis with python on 3-axis acceleration data, the following libraries were used:

    # Necessary libraries with subroutines and functions
    import os
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.integrate as it
    import scipy.signal as signal
    
# Jan 29 2019

We ran tests with our newtonian setup on an even surface at 0 degrees offset. A mass of 70g was attached to the cart to ensure a theoretical force of 0.5g to be generated. We ran 2 tests in -X, 2 tests in -Y, and 1 test in +X. A test in -X, and in -Y failed due to erroneous communication between the device and iPhone. Tests were ran at 800Hz +- 4Gs. Additionally, our test in the +X direction was sliced and we focused on the window of data where the cart accelerated (so we deleted the portion of data after the crash) to observe any changes on accurac in 3D trajectories. In the velocity plots it is possible to see a moment of constant acceleration as the slope of the velocity curves suggest there may be a constant gravitational force.

Our results and data can be reviewed in the corresponding Jan 29 2019 Data folder in this repository. PDF files have been generated for each dataset.

Questions:

- is our butterworth (lowpass filter) distorting our data, or helping it?
- should we remove the filter and run the analyzer without any filters? will this be more accurate?
- should we write our own filter? is a windowing average all we need?

# Feb 1 2019

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
    
# Feb 2 2019

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

# Feb 5 2019

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

# Feb 7 2019

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


