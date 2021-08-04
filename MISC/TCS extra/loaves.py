# Loaves Distribution
# You are the benevolent ruler of Rankhacker Castle, and today you’re distributing bread. Your subjects are in a line, and some of them already have some loaves. Times are hard and your castle’s food stocks are dwindling, so you must distribute as few loaves as possible according to the following rules:

# Every time you give a loaf of bread to some person I, you must also give a loaf of bread to the person immediately in front of or behind them in the line(i.e., persons i+1 or i-1).
# After all the bread is distributed, each person must have an even number of loaves.
# Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.
# Function Description
# Complete the fairRations function in the editor below. It should return an integer that represents the minimum number of loaves required.
# fairRations has the following parameter(s):
# B: an array of integers that represent the number of loaves each person’s starts with .
# Input Format
# The first line contains an integer n, the number of subjects in the bread line.
# The second line contains n space-separated integers b[i].
# Output Format
# Print a single integer that denotes the minimum number of loaves that must be distributed so that every person has an even number of loaves. If it’s not possible to do this, print NO.
# Sample Input
# 5
# 2 3 4 5 6
# Sample Output
# 4


def fairRations(B):
    c = 0
    m = 0
    for i in range(len(B)):
        c += B[i]
        if c % 2 == 1:
            m += 2
    if c % 2 != 0:
        return 'NO'
    else:
        return m


N = int(input())
B = list(map(int, input().rstrip().split()))
result = fairRations(B)
print(result)
