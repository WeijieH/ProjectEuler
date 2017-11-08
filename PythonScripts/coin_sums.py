'''
In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

import numpy as np

coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

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
