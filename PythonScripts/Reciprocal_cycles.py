'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''

def get_length_of_recurring_cycle(n, result_dict):
    reduced_n = remove_2_and_5(n)
    if reduced_n in result_dict:
        result_dict[n] = result_dict[reduced_n]
    else:
        m = 10 % reduced_n
        c = m
        k = 1
        while True:
            if c == 1:
                result_dict[n] = k
                break
            c = (c * m) % reduced_n
            k += 1
    return result_dict

def remove_2_and_5(n):
    while n & 1 == 0:
        n = n >> 1
    while n % 5 == 0:
        n = n // 5
    return n


result = {1:0}
for i in range(2, 1000):
    get_length_of_recurring_cycle(i, result)
#print(result)
m = max(result, key=result.get)
print('{0} : {1}'.format(m, result[m]))
