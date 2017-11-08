'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def summation_of_primes(n):
    i = 2
    sum = 0
    while i < n:
        if isprime(i):
            sum += i
        i += 1

    return sum


def isprime(n):
    """Returns True if n is prime."""
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 ==0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

print(summation_of_primes(2000000))