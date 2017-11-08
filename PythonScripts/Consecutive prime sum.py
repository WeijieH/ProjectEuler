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
accumulated_sum = [0]
for i in range(len(primes)):
    accumulated_sum.append(accumulated_sum[-1] + primes[i])

consecutive_prime_sum = {}
for i in reversed(range(len(accumulated_sum))):
    for j in range(0, i):
        t = accumulated_sum[i] - accumulated_sum[j]
        if t > limit:
            break
        if binary_search(primes, t) > 0:
            if i - j > 1:
                consecutive_prime_sum[t] = max(
                    i - j, consecutive_prime_sum.get(t, 1))


key = max(consecutive_prime_sum, key=consecutive_prime_sum.get)
print('{0}:{1}'.format(key, consecutive_prime_sum[key]))
