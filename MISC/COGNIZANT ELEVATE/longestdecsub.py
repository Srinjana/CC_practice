# Naman on his way home found ‘N’ tokens on the ground arranged in a line horizontally. Each token has some number written on it.
# Naman wants to count the longest sub-sequence of the tokens with a decreasing arrangement.
# A sub-sequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements keeping the relative positions of elements same as it was in the initial sequence. A decreasing sub-sequence is a sub-sequence in which every element is strictly less than the previous number.

# Your task is to help Naman in finding the longest subsequence of decreasing arrangement of tokens.

# Input Specification:

# input1: integer ‘n’ denoting size of array
# input2: integer array ‘A’ containing ‘n’ elements
# Output Specification:
# For each test case, print the integer denoting the length of the longest decreasing subsequence.
# Print the output of each test case in a separate line.

# Constraints:

# 1 <= n <= 5000
# 1 <= A[i] <= 10 ^ 9
# Time Limit: 1 sec
# Example1:
# Input1: 5
# Input2: {5, 0, 3, 2, 9}

# Output: 3
# Explanation: The longest decreasing subsequence is of length 3, i.e. [5, 3, 2]

# Example2:

# input1: 9
# input2: {15, 27, 14, 38, 63, 55, 46, 65, 85}

# Output: 3
# Explanation: The longest decreasing subsequence is of length 3, i.e. [63, 55, 46]


n = int(input())

arr = list(map(int, input().split()))

tokens = [1]*n

for i in range(1, n):

    for j in range(i):

        if (arr[i] < arr[j] and tokens[i] < tokens[j] + 1):

            tokens[i] = tokens[j] + 1

print(max(tokens))
