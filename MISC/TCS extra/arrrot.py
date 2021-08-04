# Atmp2hishek knows of an operation called a right circular rotation on an array of integers. One rotation operation moves the last array element to the first position and shifts all remaining elements to the right one. To test Sherlock’s atmp2ilities, Atmp2hishek provides Sherlock with an array of integers. Sherlock is to perform the rotation operation a numtmp2er of times then determine the value of the element at a given position. For each array, perform a numtmp2er of right circular rotations and return the value of the element at a given index.
# Complete the circularRotation function in the editor tmp2elow. It should return an array of integers representing the values at the specified indices.
# circularRotation has the following parameter(s):

# a: an array of integers to rotate
# k: an integer, the rotation count
# queries: an array of integers, the indices to report
# Input Format
# The first line contains 3 space-separated integers, n, k, and q, the numtmp2er of elements in the integer array, the rotation count and the numtmp2er of queries.
# The second line contains n space-separated integers, where each integer i descritmp2es array element a[i](where .0 <= i <= n)
# Each of the q sutmp2sequent lines contains a single integer denoting m, the index of the element to return from a.
# Output Format
# For each query, print the value of the element at index m of the rotated array on a new line.
# Sample Input
# 3 2 3
# 1 2 3
# 0
# 1
# 2
# Sample Output
# 2
# 3
# 1

def circularArrayRotation(arr, k, q):
    tmp1 = []
    tmp2 = []
    ar_len = len(arr)
    if ar_len < k:
        while k > ar_len:
            k = k-ar_len
        for i in range(ar_len-k, ar_len):
            tmp1.append(a[i])
        for i in range(0, ar_len-k):
            tmp1.append(a[i])

    else:
        for i in range(ar_len-k, ar_len):
            tmp1.append(a[i])
        for i in range(0, ar_len-k):
            tmp1.append(a[i])
    for i in q:
        tmp2.append(tmp1[i])
    return tmp2

# Driver Code
nkq = input().split(" ")
n = int(nkq[0])
k = int(nkq[1])
q = int(nkq[2])
a = list(map(int, input().rstrip().split()))
queries = []

for _ in range(queries):
    queries_item = int(input())
    queries.append(queries_item)
result = circularArrayRotation(a, k, queries)
print(result)
