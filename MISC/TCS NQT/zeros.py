# Given a pair of positive integers m and n(m < n
#0 < m < 999
# 1 < n <= 999), write a program to smartly affix zeroes, while printing the numbers from m to n.

# Example-1
# Input
# 5 10
# Expected output
# 05 06 07 08 09 10

low, up = map(str, input().split())
low , up = int(low), int(up)
for i in range(low, up+1):
    if(up >= 100):
        print("{:03d}".format(i), end=" ")
    elif(up >= 10):
        print("{:02d}".format(i), end=" ")
    else:
        print(i, end=" ")
