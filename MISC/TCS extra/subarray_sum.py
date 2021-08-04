# Array Addition
# We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.
# Given an array, find the maximum possible sum among:

# all nonempty subarrays.
# all nonempty subsequences.
# Print the two values as space-separated integers on one line.

# Note: empty subarrays/subsequences should not be considered.
# Function Description
# It should return an array of two integers: the maximum subarray sum and the maximum subsequence sum of arr.
# maxSubarray has the following parameter(s):

# arr: an array of integers
# Input Format
# The first line of input contains a single integer t, the number of test cases.
# The first line of each test case contains a single integer n
# The second line contains space-separated integers arr[i] where 0<=i<n.
# Output Format
# Print two space-separated integers denoting the maximum sums of nonempty subarrays and nonempty subsequences, respectively.
# Sample Input
# 2
# 4
# 1 2 3 4
# 6
# 1 -1 -1 -1 -1 5
# Sample Output
# 10 10
# 5 6

for _ in range(int(input())):

    _, arr = input(), [int(n) for n in input().split()]
    h = m = t = arr[0]
    ar = []

    for ind, n in enumerate(arr):
        if ind == 0: 
            continue
        
        t = max(t, n, t + n)
        h = max(n, h + n)
        m = max(m, h)

    print(m,t)