# Given an array of positive integers. Find the maximum length of Bitonic subsequence.
# A subsequence of array is called Bitonic if it is first increasing, then decreasing.


# Example 1:

# Input: nums = [1, 2, 5, 3, 2]
# Output: 5
# Explanation: The sequence {1, 2, 5} is
# increasing and the sequence {3, 2} is
# decreasing so merging both we will get
# length 5.

def bitonic(arr):
    n = len(arr)
    lis = [1]*(n+1)

    # left to right checking (longest increasing subsequence)
    for i in range(1, n):
        for j in range(0, i):
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] + 1)):
                lis[i] = lis[j] + 1

    lds = [1]*(n+1)

    #  right to left checking (longest decreasing subsequence)
    for i in reversed(range(n-1)):  
        for j in reversed(range(i-1, n)):  
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1):
                lds[i] = lds[j] + 1

    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n):
        maximum = max((lis[i] + lds[i]-1), maximum)
     
    return maximum

input_arr = list(map(int, input().split()))
res = bitonic(input_arr)
print (res)
