# Aashay loves to go to WONDERLA, an amusement park. They are offering students who can code well with some discount. Our task is to reduce the cost of the ticket as low as possible.

# They will give some k turns to remove the cost of one ticket where the cost of tickets are combined and given as string.Help Aashay in coding as he is not good in programming and get a 50 % discount for your ticket.

# Constraints:

# 1 <= number of tickets <= 10 ^ 5
# 1 <= K <= number of tickets
# Input Format for Custom Testing:

# The first line contains a string, Tickets, denoting the given cost of each ticket.
# The next line contains an integer, K, denoting the number of tickets that is to be removed

import sys

n = input()
k = int(input())
n1 = len(n)

if len(n)<= k:
    print(0)
    sys.exit()

a = ''
i = 0

while i<(n1-1) and k>0:
    if (int(n[i]) > int(n[i+1])):
        i += 1
        k -= 1
        continue
    else:
        a += n[i]
        i += 1

a += n[i]
i += 1
if k>0:
    a = a[:-k]

if i<=(n1-1):
    while i<n1:
        a += n[i]
        i += 1

print(int(a)%((10**9)+7))