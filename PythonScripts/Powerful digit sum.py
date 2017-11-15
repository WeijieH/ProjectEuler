'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''


m = 0
ma = 0
mb = 0

for a in range(1, 100):
    for b in range(1, 100):
        c = sum([int(i) for i in str(a**b)])
        if c > m:
            m = c
            ma = a
            mb = b

print('{0}**{1}:{2}'.format(ma, mb, m))
