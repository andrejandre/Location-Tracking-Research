# MetaMotionR-Accelerometer-Research

# Jan 29 2019:

We ran tests with our newtonian setup on an even surface at 0 degrees offset. A mass of 70g was attached to the cart to ensure a theoretical force of 0.5g to be generated. We ran 2 tests in -X, 2 tests in -Y, and 1 test in +X. A test in -X, and in -Y failed due to erroneous communication between the device and iPhone. Tests were ran at 800Hz +- 4Gs. Additionally, our test in the +X direction was sliced and we focused on the window of data where the cart accelerated (so we deleted the portion of data after the crash) to observe any changes on accurac in 3D trajectories. In the velocity plots it is possible to see a moment of constant acceleration as the slope of the velocity curves suggest there may be a constant gravitational force.

Our results and data can be reviewed in the corresponding Jan 29 2019 Data folder in this repository. PDF files have been generated for each dataset.

Questions:

- is our butterworth (lowpass filter) distorting our data, or helping it?
- should we remove the filter and run the analyzer without any filters? will this be more accurate?
- should we write our own filter? is a windowing average all we need?

# Feb 1 2019:

We determined that we need to zoom in on the data where our accelerometer is actually undergoing newtonian motion in our setup. A lot of our datasets from Jan 29, 2019 showcase what happened in acceleration over a very long time interval. We need to cut out the 0.5s window of time where the action happened and apply our signal processing exactly to that section of data. This will require manipulating our algorithm and slicing up the raw data to generate the analytics we are after.

We also intend to perform some more stationary tests at lower data rates, as well as continue to test the track upcoming on Feb 5, 2019. With the new insights from the meeting today, we hope to accelerate our preparation for kalman filter research and implementation.
