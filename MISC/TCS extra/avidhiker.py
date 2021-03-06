# Pal is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike, he took exactly n steps. For every step he took, he noted if it was an uphill, U, or a downhill D, step. Pal’s hikes start and end at sea level and each step up or down represents a 1 unit change in altitude.

# We define the following terms:

# A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
# A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
# Given Pal’s sequence of up and down steps during his last hike, find and print the number of valleys he walked through.
# Function Description
# Complete the counting function in the editor below. It must return an integer that denotes the number of valleys pal traversed.
# counting has the following parameter(s):

# n: the number of steps pal takes
# s: a string describing his path
# Input Format
# The first line contains an integer n, the number of steps in Pal’s hike.
# The second line contains a single string s, of n characters that describe his path.
# Output Format
# Print a single integer that denotes the number of valleys pal walked through during his hike.
# Sample Input
# 8
# UDDDUDUU
# Sample Output
# 1


def countingValleys(n, s):
    height = 0
    prev_height = 0
    cnt = 0
    for i in range(len(s)):
        if (s[i] == 'U'):
            height += 1
        elif s[i] == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height
    return cnt


n = int(input())
s = input()
result = countingValleys(n, s)
print(result)
