'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def special_Pythagorean_triplet(n):
    max_c = int(2 * (2**0.5 - 1) * n)
    for c in range(n//3, max_c):
        c2 = c**2
        for b in range (1, min(c, n//2)):
            a = n - c - b            
            if a**2 + b**2 == c2:
                return a*b*c
    return 0


print(special_Pythagorean_triplet(1000))