# Superior Array Element
# In an array, a superior element is one that is greater than all elements to its right. the rightmost element will always be considered as a superior element.
# Here, the function accepts an integer array ‘arr’ and its length ‘n’. Implement the function to find and return the number of superior element in the array ‘arr’.
# Assumptions:
# 1. n > 0
# 2. Array index starts from 0.
# Example 1:
# Input 1: 7 9 5 2 8 7
# Output: 3

arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)-1):
    j = i+ 1
    arr_n = arr[j:]
    m = max(arr_n)
    if arr[i] > m:
        count += 1
print(count+1)