# Given a sequence of integers a, a triplet(a[i], a[j], a[k])is beautiful if:

# i < j < k
# a[j] – a[i] = a[k] – a[j] = d
# Given an increasing sequence of integers and the value of d, count the number of beautiful triplets in the sequence.

# Function Description
# Complete the beautifulTriplets function in the editor below. It must return an integer that represents the number of beautiful triplets in the sequence.
# beautifulTriplets has the following parameters:

# d: an integer
# arr: an array of integers, sorted ascending
# Input Format
# The first line contains 2 space-separated integers n and d, the length of the sequence and the beautiful difference.
# The second line contains n space-separated integers arr[i].

# Output Format
# Print a single line denoting the number of beautiful triplets in the sequence.
# Sample Input
# 7 3
# 1 2 4 5 7 8 10
# Sample Output
# 3

def beautifulTriplets(d, arr):
    gc = 0
    for i in range(n):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc += 1


nd = input().split()
n = int(nd[0])
d = int(nd[1])
arr = list(map(int, input().rstrip().split()))
result = beautifulTriplets(d, arr)
print(result)
