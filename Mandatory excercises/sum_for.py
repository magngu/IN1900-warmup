# sum_for.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------

s = 0
M = 3

for k in range(1, M + 1):
    s += 1 / ((2 * k) ** 2)

print(s)

"""
Errors corrected:
    Line 8: Adjusted range() to not start at zero to avoid division by zero
    Line 8: Changed name of selected element to k
    Line 9: Put parenthesis around (2*k) to raise the whole expression **2

Test run:
>>>python3 sum_for.py
0.3402777777777778
>>>
"""
