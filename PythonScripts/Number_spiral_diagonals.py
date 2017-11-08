'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


def number_spiral_diagonals(d):
    result = 0
    for i in range(1, d + 1):
        result += sum_of_corners(i)
    print(result)


def sum_of_corners(n):
    if n & 1 == 0:
        return 0
    if n < 3:
        return 1
    return 4*n**2 - 6*(n - 1)



number_spiral_diagonals(1001)