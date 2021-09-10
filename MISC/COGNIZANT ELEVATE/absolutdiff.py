# Maxwell filled his university exam form in which he has filled his mid sem marks but by mistake he has filled DS marks in AI field and AI marks in DS field. He wants to update his mid sem marks but for that he has to pay some penalty.

# Penalty equal to the sum of absolute differences between adjacent subject marks.

# Return the minimum penalty that must be paid by him.

# Input Specification:

# input1: length of an integer array of numbers(2 <= input 1 <= 1000)
# input2: integer array(1 <= input2[i] <= 10000)
# Example 1:

# Input: arr = {4, 1, 5}

# Output: 5

# Explanation: Sum of absolute differences is | 4-5 | + | 1-4 | + | 5-4|

# Example 2:

# Input: arr = {5, 10, 1, 4, 8, 7}

# Output: 9

# Example 3:

# Input: {12, 10, 15, 22, 21, 20, 1, 8, 9}

# Output: 18


n = int(input())

arr = sorted(list(map(int, input().split())))

s = abs(arr[0]-arr[1])+abs(arr[-1]-arr[-2])

for i in range(1, n-1):

    s += min(abs(arr[i]-arr[i-1]), abs(arr[i]-arr[i+1]))

print(s)
