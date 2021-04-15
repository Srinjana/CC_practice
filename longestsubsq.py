# Consider a non-empty string instrcontaining only lower-case alphabets. Print the Output based on the below Logic.
# 1. Identify and print the longest sub-sequence of at least 3 alphabets between vowels and consonants possible from instr. The sub-sequence can start with a vowel or a consonant
#      -A sub-sequence of a string str is the possible set of characters from str starting from left to right.
# 2.  If more than one such longest sub-sequences are identified print the one having the highest sum of ASCII Values of its Alphabets.
# 3. If no such sub-sequence of at least 3 alphabets is possible, print X(upper case)
# .Assumption: -There will be only one longest sub-sequence having the highest sum of ASCII Values of its alphabets.

string_ip = input()

consonents = 0
vowels = 0

v = ['a', 'e', 'i', 'o', 'u']

if (string_ip[0] in v):
    vowels = 1
else:
    consonents = 1

arr = []
i = 0
length = len(string_ip)

newstr = ''

while True:
    if (i == length):
        newstr += max(arr)
        break
    if(vowels):
        if(string_ip[i] in v):
            arr.append(string_ip[i])
            i += 1
        else:
            newstr += max(arr)
            consonents = 1
            vowels = 1
            arr = []
    else:
        if(string_ip[i] not in v):
            arr.append(string_ip[i])
            i += 1
        else:
            newstr += max(arr)
            consonents = 0
            vowels = 1
            arr = []
    if (len(newstr) < 3):
        print("X")
    else:
        print(newstr)
    