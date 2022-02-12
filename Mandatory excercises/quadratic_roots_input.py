# quadratic_roots_inpu.py.py
# Python 3.10.1
# Author Magnus // Feb 2022
# ------------------------------------------------------------------------------

from math import sqrt

# Initiate variables and print header in terminal
values = []
i = 0
print(f'|--------------------------------------------|')
print(f'|----------QUADRATIC EUATION SOLVER----------|')
print(f'|--------------------------------------------|')

# Get user input. Repeats until 3 integers are entered
while i < 3:
    try:
        values.append(int(input(f'    Enter an integer: ')))
        i += 1
    except ValueError:
        print('You did not enter an integer, please try again')

# Calculate answer
a, b, c = values[0], values[1], values[2]
try:
    x1 = (-b + sqrt(b**2 - 4*a*c)) / 2*a
    x2 = (-b - sqrt(b**2 - 4*a*c)) / 2*a
except ValueError:
    print(f'The solution is not in the domain of Real numbers')

# Format the output
if b >= 0 and c >= 0:
    print(f'    Your polynom is {a}x^2 + {b}x + {c} = 0')
elif b >= 0 and  c < 0:
    print(f'    Your polynom is {a}x^2 + {b}x - {c} = 0')
elif b < 0 and c >= 0:
    print(f'    Your polynom is {a}x^2 - {b}x + {c} = 0')
else:
    print(f'    Your polynom is {a}x^2 - {b}x - {c} = 0')

#Print the solution
print(f'|--------------------------------------------|')
print(f'|    SOLUTION: x1 = {x1:4.2f} and x2 = {x2:4.2f}.    |')
print(f'|--------------------------------------------|')



"""
Test run:
>>>python3 quadratic_roots_input.py
|--------------------------------------------|
|----------QUADRATIC EUATION SOLVER----------|
|--------------------------------------------|
    Enter an integer: 1       
    Enter an integer: 10
    Enter an integer: 2
    Your polynom is 1x^2 + 10x + 2 = 0
|--------------------------------------------|
|    SOLUTION: x1 = -0.20 and x2 = -9.80.    |
|--------------------------------------------|
"""
