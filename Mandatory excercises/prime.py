# prime.py
# Python 3.10.1
# Author Magnus // Jan 2022
# ------------------------------------------------------------------------------
from math import ceil, sqrt


def is_prime(n):
    """Checks if n is prime. Returns True/False."""
    status = None
    loop_lim = ceil(sqrt(n))
    for i in range(2, loop_lim + 1):
        if n % i == 0:
            status = False
            break

    return status


def factor_num(n, i=2):
    """Factors the n into prime components."""
    lst = []
    while n % i != 0 and i <= n:  # Loop to find the lowest factor
        i += 1

    # Append factor to list and find next factor using recursion
    if n == i:  # Recursive base case
        lst.append(i)
    elif n != i:
        lst.append(i)
        lst = lst + factor_num(n // i)
    return lst


def prime_factorization(n):
    """Factors a number and states if it is a prime."""
    if is_prime(n):
        print(f"{n} is prime")
    else:
        factors = factor_num(n)
        print(f"The factors of {n} are: {factors}")
        return factors


def test_is_prime():
    """Test function for is_prime(n)."""
    exp = False
    act = is_prime(25)
    assert exp == act, f"Expected {exp}, but got {act}"


def test_prime_factorization():
    """Test function for prime_factorization(n)."""
    exp = [2, 2, 5, 5]
    act = prime_factorization(100)
    print(act)
    assert exp == act, f"Expected factors does not mach calculated."


print(is_prime(25))
# prime_factorization(5525612)


"""
Test run:
>>>python3 prime.py
The factors of 5525612 are: [2, 2, 17, 23, 3533]

>>> pytest prime.py
============================================== test session starts ==============================================
platform darwin -- Python 3.10.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
collected 2 items                                                                                               

prime.py ..                                                                                               [100%]

=============================================== 2 passed in 0.01s ===============================================
"""
