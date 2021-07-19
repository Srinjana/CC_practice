// Given an n x n matrix.In the given matrix, you have to print the elements of the matrix in the snake pattern.

//                                            Examples :

//     Input : mat[][] = {{10, 20, 30, 40},
//                                            {15, 25, 35, 45},
//                                            {27, 29, 37, 48},
//                                            {32, 33, 39, 50}};

// Output : 10 20 30 40 45 35 25 15 27 29 37 48 50 39 33 32

#include<stdio.h>
#include<conio.h>
#define M  4
#define N  4

void Snake(int mat[M][N])
{   
    int i;
    for (int i = 0; i < M; i++)
    {

        // If current row is even, print from
        // left to right
        if (i % 2 == 0)
        {
            for (int j = 0; j < N; j++)
                printf(" %d ",mat[i][j]);

            // If current row is odd, print from
            // right to left
        }
        else
        {
            for (int j = N - 1; j >= 0; j--)
                printf(" %d ", mat[i][j]);
        }
    }
}


// Driver code
int main()
{
    int mat[M][N] = {{10, 20, 30, 40},
                   {15, 25, 35, 45},
                   {27, 29, 37, 48},
                   {32, 33, 39, 50}};
                   
    
    Snake(mat);
    return 0;
}