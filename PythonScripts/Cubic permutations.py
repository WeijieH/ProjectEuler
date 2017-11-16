'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''


def isPermutation(number1, number2):
    s1 = str(number1)
    s2 = str(number2)
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


i = 406
cubes = []
result = {}
found = False
while not found:
    c = i ** 3
    result[c] = 1
    cubes.append(c)
    for cube in cubes:
        if cube == c:
            continue
        if isPermutation(c, cube):
            result[cube] += 1
            if result[cube] == 5:
                print('Stopped at: {0}'.format(i))
                print('{0}:{1}'.format(cubes.index(cube) + 406, cube))
                found = True
            break
    i += 1
