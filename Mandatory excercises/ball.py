# ball.py
# Author Magnus // Des 2021
#------------------------------------------------------------------------------

v0 = 8.2      #start velocity, meter per sec
g  = 9.81     #gravitation, meter per sec^2
t_max  = v0/g #time of maximum height
height = v0*t_max - 0.5*g*t_max**2 #height in meters

print(height)

#------------------------------------------------------------------------------
'''Execution example:
>>>python3 ball.py         
3.4271151885830773
'''