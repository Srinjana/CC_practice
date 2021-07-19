# Given a matrix of n*n size, the task is to print its elements in a diagonal pattern.

# Input: mat[3][3] = {{1, 2, 3},
#                     {4, 5, 6},
#                     {7, 8, 9}}
# Output: 1 2 4 7 5 3 6 8 9.
# Explanation: Start from 1
# Then from upward to downward diagonally i.e. 2 and 4
# Then from downward to upward diagonally i.e 7, 5, 3
# Then from up to down diagonally i.e  6, 8
# Then down to up i.e. end at 9.

# Create variables i = 0, j = 0 to store the current indices of row and column
# Run a loop from 0 to n*n, where n is side of the matrix.
# Use a flag isUp to decide whether the direction is upwards or downwards. Set isUp = true initially the direction is going upward.
# If isUp = 1 then start printing elements by incrementing column index and decrementing the row index.
# Similarly if isUp = 0, then decrement the column index and increment the row index.
# Move to the next column or row(next starting row and column
# Do this till all the elements get traversed.

MAX = 100

def DiagonalMatrixTraversal(mat, n):
    i, j, k = 0, 0, 0
    isUp = True

    while (k < n*n):
        if isUp:
            
            # If isUp = True then traverse from downwards to upwards
            while (i >= 0 and j < n):
                print(str(mat[i][j]), end=" ")
                k += 1
                j += 1
                i -= 1

             # Set i and j according to direction
            if (i < 0 and j <= n - 1):
                i = 0
            if (j == n):
                i = i + 2
                j -= 1

        else:

            # If isUp = False then traverse from upwards to downwards
            while (j >= 0 and i < n):
                print(str(mat[i][j]), end=" ")
                k += 1
                j += 1
                i -= 1

             # Set i and j according to direction
            if (j < 0 and i <= n - 1):
                j = 0
            if (i == n):
                j = j + 2
                i -= 1

        #reset flag to change direction
        isUp = not isUp


# Driver program
if __name__ == "__main__":
    mat = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    n = len(mat[0])
    DiagonalMatrixTraversal(mat, n)
