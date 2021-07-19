# #Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

# Example

# The grid is illustrated below.

# a b c
# a d e
# e f g
# The rows are already in alphabetical order. The columns a a e, b d f and c e g are also in alphabetical order, so the answer would be YES. Only elements within the same row can be rearranged. They cannot be moved to a different row.

# Function Description

# Complete the gridChallenge function in the editor below.

# gridChallenge has the following parameter(s):

# string grid[n]: an array of strings
# Returns

# string: either YES or NO
# Input Format

# The first line contains, the number of testcases.

# Each of the next  sets of lines are described as follows:
# - The first line contains, the number of rows and columns in the grid.
# - The next  lines contains a string of length

# Constraints


# Each string consists of lowercase letters in the range ascii[a-z]

# Output Format
# For each test case, on a separate line print YES if it is possible to rearrange the grid alphabetically ascending in both its rows and columns, or NO otherwise.

import sys

def gridChallenge(grid):
    for i in range(n):
        grid[i] = sorted(grid[i])
    for i in range(n-1):
        for j in range(n):
            if (grid[i][j] > grid[i+1][j]):
                return "NO"
    return "YES"        
        

if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        grid = []

        for grid_i in range(n):
            grid_t = str(input().strip())
            grid.append(grid_t)
        print (gridChallenge(grid))
