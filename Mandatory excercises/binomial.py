# binomial.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------

from math import factorial

n, k = 14, 3
bcoff1 = 1  # Init 1 to avoid division by zero

# Binomial coefficient as for loop
for j in range(1, n - k + 1):
    bcoff1 *= (k + j) / j

# Binomial coefficient using formula with factorial
bcoff2 = factorial(n) / (factorial(k) * factorial(n - k))

# Print result for comparison
print(bcoff1, bcoff2)


"""
Test run:
>>>python3 binomial.py
364.0 364.0
>>>
"""
