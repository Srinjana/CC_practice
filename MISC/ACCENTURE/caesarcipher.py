# Vaibhav protected his confidential information by encrypting it using a cipher. This Cipher shifts each letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet.
#  In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

# Original alphabet:      abcdef-ghijkl-mnopqr-stuvwx-yz

# Alphabet rotated + 3:    defghi-jklmno-pqrstu-vwxyza-bc

# Note: The cipher only encrypts letters
# symbols, such as -, remain unencrypted.This Cipher is also known as Caesar Cipher.


import string

symbols_low = string.ascii_lowercase
symbols_up = string.ascii_uppercase


def caesarCipher(s, k):

    res = []
    for c in s:
        if c.isupper():
            res.append(symbols_up[(symbols_up.index(c)+k) % len(symbols_up)])

        elif c.islower():
            res.append(symbols_low[(symbols_low.index(c)+k) % len(symbols_low)])

        else:
            res.append(c)

        return "".join(map(str, res))

  

k = int(input())
s = input()
result = caesarCipher(s, k)
print(result)
