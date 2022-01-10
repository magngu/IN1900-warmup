# sumint.py
# Python 3.10.1
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------


def sumint(n):
    """Returns sum of integers up to n."""
    s = 0
    for i in range(n + 1):
        s += i
    return s


def sumint2(n):
    """Returns sum of integers up to n using n(n+1)/2"""
    return (n * (n + 1)) / 2


def test_sumint():
    """Test function for sumint() using n=3"""
    exp = 6
    act = sumint(3)
    success = exp == act
    msg = f"Value {exp} expected, but {act} computed."
    assert success, msg


def test_sumint2():
    """Test function for sumint2() using n=3"""
    exp = 6
    act = sumint2(3)
    success = exp == act
    msg = f"Value {exp} expected, but {act} computed."
    assert success, msg


"""
Test run:
>>>pytest sumint.py
============================= test session starts =============================
platform darwin -- Python 3.8.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~~~~~~~~~~~~~~~~~~~~s
collected 2 items                                                             

sumint.py ..                                                            [100%]

============================== 2 passed in 0.01s ==============================
>>>
"""
