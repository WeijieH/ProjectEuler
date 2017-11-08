'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from math import log


def smallest_multiple(num):
    result = 1
    for i in range(2, num + 1):
        if not isprime(i):
            continue
        result *= i ** int(log(num, i))
    return result


def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


print(smallest_multiple(20))
