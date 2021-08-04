# In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

# Function Description
# It should return an integer that denotes the longest string that can be formed, or 0 if it cannot be done.
# alternate has the following parameter(s):

# s: a string
# Input Format
# The first line contains a single integer denoting the length of s.
# The second line contains string s.
# Output Format
# Print a single integer denoting the maximum length of t for the given s; if it is not possible to form string t, print 0 instead.
# Sample Input
# 10
# beabeefeab
# Sample Output
# 5

from itertools import combinations 


def alternate(s):
    x=set(s)
    m=0
    l=list(map(set,combinations(x,2)))
    for i in l:
        y=x-i
        z=s
        for j in y:
            z=z.replace(j,"")
        r=("".join(i))*(len(z)//2)
        if r+r[0]==z or r==z or r==z[::-1] or r[1]+r==z:
            m=max(m,len(z))
    return m


l = int(input().strip())
s = input()
result = alternate(s)
print(result)