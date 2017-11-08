'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''

def digit_fifth_powers(p):
    power = {}
    result = []
    for i in range(0, 11):
        power[str(i)] = i**p
    for i in range(10, p * 9**p):
        if sum([power[x] for x in str(i)]) == i:
            result.append(i)
    print(result)
    print(sum(result))



digit_fifth_powers(5)
