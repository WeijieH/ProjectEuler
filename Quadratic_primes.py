'''
Euler discovered the remarkable quadratic formula:

n2+n+41n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤390≤n≤39. However, when n=40,402+40+41=40(40+1)+41n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤790≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+bn2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, aa and bb, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0.
'''

from sympy import primerange

upper_limit = 1000

primes = set(primerange(0, upper_limit**2))
b_primes = list(primerange(0, upper_limit))

result = {}
for a in range(-upper_limit, upper_limit + 1):
    for b in b_primes:
        n = 0
        while n**2 + a * n + b in primes:
            n += 1
        if n > 0:
            result[a * b] = n

m = max(result, key=result.get)
print('{0} : {1}'.format(m, result[m]))
