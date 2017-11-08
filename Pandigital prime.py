'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

from sympy import primerange


largest_primes = reversed(list(primerange(1234567, 7654321)))


def isPandigital(n):
    n = str(n)
    return set(int(x) for x in n) == set(range(1, len(n) + 1))


for prime in largest_primes:
    if isPandigital(prime):
        print(prime)
        break
