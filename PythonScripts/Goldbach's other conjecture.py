'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''


from primesieve import primes

limit = 10000


def conjecture_check(n, prime_numbers, prime_lookup, twice_a_square):
    for p in prime_numbers:
        if p > n:
            return False
        for j in range(1, len(twice_a_square) + 1):
            t = n - twice_a_square[j]
            if t < 2:
                break
            if t in prime_lookup:
                return True


prime_numbers = primes(limit)
prime_lookup = set(prime_numbers)

twice_a_square = {}
for i in range(1, 100):
    twice_a_square[i] = 2 * i * i


for i in range(1, limit):
    n = 2 * i + 1
    if n in prime_lookup:
        continue
    if not conjecture_check(n, prime_numbers, prime_lookup, twice_a_square):
        print(n)
        break
