'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''


def is_bin_Palindrome(n):
    b = str(bin(n))[2:]
    return b == b[::-1]


double_base_palindromes = set()


for i in range(1, 10):
    if is_bin_Palindrome(i):
        double_base_palindromes.add(i)


for i in range(1, 1000):
    # for abccba
    n_even = int(str(i) + str(i)[::-1])
    if is_bin_Palindrome(n_even):
        double_base_palindromes.add(n_even)
    if i < 100:
        for j in range(0, 10):
            # for abcxcba          
            n_odd = int(str(i) + str(j) + str(i)[::-1])
            if is_bin_Palindrome(n_odd):
                double_base_palindromes.add(n_odd)


print('Length:Sum = {0}:{1}'.format(
    len(double_base_palindromes), sum(double_base_palindromes)))
