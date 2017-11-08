'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''


from sympy import primerange

MATH_LIMIT = 28123


def find_abundant_numbers():
    abundant_numbers = set()
    primes = list(primerange(0, MATH_LIMIT + 1))
    for i in range(12, MATH_LIMIT + 1):       
        if (sum_of_divisors(factorize(i, primes)) - i) > i:
            abundant_numbers.add(i)
    abundant_number_sums = set()
    for x in abundant_numbers:
        for y in abundant_numbers:
            s = x + y
            if s <= MATH_LIMIT:
                abundant_number_sums.add(s)
    result = 0
    for i in range(1, MATH_LIMIT + 1):
        if i not in abundant_number_sums:
            result += i
    print(result)


def sum_of_divisors(factors):
    '''
    http://mathworld.wolfram.com/DivisorFunction.html
    '''
    s = 1
    for (p, r) in factors:
        s *= ((p**(r + 1) - 1) // (p - 1))
    return s



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


find_abundant_numbers()