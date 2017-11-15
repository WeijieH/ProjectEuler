'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''


from math import log10

result = 0
for n in range(1, 10):
    b = log10(n)
    p = 1
    while True:
        d = p * b
        if d >= p - 1:
            result += 1
        else:
            break
        p += 1

print(result)
