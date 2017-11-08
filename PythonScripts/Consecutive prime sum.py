'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

from sympy import primerange


def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   
                break        
            lower = x
        elif target < val:
            upper = x
    return -x


limit = 1000000
primes = list(primerange(0, limit))
accumulated_sum = [2]
for i in range(1, len(primes)):
    accumulated_sum.append(accumulated_sum[-1] + primes[i])

consecutive_prime_sum = {}
for i in range(len(accumulated_sum)):
    max_prime_to_search = limit - accumulated_sum[i]
    

print(consecutive_prime_sum)
