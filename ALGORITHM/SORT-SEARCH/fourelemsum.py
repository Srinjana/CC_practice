# Given an array of integers and another number. Find all the unique quadruple from the given array that sums up to the given number.
# Input:
# N = 7, K = 23
# A[] = {10, 2, 3, 4, 5, 7, 8}
# Output: 2 3 8 10 $2 4 7 10 $3 5 7 8 $
# Explanation: Sum of 2, 3, 8, 10 = 23,
# sum of 2, 4, 7, 10 = 23 and sum of 3,
# 5, 7, 8 = 23.

import itertools
from itertools import combinations, chain

# arr[] : int input array of integers
# k : the quadruple sum required


class Solution:
    def fourSum(self, arr, k):
        arr.sort()
        subsets = list(map(set, itertools.combinations(arr, 4)))
        #print(subsets)
        result = []
        for item in subsets:
            if sum(item) == k:
                result.append(item)
        for element in result:
            print (*element)

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        i = int(input())
        a.append(i)

    ob = Solution()
    ob.fourSum(a,k)

