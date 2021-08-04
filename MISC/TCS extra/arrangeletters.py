# Lexicographic order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list. Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

# It must be greater than the original word
# It must be the smallest word that meets the first condition
# Function Description
# It should return the smallest lexicographically higher string possible from the given string or no answer.
# biggerIsGreater has the following parameter(s):

# w: a string
# Input Format
# The first line of input contains T, the number of test cases.
# Each of the next T lines contains w.
# Output Format
# For each test case, output the string meeting the criteria. If no answer exists, print no answer.
# Sample Input
# 5
# ab
# bb
# hefg
# dhck
# dkhc
# Sample Output
# ba
# no answer
# hegf
# dhkc
# hcdk

t = int(input())
for _ in range(t):
    s = input()
    s = list(s[::-1])
    done = 0
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            for j in range(i):
                if s[j] > s[i]:
                    s[j],s[i] = s[i],s[j]
                    s = sorted(s[:i])[::-1] + s[i:]
                    print("".join(s[::-1]))
                    break
            break
    else:
        print("no answer")
