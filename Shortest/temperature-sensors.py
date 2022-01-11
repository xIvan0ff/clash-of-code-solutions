# Description
# Our reactor is equipped with four temperature sensors. It is common for one or more sensors to fail between two maintenance and refueling outages.
# It was determined by engineering that the second maximum value is the most representative and envelope value to protect the reactor. You need to code an algorithm that returns the second maximum so the control and protection system of the reactor become more fault tolerant.

# Input
# line 1 : N the number of measurement point
# line N: A list of four integers corresponding to sensor measurements in degree Celsius.

# Output
# Line N : for each line given as input return the second maximum value.

# 59 CHARACTERS

I=input
I()
while 1:print(sorted(map(int,I().split()))[-2])
