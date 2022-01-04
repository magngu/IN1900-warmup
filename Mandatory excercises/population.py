# population.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
import math


def population(B, C, k, t):
    """
    Returns population after t hours.

    B: carrying capacity
    C: eqation constant
    k: growth factor
    t: time in hours, float

    returns float
    """
    return B / (1 + C * math.e ** (-k * t))


# Given variables
B = 50000  # carrying capacity
k = 0.2  # growth factor per hour^-1
N0 = 5000  # initial condition at t=0
C = B / N0 - 1  # Find C. t=0 --> e^(-kt) = 1

# Find bacteria in colony after 24 hours
N24 = population(B, C, k, 24)
print(N24)
