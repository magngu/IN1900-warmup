# statistics.py
# Python 3.10.1
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
import numpy as np
from math import sqrt


def mean(x_list):
    """Calculates mean value of list of numbers."""
    s = 0
    N = len(x_list)
    for x in x_list:
        s += x
    return s / N


def standard_deviation(x_list):
    """Calcualtes standard deviation of a list of numbers."""
    x_mean = mean(x_list)
    x_diff = [(x - x_mean) ** 2 for x in x_list]
    std_dev = sqrt((mean(x_diff)))
    return std_dev


def test_mean():
    """Test funciton for mean() using x_list = [1, 2, 3]"""
    x_list = [1, 2, 3]
    tol = 1e-14
    exp = np.mean(x_list)
    act = mean(x_list)
    success = (exp - act) < tol
    assert success, f"{exp} was expected, but {act} calculated."


def test_standard_deviation():
    """Test funciton for standard_deviation() using x_list = [0.699, 0.703, 0.698, 0.688, 0.701]"""
    x_list = [0.699, 0.703, 0.698, 0.688, 0.701]
    tol = 1e-14
    exp = np.std(x_list)
    act = standard_deviation(x_list)
    success = (exp - act) < tol
    assert success, f"{exp} was expected, but {act} calculated."


"""
Test run:
>>>pytest statistics.py
================================ test session starts ================================
platform darwin -- Python 3.8.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
collected 2 items                                                                   

statistics.py ..                                                              [100%]

================================= 2 passed in 0.12s =================================
>>>
"""
