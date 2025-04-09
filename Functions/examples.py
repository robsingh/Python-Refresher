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
write a function to translate a text to morse code.
write another function to translate a string in morse code into a normal string.
'''
'''
latin2morse_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 
                    'E':'.', 'F':'..-.', 'G':'--.','H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 
                    'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 
                    'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 
                    'Y':'-.--', 'Z':'--..', '1':'.----', '2':'...--', 
                    '3':'...--', '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', '0':'-----', 
                    ',':'--..--', '.':'.-.-.-', '?':'..--..', ';':'-.-.-', 
                    ':':'---...', '/':'-..-.', '-':'-....-', '\'':'.----.', 
                    '(':'-.--.-', ')':'-.--.-', '[':'-.--.-', ']':'-.--.-', 
                    '{':'-.--.-', '}':'-.--.-', '_':'..--.-'}

morse2latin_dict = dict(zip(latin2morse_dict.values(), 
                            latin2morse_dict.keys()))

def txt2morse(txt, alphabet):
    morse_code = ""
    for char in txt.upper():
        if char == " ":
            morse_code += "  "
        else:
            morse_code += alphabet[char] + " "
    return morse_code


def morse2txt(txt, alphabet):
    result = ""
    mwords = txt.split("  ")
    for mword in mwords:
        for mchar in mword.split():
            result += alphabet[mchar]
        result += " "
    return result

txt = "What is this?"
mstring = txt2morse(txt, latin2morse_dict)
print(mstring)
print(morse2txt(mstring, morse2latin_dict))'''

'''
Write a function which calculates the position of the n-th occurence of a string 'sub' in another string 's'. 
If 'sub' doesn't occur in 's', -1 shall be returned.
'''
'''
def findnth(s, sub, n):
    num = 0
    start = -1
    while num < n:
        start = s.find(sub, start+1)
        if start == -1:
            return -1
        num += 1
    
    return start

s = "abc abc"
print(findnth(s, "abc", 3))'''

'''
Write a function fuzzy_time which expects a time string in the form hh: mm (e.g. "12:25", "04:56"). 
The function rounds up or down to a quarter of an hour.
'''
'''
def fuzzy_time(time):
    hour,minute = map(int, time.strip().split(':'))

    if minute < 8:
        minute = 0
    elif minute < 23:
        minute = 15
    elif minute < 38:
        minute = 30
    elif minute < 53:
        minute = 45
    else:
        #round up to next hour
        minute = 0
        hour = (hour + 1) % 24 #wrap around if hour is 23
    
    return f"{hour:02d}:{minute:02d}"


print(fuzzy_time("12:25"))'''