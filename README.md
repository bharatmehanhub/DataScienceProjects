## sklearn-classifiers

This repository is to share my work on basic machine learning
classifiers provided by sklearn.

These are really useful tools once we understand what exactly each of
them does. I have tried to explain the functionality of each of these
classifiers by taking a simple example and drawing a decision boundary
and predictions on test data set using visual images:

# The story:

A car is on its journey through rocky roads to reach a random city A. On
its way, the vehicle faces two types of variations in the structure and
alignment of the road which result in the change of speed as below:

i) Gradient or slope of the road (grad).  
ii) Bumpiness on the road (bumpiness).

The car is already running late and so driver has to driver faster
wherever possible without damaging the wheels of the car. After 4 hour
of tough journey, lets assume that the driver reached city A in time. We
have collected the data from this journey which will represent the 'Test
Data' in our project.

Now, driver has to make a move for city B which is 1 hour away from city
A. Let's assume that even this time it is the same kind of the road that
vehicle is going to face.

# Problem Statement:

We have to predict the kind of speed the driver should follow (Slow or
Fast) so that he does not have to make any effort on his own to decide  
whether he should slow down the car or not. As this is a binary
classification problem, we haven't defined the speed in numbers but just
in two categories.

We will use different types of classifiers available in sci-kit learn
(can easily figure out from the names of the directories available)  
to predict this binary variable (Slow or Fast) using the two features
(gradient and bumpiness) for the journey from city A to city B.

Keenly observe the decision boundary created by each of these
classifiers

Note: Labels 1 corresponds to driving 'Slow' and 0 corresponds to
driving 'Fast'.

Enjoy !!!
