# Problem statement

# You are required to implement the following function: int MatchString(char stri[], int len1, char str2[], int len2, int k1, int k2)

# The function accepts two strings 'stri' and 'str2' of length 'len1' and 'len2' respectively and two integers 'k1' and 'k2' as its arguments. Implement the function to compare each index of 'str1' and 'str2' leaving out the first 'k1' characters from 'str1' and 'k2' characters from 'str2' respectively till the end of each string and return an integer as per the following rules in the given priority:

# 1. If all the remaining characters match, then return the length of the match

# 2. Return 0, if remaining characters to be matched for either of the string is 0 or both the strings are null ( or None in case of python)

# 3. Return - 1, in case of mismatch in characters or count of remaining characters or one of the string, is null (or None in case of python)

# Assumption:

# 'str1' and 'str2' contain lower case alphabets only

# . Index starts from 0

# 0 <= k1 <= len1

l1= int(input())
str1 = input()
l2 = int(input())
str2 = input()
k1 = int(input())
k2 = int(input())

slice1 = str1[k1:l1+1]
print(slice1)
slice2 = str2[k2:l2+1]
print(slice2)

if (slice1 == slice2):
    print(len(slice1))
elif(slice1 == None or slice2 == None or len(slice1) == 0 or len(slice2) == 0): 
    print("0")
else:
    print("-1")