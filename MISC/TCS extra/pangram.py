# Given a string check if it is Pangram or not. A pangram is a sentence containing every letter in the English Alphabet.

# Examples : The quick brown fox jumps over the lazy dog ” is a Pangram [Contains all the characters from ‘a’ to ‘z’]
# “The quick brown fox jumps over the dog” is not a Pangram [Doesn’t contains all the characters from ‘a’ to ‘z’, as ‘l’, ‘z’, ‘y’ are missing]

# We create a mark[] array of Boolean type. We iterate through all the characters of our string and whenever we see a character we mark it. Lowercase and Uppercase are considered the same. So ‘A’ and ‘a’ are marked in index 0 and similarly ‘Z’ and ‘z’ are marked in index 25.

# After iterating through all the characters we check whether all the characters are marked or not. If not then return false as this is not a pangram else return true.


import string


def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False

    return True


# Driver code
string = input("Enter the string: ")
if(ispangram(string) == True):
    print("Yes")
else:
    print("No")
