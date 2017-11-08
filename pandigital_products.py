'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''


def isPandigital(m, n, p):
    s = str(m) + str(n) + str(p)
    if len(s) != 9 or '0' in s:
        return False
    return len(set(s)) == 9

result = set()
for m in range(2, 100):
    ns = 123 if m > 9 else 1234
    ne = 10000 // m + 1
    for n in range(ns, ne):
        p = m * n
        if isPandigital(m, n, p):
            result.add(p)

print(result)
print(sum(result))
