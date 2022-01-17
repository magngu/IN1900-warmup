# factorial.py
# Python 3.10.1
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
from math import factorial


def myfactorial(n):
    "Returns the factorial of n."
    if n == 1:
        return 1
    else:
        return n * myfactorial(n - 1)


def test_myfactorial():
    "Test function for myfactorial()"
    exp = factorial(3)
    act = myfactorial(3)

    success = exp == act
    assert success, f"The factorial is {exp}, but {act} was caluclated."


"""
Test run:
>>>pytest factorial.py
============================= test session starts ==============================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
collected 1 item                                                               

factorial.py .                                                           [100%]

============================== 1 passed in 0.01s ===============================
>>>
"""
