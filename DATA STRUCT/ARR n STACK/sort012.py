# Given an array of size N containing only 0s, 1s, and 2s sort the array in ascending order.
#@author = Srinjana




class Solution:
    def sort012(self, arr, n):
        # code here
        lo = 0
        hi = len(arr) - 1
        mid = 0

        while mid <= hi:

            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo = lo + 1
                mid = mid + 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi -= 1
        return arr


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        ob.sort012(arr, n)
        for i in arr:
            print(i, end=' ')
        print()
