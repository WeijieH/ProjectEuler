'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

import numpy as np

triangle_numbers = set([n * (n + 1) // 2 for n in range(1, 50)])
x = 1
letters = {}
for c in range(ord('A'), ord('Z') + 1):
    letters[chr(c)] = x
    x += 1


def word_value(w):
    return sum([letters[c] for c in w])


with open('.\Data\p042_words.txt') as f:
    words = f.readlines()[0].replace('\"', '')
    words = np.array(words.split(','))
    result = 0
    for word in words:
        if word_value(word) in triangle_numbers:
            result += 1
    print(result)
