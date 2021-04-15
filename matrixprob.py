# read m and n, take an m*n matrix. If any num is consequtive 3 times in a row or col or diag, then print the number, if there are multiple numbers then print the minimum of those numbers
# Author @Srinjana

row = int(input())
col = int(input())
matrix_digit = []
matrix = []

for r in range (row):
    a = list(map(int, input().split()))
    matrix.append(a)
    # a=[]
    # for c in range (col):
    #     a.append(int(input()))
    # matrix.append(a)

for r in range (0,row):
    for c in range (0,col):
        if (c<col-3):
            if (matrix[r][c] == matrix[r][c+1] == matrix[r][c+2] == matrix[r][c+3]):
                matrix_digit.append(matrix[r][c])

if (r<row-3):
    if (matrix[r][c] == matrix[r+1][c] == matrix[r+2][c] == matrix[r+3][c]):
        matrix_digit.append(matrix[r][c])
        
if (c< col-3 and r>=3):
    if (matrix[r][c] == matrix[r-1][c+1] == matrix[r-2][c+2] == matrix[r-3][c+3]):
        matrix_digit.append(matrix[r][c])

if (c >=3 and r >= 3):
    if (matrix[r][c] == matrix[r-1][c-1] == matrix[r-2][c-2] == matrix[r-3][c-3]):
        matrix_digit.append(matrix[r][c])

if (len(matrix_digit)== 0):
    print(" ")
    print("-1")
else:
    print (" ")
    print ("the answer is: ")
    print(min(matrix_digit))