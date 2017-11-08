'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'
'''


def max_a(p):
    return 1 + int(p * (2 + 2**0.5) / 2)

result = {}
for p in range(1, 1001):
    t = 0
    for a in range(1, max_a(p)):
        for b in range(a, 501):
            c2 = (p - a - b) ** 2
            s = a*a +b*b
            if s > c2:
                break
            elif s == c2:
                t += 1
    if t > 0:
        result[p] = t

print(max(result, key = result.get))