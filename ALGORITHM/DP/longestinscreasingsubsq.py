# You have an array A of N integers A1 A2 .. An. Find the longest increasing subsequence Ai1 Ai2 .. Ak (1 <= k <= N) that satisfies the following condition:
# For every adjacent pair of numbers of the chosen subsequence Ai[x] and Ai[x+1] (1 < x < k), the expression( Ai[x] & Ai[x+1] ) * 2 < ( Ai[x] | Ai[x+1] ) is true
# Note: '&' is the bitwise AND operation, ' | ' is the bit-wise OR operation
# Input:
# The first line contains an integer, N, denoting the number of elements in A.
# Each line i of the N subsequent lines (where 0 ≤ i < N) contains an integer describing Ai.
# Sample cases:
# Input
# Output
# Output description 5 15 6 5 12 1
# 2
# One possible subsequence is:
# 5 12

def lis(arr):
    n = len(arr)

    # Declare the list (array) for LIS and
    # initialize LIS values for all indexes
    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        for j in range(0, i):
            if (arr[i] & arr[j])*2 < (lis[i] | lis[j]):
                lis[i] = lis[j]+1

    # Initialize maximum to 0 to get
    # the maximum of all LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum
# end of lis function


 #Driver Code

arr = [5, 15, 6, 5, 12, 1]
# arr = [7 ,17 ,16 ,12 ,2, 8 ,17, 17]
arr = sorted(list(set(arr)))
res = lis(arr)
print(res)