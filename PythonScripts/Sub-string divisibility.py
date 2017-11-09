'''
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
'''


def find_next_permutation(number):
    '''
    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    '''
    l = len(number)
    low = l - 1
    while low > 0:
        if number[low] > number[low - 1]:
            for high in reversed(range(low, l)):
                if number[high] > number[low - 1]:
                    number[high], number[low - 1] = number[low - 1], number[high]
                    number[low:] = number[low:][::-1]
                    return number
        low -= 1
    return None


pandigital_number = 1023456789
pandigital_number = [int(d) for d in str(pandigital_number)]
result = []

while True:
    pandigital_number = find_next_permutation(pandigital_number)
    if pandigital_number == None:
        break
    if pandigital_number[3] % 2 != 0:
        continue
    if pandigital_number[5] != 0 and pandigital_number[5] != 5:
        continue
    if (pandigital_number[2] + pandigital_number[3] + pandigital_number[4]) % 3 != 0:
        continue
    if (100 * pandigital_number[4] + 10 * pandigital_number[5] + pandigital_number[6]) % 7 != 0:
        continue
    if (100 * pandigital_number[5] + 10 * pandigital_number[6] + pandigital_number[7]) % 11 != 0:
        continue
    if (100 * pandigital_number[6] + 10 * pandigital_number[7] + pandigital_number[8]) % 13 != 0:
        continue
    if (100 * pandigital_number[7] + 10 * pandigital_number[8] + pandigital_number[9]) % 17 != 0:
        continue
    result.append(int(''.join(map(str, pandigital_number))))

print(result)
print(sum(result))
