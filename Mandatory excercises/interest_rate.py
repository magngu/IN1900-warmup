# interest_rate.py
# Author Magnus // Des 2021
#------------------------------------------------------------------------------

P = 1000    #initial amount, euros
n = 3       #time in years
r = 5       #interest per year in perent

A = P*(1+r/100)**n

print(A)


#------------------------------------------------------------------------------
'''Execution example:
>>>python3 interest_rate.py
1157.6250000000002
'''