'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''

import numpy as np

# https://en.wikipedia.org/wiki/Most_common_words_in_English
commom_words = set(['the', 'be', 'to', 'of', 'a',
                    'and', 'in', 'that', 'have', 'I', 'it', 'for'])


def decryptText(text, password, common_words=None):
    l = len(password)
    score = 0
    for i in range(len(text)):
        d = text[i] ^ password[i % l]
        if d > 255 or d < 1:
            return 0, ''
        text[i] = d
    decryptedText = text.tostring().decode("ascii")
    words = decryptedText.split()
    if commom_words != None:
        for word in words:
            if word in commom_words:
                score += 1
    return score, decryptedText


with open('./Data/p059_cipher.txt') as f:
    text = f.readlines()[0]
    text = np.fromstring(text, dtype=np.int8, sep=',')


result = {}
for a in range(ord('a'), ord('z') + 1):
    for b in range(ord('a'), ord('z') + 1):
        for c in range(ord('a'), ord('z') + 1):
            password = [a, b, c]
            # must pass a copy of original array
            sc, _ = decryptText(text.copy(), password, commom_words)
            if sc > 0:
                result[chr(a) + chr(b) + chr(c)] = sc

key = max(result, key=result.get)
print('{0}:{1}'.format(key, result[key]))

_, de_text = decryptText(text, [ord(k) for k in key])
print(de_text)
print(sum([ord(i) for i in de_text]))
