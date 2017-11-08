'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''


from sympy import primerange


def generate_number(digits, index):
    result = 0
    m = 1
    for i in range(index + 1):
        result += digits[i] * m
        m *= 10
    return result


def remove_from_right(n):
    n = str(n)
    result = set()
    for i in range(1, len(n)):
        result.add(int(n[:-i]))
    return result


limit = 1000000
primes = set(primerange(0, limit))
l = len(str(limit))


digits = [1] * l
# last digit has to be 3 or 7
digits[0] = 3


selected_primes = set()
index = 1
while index >= 0 and index < l and digits[0] < 10:
    current_number = generate_number(digits, index)
    if current_number in primes:
        index += 1
        selected_primes.add(current_number)
    else:
        if digits[index] >= 9:
            digits[index] = 1
            index -= 1
        if index == 0:
            # last digit has to be 3 or 7
            digits[index] += 4
        else:
            digits[index] += 1

truncatable_primes = set()
for prime in selected_primes:
    if prime < 10:
        continue
    if remove_from_right(prime) < primes:
        truncatable_primes.add(prime)
print(truncatable_primes)
print(sum(truncatable_primes))
