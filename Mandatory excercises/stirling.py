# stirling.py
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
from math import factorial, log

# Generate list with ln(x!) and sterling approximation
i = [x for x in range(500, 10500, 500)]
fact = [log(factorial(x)) for x in i]
aprx = [x * log(x) - x for x in i]

# Print formatted list
print(f"      X   | FACTORIAL | STERLING APPRX")
for x, a, b in zip(i, fact, aprx):
    print(f"{x:9} | {a:9.1f} | {b:9.1f}")


"""
Test run:
>>>python3 stirling.py
      X   | FACTORIAL | STERLING APPRX
      500 |    2611.3 |    2607.3
     1000 |    5912.1 |    5907.8
     1500 |    9474.4 |    9469.8
     2000 |   13206.5 |   13201.8
     2500 |   17064.9 |   17060.1
     3000 |   21024.0 |   21019.1
     3500 |   25066.8 |   25061.8
     4000 |   29181.3 |   29176.2
     4500 |   33358.4 |   33353.2
     5000 |   37591.1 |   37586.0
     5500 |   41874.0 |   41868.8
     6000 |   46202.4 |   46197.1
     6500 |   50572.4 |   50567.1
     7000 |   54981.0 |   54975.7
     7500 |   59425.3 |   59419.9
     8000 |   63903.0 |   63897.6
     8500 |   68411.9 |   68406.5
     9000 |   72950.3 |   72944.8
     9500 |   77516.4 |   77510.9
    10000 |   82108.9 |   82103.4
>>>
"""
