'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def ith_prime(i):
    count = 0
    n = 1
    while count < i:   
        n += 1   
        if isprime(n):
            count += 1
            continue    
    return n



def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
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

print(ith_prime(10001))