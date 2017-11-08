'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def largest_palindrome_product(num1, num2):
    i = 0
    result = 0
    isFind = False
    while i < num1:
        for j in range(i // 2 + 1):
            p = (num1 - j) * (num2 - (i - j))
            if p == reverse_int(p):
                result = max(result, p)
                isFind = True
        if isFind:
            break
        i += 1
    return result


def reverse_int(n):
    return int(str(n)[::-1])


print(largest_palindrome_product(999, 999))
