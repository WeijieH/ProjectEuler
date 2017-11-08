'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''


with open('.\Data\large_sum_data.txt') as f:
    numbers = f.readlines()
    result = 0
    for number in numbers:
        result += int(number) 
    print(str(result)[:10])