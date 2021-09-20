# Problem statement
# Mr. Professor is a great scientist, but he is not able to find a solution to one problem. There are N straight
# lines that are not parallel, and no three lines go through the same point. The lines divide the plane into M
# regions. Write a function to find out the maximum number of such regions he can get on the plane.
# Input Specification:
# input1: An integer N representing the number of straight lines(0 <= N <= 100)
# Output Specification:
# Page 44 | 45
# Return the maximum number of regions
# Example:
# Input Output Explanation
# 2 4
# Given the above scenario, 2 lines
# divide the plane into 4 regions.
# Therefore, 4 is returned as the
# output.
# 3 7
# Given the above scenario, 3 lines
# divide the plane into 7 regions.
# Therefore, 7 is returned as the
# output.

class Solution:
    def maxRegions(self, n):
        num = n * (n + 1) // 2 + 1
        return num


if __name__ == '__main__':
    n = int(input())
    ob = Solution()
    ans = ob.maxRegions(n)
    print(ans)
