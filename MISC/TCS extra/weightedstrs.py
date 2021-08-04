# A weighted string is a string of lowercase English letters where each letter has a weight. Character weights are 1 to 26 from a to z given a string s, let U be the set of weights for all possible uniform contiguous substrings of string s. You have to answer n queries, where each query I consists of a single integer, x[i]. For each query, print Yes on a new line if x[i] is set of U; otherwise, print No instead.

# We define the following terms:

# The weight of a string is the sum of the weights of all the string’s characters. For example:
# A uniform string consists of a single character repeated zero or more times. For example, ccc and a are uniform strings, but bcb and cd are not.
# Function Description
# Complete the weightedUniformStrings function in the editor below. It should return an array of strings, either Yes or No, one for each query.
# weightedUniformStrings has the following parameter(s):

# s: a string
# queries: an array of integers
# Input Format
# The first line contains a string s, the original string.
# The second line contains an integer n, the number of queries.
# Each of the next n lines contains an integer x[i], the weight of a uniform substring of s that may or may not exist.
# Output Format
# Print n lines. For each query, print Yes on a new line if x[i] is set of U Otherwise, print No.
# Sample Input
# abccddde
# 6
# 1
# 3
# 12
# 5
# 9
# 10
# Sample Output
# Yes
# Yes
# Yes
# Yes
# No
# No


import sys

s = input().strip()
n = int(input().strip())
seq=[]
for num in range(1,27):
    seq.append(0)
    
for x in sorted(set(s)):
    i = 1
    while x * i in s:
        i += 1
    seq[ord(x)-97]=i-1 
finale=set()                 
for index,every in enumerate(seq):
    for sval in range(every):
        finale.add((index+1)*(sval+1))     
for a0 in range(n):
    x = int(input().strip())
    print("Yes" if x in finale else "No")