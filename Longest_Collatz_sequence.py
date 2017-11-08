'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''


def longest_Collatz_sequence(upper_limit, table):
    for i in range(2, upper_limit):
        if i in table:
            continue
        ss = collatz_sequence(i, table)
        t = table[ss[0]] + 1
        for s in ss[1:]:
            table[s] = t
            t += 1
    result = max(table, key=table.get)
    print(result)


def collatz_sequence(number, table):
    n = number
    s = [n]
    while n not in table:
        if n % 2 == 0:
            n = n // 2
            s.append(n)
        else:
            n = 3 * n + 1
            s.append(n)
    return s[::-1]


collatz_grid = {1 : 1}
longest_Collatz_sequence(1000000, collatz_grid)
