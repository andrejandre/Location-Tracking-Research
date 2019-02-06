# MetaMotionR-Accelerometer-Research

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

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%205%202019%20Data/velocity%20of%20sliced%20data.png)

![alt text](https://github.com/andrejandre/MetaMotionR-Accelerometer-Research/blob/master/Feb%205%202019%20Data/location%20trajectory%20of%20sliced%20data.png)
