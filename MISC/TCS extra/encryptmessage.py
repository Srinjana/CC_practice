# An English text needs to be encrypted using the following encryption scheme. First, the spaces are removed from the text. Let L be the length of this text. Then, characters are written into a grid, whose rows and columns have the following constraints:
# [lowerbond(root(L))] <= row <= column <= [upperbond(root(L))]

# For example S = happyprogrammersday
# Here the letter count is 19 whose root is between 4 and 5, so the upper bond is 5 and lowe bond is 4.
# Function Description
# It should return a single string composed as described.
# encryption has the following parameter(s):

# s: a string to encrypt
# Input Format
# One line of text, the string s
# Output Format
# Print the encoded message on one line as described.
# Sample Input
# haveaniceday
# Sample Output
# hae and via ecy

import math

s = input("Enter the string: ")
s = s.replace(" ","")
length = len(s)

r = math.floor(math.sqrt(length))
c = math.ceil(math.sqrt(length))

for i in range(c):
    print(s[i::c],end=" ")
