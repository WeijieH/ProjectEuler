'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

from math import factorial

permutation = ['0' ,'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9']


def lexicographic_permutations(permutation, position):
    result = ''
    position -= 1
    if position < 1 or position > factorial(len(permutation)):
        return result
    for _ in range(len(permutation) - 1):
        d = factorial(len(permutation) - 1)
        i = position // d
        adder = permutation[i]
        result += adder
        permutation.remove(adder)
        position = position % d
    result += permutation[0]
    print(result)


lexicographic_permutations(permutation, 1000000)