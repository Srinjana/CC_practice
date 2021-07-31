#  In this 3 Palindrome, Given an input string word, split the string into exactly 3 palindromic substrings. Working from left to right, choose the smallest split for the first substring that still allows the remaining word to be split into 2 palindromes.

# Similarly, choose the smallest second palindromic substring that leaves a third palindromic substring.

# If there is no way to split the word into exactly three palindromic substrings, print “Impossible” (without quotes). Every character of the string needs to be consumed.

# Cases not allowed –

# After finding 3 palindromes using above instructions, if any character of the original string remains unconsumed.
# No character may be shared in forming 3 palindromes.
# Constraints

# 1 <= the length of input sting <= 1000
# Input

# First line contains the input string consisting of characters between [a-z].
# Output

# Print 3 substrings one on each line.
# Time Limit

# 1

# Examples

# Example 1

# Input

# nayannamantenet

# Output

# nayan

# naman

# tenet

# Explanation

# The original string can be split into 3 palindromes as mentioned in the output.
# However, if the input was nayanamantenet, then the answer would be “Impossible”.

import sys


def if_palindrome(s):

    if len(s) == 1:
        return True
        
    s1 = s[::-1]
    return s1 == s


s = input("Enter the string: ")
l = len(s)

for i in range(1, l-1):
    s1 = s[:i]

    if if_palindrome(s1):
        for j in range(1, l-i):
            s2 = s[i:i+j]
            s3 = s[i+j:]

            if if_palindrome(s2) and if_palindrome(s3):
                print(s1)
                print(s2)
                print(s3)

                sys.exit()

print("Impossible")
