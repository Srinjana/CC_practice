# You are given an array and you need to find the number of triplets of indices(i, j, k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.

# Function Description
# It should return the number of triplets forming a geometric progression for a given r as an integer.
# countTriplets has the following parameter(s):

# arr: an array of integers
# r: an integer, the common ratio
# Input Format
# The first line contains two space-separated integers n and r, the size of arr and the common ratio.
# The next line contains n space-separated integers arr[i].
# Output Format
# Return the count of triplets that form a geometric progression.
# Sample Input
# 4 2
# 1 2 2 4
# Sample Output
# 2


def countTriplets(arr, r):
    count = 0
    dict = {}
    dictPairs = {}

    for i in reversed(arr):

        if i*r in dictPairs:
            count += dictPairs[i*r]

        if i*r in dict:
            dictPairs[i] = dictPairs.get(i, 0) + dict[i*r]
        dict[i] = dict.get(i, 0) + 1
        
    return count


nr = input().rstrip().split()
n = int(nr[0])
r = int(nr[1])
arr = list(map(int, input().rstrip().split()))
ans = countTriplets(arr, r)
print(ans)
