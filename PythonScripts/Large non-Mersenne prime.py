'''
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.

Find the last ten digits of this prime number.
'''


def last_ten_digits_mul(a, b):
    n = a * b
    n = n % 10000000000
    return n


result = 1
for _ in range(7830457):
    result = last_ten_digits_mul(2, result)

result = last_ten_digits_mul(28433, result)
result += 1
print(result)
