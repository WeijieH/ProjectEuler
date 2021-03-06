'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''


def has_0_or_repeat_digits(n):
    n = str(n)
    return len(set(n)) < len(n) or '0' in n


def concatenated_product(n):
    s = str(n)
    m = 2
    while True:
        p = m * n
        s = s + str(p)
        l = len(s)
        if l > 9:
            return None
        elif l == 9:
            return int(s)
        m += 1


result = {}
for i in range(1, 9876 + 1):
    if has_0_or_repeat_digits(i):
        continue
    p = concatenated_product(i)
    if p is not None:
        if not has_0_or_repeat_digits(p):
            result[i] = p

key = max(result, key=result.get)
print('{0}:{1}'.format(key, result[key]))
