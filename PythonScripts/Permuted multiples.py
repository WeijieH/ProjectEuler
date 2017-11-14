'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''


def check_multiples(n):
    n6 = sorted(str(n * 6))
    if len(n6) != len(str(n)):
        return False

    n2 = sorted(str(n * 2))
    n3 = sorted(str(n * 3))
    n4 = sorted(str(n * 4))
    n5 = sorted(str(n * 5))
    n = sorted(str(n))
    return n == n2 and n == n3 and n == n4 and n == n5 and n == n6


i = 0
while True:
    i += 1
    if check_multiples(i):
        print(i)
        break
