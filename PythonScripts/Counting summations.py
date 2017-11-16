'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

# take code from coin_sums.py
import numpy as np

coins = [i for i in range(1, 100)]

target = 100

solution = np.zeros((target, len(coins)), dtype=np.int)
solution[:, 0] = 1
for y in range(target):
    for x in range(0, len(coins)):
        coin = y + 1
        if coin < coins[x]:
            solution[y, x] = solution[y, x - 1]
        elif coin > coins[x]:
            solution[y, x] = solution[y, x - 1] + solution[y - coins[x], x]
        else:
            solution[y, x] = solution[y, x - 1] + 1
print(solution[-1, -1])
