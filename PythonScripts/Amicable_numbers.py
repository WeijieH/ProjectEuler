'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from sympy import primerange



def amicable_numbers(n):
    primes = list(primerange(0, n + 1))
    numbers = set()
    for i in range(2, n):
        s1 = sum(divisors(factorize(i, primes))[:-1])
        if i == s1: #skip perfect number like 6
            continue
        s2 = sum(divisors(factorize(s1, primes))[:-1])
        if s2 == i:
            numbers.add(i)
            numbers.add(s1)
    print(numbers)
    print(sum(numbers))


def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i += 1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))
    return factors

def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return sorted(div)


amicable_numbers(10000)