'''
write a function which takes a text and encrypts it with a Caesar cipher.
Note : coded = True, shifts the character n positions forward in the blanket.
       coded = False, shifts the character n positions backward in the blanket.
'''
import string
from random import sample
'''
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
'''
#without the calculations
'''
shift = 3
abc = string.ascii_uppercase
abc_cipher = abc[-shift:] + abc[:-shift]
print(abc_cipher)

def caesar(txt, shift):
    new_text = ""
    for char in txt.upper():
        position = abc.find(char)
        new_text += abc_cipher[position]
    return new_text

shift = 3
txt = "Hello, how are?"
print(caesar(txt, shift))'''

'''
Write a function which takes a text and a dictionary to decrypt or encrypt the given text with a permutated alphabet.
'''
'''
alphabet = string.ascii_letters
permutated_alphabet = sample(alphabet, len(alphabet))

encrypt_dict = dict(zip(alphabet, permutated_alphabet))
decrypt_dict = dict(zip(permutated_alphabet, alphabet))

def encrypt(txt, edict):
    result = ""
    for char in txt:
        result += edict.get(char, char)
    return result


txt = """More use of LLM is harmful to the environment.
People do not understand the computing power being used to generate output for a simple query.
It is just so sad!!
"""

print(encrypt(txt, decrypt_dict))'''

'''


'''