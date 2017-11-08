'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

import numpy as np

def lattice_paths(width, height):
    grid = np.zeros((width + 1, height + 1), dtype = np.int64)
    grid[-1,-1] = 1
    for x in reversed(range(0, width + 1)):
        for y in reversed(range(0, height + 1)):
            if grid[x, y] != 0:
                continue

            if y == height:
                down = 0
            else:
                down = grid[x, y + 1]

            if x == width:
                right = 0
            else:
                right = grid[x + 1, y]

            grid[x, y] = down + right
    return grid[0, 0]

print(lattice_paths(20,20))