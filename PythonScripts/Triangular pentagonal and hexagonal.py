'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''


def triangle_number(n):
    return n * (n + 1) // 2


def pentagonal_number(n):
    return n * (3 * n - 1) // 2


def hexagonal_number(n):
    return n * (2 * n - 1)


limit = 100000

pentagonal_numbers = set()
hexagonal_numbers = set()

np = 166
nh = 144
for _ in range(limit):
    pentagonal_numbers.add(pentagonal_number(np))
    hexagonal_numbers.add(hexagonal_number(nh))
    nh += 1
    np += 1

nt = 286
for _ in range(limit):
    n = triangle_number(nt)
    if n in pentagonal_numbers and n in hexagonal_numbers:
        print('T{0} = {1}'.format(nt, n))
    nt += 1
