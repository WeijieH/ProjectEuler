'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''


def nextinChain(n):
    result = 0
    while n > 0:
        t = n % 10
        result += t * t
        n //= 10
    return result


end_with_1 = {1}
end_with_89 = {89}


limit = 10000000
for i in range(2, limit):
    if i in end_with_1 or i in end_with_89:
        continue
    visited = {i}
    n = nextinChain(i)
    while True:
        visited.add(n)
        if n in end_with_1:
            end_with_1.update(visited)
            break
        if n in end_with_89:
            end_with_89.update(visited)
            break
        n = nextinChain(n)

print(len(end_with_89))
