# Vira writes an apology letter to anu. However, before Anu can read it, Vira’s enemy Rohan takes it and rotates the characters of each word left to right N times. Find the number of words that remain the same even after this shifting of letters.

# Input Specification:

# input1: String of words
# input2: N, number of times rotation happens
# Output Specification:

# Your function should return the number of correct words.
# Example 1:

# input1: llohe ereth
# input2: 2

# Output: 2

# Example 2:

# input1: Sorry
# input2: 2

# Output: 0

string_inp = input()
rot = int(input())
ctr = 0

string_l = [c for c in string_inp]
# print(string_l)
rot_str = string_inp[rot:] + string_inp[0:rot]
# print(rot_str)
rot_l = [c for c in rot_str]
# print(rot_l)

for i in range(len(string_l)):
    if string_l[i] == rot_l[i]:
        ctr += 1
print(ctr)
