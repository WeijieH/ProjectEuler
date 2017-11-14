'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from primesieve import primes


def find_next_permutation(number):
    '''
    https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
    '''
    number = [i for i in str(number)]
    l = len(number)
    low = l - 1
    while low > 0:
        if number[low] > number[low - 1]:
            for high in reversed(range(low, l)):
                if number[high] > number[low - 1]:
                    number[high], number[low -
                                         1] = number[low - 1], number[high]
                    number[low:] = number[low:][::-1]
                    return int(''.join(number))
        low -= 1
    return 0


prime_numbers = primes(1000, 9999)
visited = set()
selected_primes = {}

for p in prime_numbers:
    if p in visited:
        continue
    c = [p]
    visited.add(p)
    n = p
    while True:
        n = find_next_permutation(n)
        if n < 1000:
            break
        if n in prime_numbers:
            c.append(n)
            visited.add(n)
    if len(c) > 2:
        selected_primes[p] = c

for p in selected_primes:
    plist = selected_primes[p]
    for i in range(len(plist)):
        for j in range(i + 1, len(plist)):
            s = 2 * plist[j] - plist[i]
            if s > plist[-1]:
                break
            elif s in plist:
                print('{0} -> {1} -> {2}'.format(plist[i], plist[j], s))
                break
