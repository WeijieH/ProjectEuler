'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

lookup = {0: 0}
for i in range(1, 10):
    lookup[i] = 9 * i * 10 ** (i - 1) + lookup[i - 1]


def g(number, lookup):
    for i in range(len(lookup)):
        if lookup[i] > number:
            break
    return i


def find_ith_digit(ith):
    a = g(ith, lookup)
    target = 10**a - 1 - (lookup[a] - ith) // a
    offset = 1 + (lookup[a] - ith) % a
    return int(str(target)[-offset])


d = [1, 10, 100, 1000, 10000, 100000, 1000000]
print([find_ith_digit(x) for x in d])
