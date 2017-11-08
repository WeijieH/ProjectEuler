'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

def largest_prime_factor(number):
    if (number < 2):
        return 1
    i = 1
    current_number = number
    while True:
        i += 1
        if not isprime(i):
            continue

        while current_number % i == 0:
            if (i == current_number):
                return i
            current_number = current_number // i



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

print(largest_prime_factor(600851475143))
