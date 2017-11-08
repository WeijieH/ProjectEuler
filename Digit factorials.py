'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

factorials = {'0': 1}
f = 1
for i in range(1, 10):
    f *= i
    factorials[str(i)] = f

result = set()
for i in range(10, 2540160):
    if sum([factorials[x] for x in str(i)]) == i:
        result.add(i)

print(result)
