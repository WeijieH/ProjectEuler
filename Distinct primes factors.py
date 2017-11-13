'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
'''


from sympy import primerange

limit = 100000

primes = list(primerange(0,limit))

def get_distinct_prime_factors(n, primes):
    result = 1
    for p in primes:
        if p * p > n:
            break
        f = False
        while n % p == 0:
            f = True
            n = n // p
        if f:
            result += 1
    return result

count = 0
target = 4
for n in range(647, 2*limit):
    f = get_distinct_prime_factors(n, primes)
    if f == target:
        count += 1
        if count == target:
            print(n - target + 1)
            break
    else:
        count = 0
