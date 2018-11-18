'''
https://projecteuler.net/problem=108
'''


def solution_count(n):
    count = 0
    for x in range(n + 1, 2 * n + 1):
        y = x * n / (x - n)
        if y.is_integer():
            count += 1
    return count


i = 1000
while True:
    result = solution_count(i)
    if result > 1000:
        print(i)
        break
    i += 1
