# You will be given an array of integers and a target value. Determine the number of pairs of array elements that have a difference equal to a target value.

# For example, given an array of[1, 2, 3, 4] and a target value of 1, we have three values meeting the condition: 2-1 = 1, 3-2 = 1, and 4-3 = 1.

# Function Description
# Write a function pairs. It must return an integer representing the number of element pairs having the required difference.
# pairs has the following parameter(s):

# k: an integer, the target difference
# arr: an array of integers

# Input Format
# The first line contains two space-separated integers n and k, the size of arr and the target value.
# The second line contains n space-separated integers of the array arr

# Sample Input
# 5 2
# 1 5 3 4 2

# Sample Output
# 2

def pairs(k, arr):
    q = 0
    n = len(arr)
    arr = set(arr)
    h = len(arr) - n
    for i in arr:
        if (i + k) in arr:
            q += 1
    return q + h


n, k = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
result = pairs(k, arr)
print(result)
