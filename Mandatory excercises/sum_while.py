# sum_while.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------

s = 0
M = 3
i = 1

while i <= M:
    s += 1 / ((2 * i) ** 2)
    i += 1

print(s)

"""
Test run:
>>>python3 sum_while.py
0.3402777777777778
>>>
"""
