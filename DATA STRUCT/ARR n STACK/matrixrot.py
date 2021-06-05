# Write a code to rotate a given matrix by 90 degrees

N = 4

def rotation(matrix):
    for x in range(0, int(N/2)):
        for y in range(x, N-x-1):

            # current is stored in temp
            temp = matrix[x][y]
            #from right to top
            matrix[x][y] = matrix[y][N-1-x]
            # from bottom to right
            matrix[y][N-1-x] = matrix[N-1-x][N-1-y]
            # from left to bottom
            matrix[N-1-x][N-1-y] = matrix[N-1-y][x]
            #  from temp to left
            matrix[N-1-y][x] = temp


def displayMatrix(matrix):

    for i in range(0, N):
        for j in range(0, N):

            print (matrix[i][j], end=' ')
        print("")


mat = [[0 for x in range(N)] for y in range(N)]
mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

rotation(mat)
displayMatrix(mat)
