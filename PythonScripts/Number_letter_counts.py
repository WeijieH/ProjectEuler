'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
'''
words = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'ninety',
    100:'hundred'
}

def number_letter_counts(number):
    c = 0
    if number == 999:
        c = 11
    for i in range(1, number + 1):
        s = number_to_words(i).replace(' ', '')
        c += len(s)
    print(c)

def number_to_words(number):
    s = ''
    if number > 999:
        return s
    d = [0] * 3
    d[0] = number % 10
    number = number // 10
    d[1] = number % 10
    number = number // 10
    d[2] = number % 10
    check = 10 * d[1]  +d[0]

    if d[2] > 0:
        s += words[d[2]] + ' ' + words[100]
        if check > 0:
            s += ' and '
    if check > 20:
        s += words[10*d[1]] + ' ' + words[d[0]]
    else:
        s += words[check]
    return s

number_letter_counts(999)