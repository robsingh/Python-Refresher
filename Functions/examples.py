'''
write a function which takes a text and encrypts it with a Caesar cipher.
Note : coded = True, shifts the character n positions forward in the blanket.
       coded = False, shifts the character n positions backward in the blanket.
'''
import string
abc = string.ascii_uppercase + " .,-?!"
def caesar(text, n, coded=False):
    result = ""
    for char in text.upper():
        if char not in abc:
            result += char
        elif coded:
            result += abc[(abc.find(char) + n) % len(abc)]
        else:
            result += abc[(abc.find(char) - n) % len(abc)]
    return result

n = 3
x = caesar("Hello, here I am!", n)
print(x)
print(caesar(x, n, True))