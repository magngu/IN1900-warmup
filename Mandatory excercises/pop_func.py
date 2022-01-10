# pop_func.py
# Python 3.10.1
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
from math import exp


def population(t, k=0.2, B=50000, C=9):
    """Calculates populations size at time t."""
    return B / (1 + C * exp(-k * t))


p = 48  # time period in hours
n = 12  # number of intervals
h = int(48 / 12)  # interval length
t_list = [t for t in range(0, 48 + 1, h)]

# Print table with values
print("   t |  N")
print("--------------")
for t in t_list:
    N = int(population(t))
    print(f"|{t:3} | {N:5} |")
print("--------------")


"""
Test run:
>>>python3 pop_func.py
   t |  N
--------------
|  0 |  5000 |
|  4 |  9912 |
|  8 | 17748 |
| 12 | 27526 |
| 16 | 36580 |
| 20 | 42924 |
| 24 | 46551 |
| 28 | 48389 |
| 32 | 49263 |
| 36 | 49666 |
| 40 | 49849 |
| 44 | 49932 |
| 48 | 49969 |
--------------
>>>
"""
