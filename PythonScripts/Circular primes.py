'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

from sympy import primerange

limit = 1000000


primes = set(primerange(0, 10 * limit))


def generated_rotated_numbers(n):
    numbers = {n}
    n = str(n)
    for i in range(1, len(n)):
        s = n[i:] + n[:i]
        numbers.add(int(s))
    return numbers


result = set()
for prime in primes:
    if prime in result: continue
    all_numbers = generated_rotated_numbers(prime)
    if prime < limit and all_numbers < primes:
        result.add(prime)

print(len(result))
