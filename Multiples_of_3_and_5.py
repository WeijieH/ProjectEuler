'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def multiples_of_3_and_5(upper_limit):
    if (upper_limit < 3):
        return 0
    result = 0
    m3 = 3
    m5 = 5
    while True:
        if (m5 > m3):
            adder = m3
            m3 += 3
        elif (m5 < m3):
            adder = m5
            m5 += 5
        else:
            adder = m3
            m3 += 3
            m5 += 5

        if (adder >= upper_limit):
            break
        
        result += adder
    return result

print(multiples_of_3_and_5(1000))