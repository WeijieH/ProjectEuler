'''
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
'''


i = 1000

result = 0
for x in range(1, i+1):
    if x % 10 == 0:
        continue
    result += x**x

print(str(result)[-10:])