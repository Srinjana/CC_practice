// # Given a M x N matrix, calculate maximum sum submatrix of size k x k in a given M x N matrix in O(M*N) time. Here, 0 < k < M, N.

// # For example, consider below 5 x 5 matrix

// # [3 - 4 6 - 5 1]
// # [1 - 2 8 - 4 - 2]
// # [3 - 8 9 3 1]
// # [-7 3 4 2 7]
// # [-3 7 - 5 7 - 6]

// # If k = 2, maximum sum k x k sub-matrix is

// # [9 3]
// # [4 2]

// # If k = 3, maximum sum k x k sub-matrix is

// # [8 - 4 - 2]
// # [9 3 1]
// # [4 2 7]

// An efficient C++ program to find maximum sum
// sub-square matrix
#include <bits/stdc++.h>
using namespace std;
 
// Size of given matrix
#define N 5
 
// A O(n^2) function to the maximum sum sub-
// squares of size k x k in a given square
// matrix of size n x n
void printMaxSumSub(int mat[][N], int k)
{
    // k must be smaller than or equal to n
    if (k > N) return;
 
    // 1: PREPROCESSING
    // To store sums of all strips of size k x 1
    int stripSum[N][N];
 
    // Go column by column
    for (int j=0; j<N; j++)
    {
        // Calculate sum of first k x 1 rectangle
        // in this column
        int sum = 0;
        for (int i=0; i<k; i++)
            sum += mat[i][j];
        stripSum[0][j] = sum;
 
        // Calculate sum of remaining rectangles
        for (int i=1; i<N-k+1; i++)
        {
            sum += (mat[i+k-1][j] - mat[i-1][j]);
            stripSum[i][j] = sum;
        }
    }
 
    // max_sum stores maximum sum and its
    // position in matrix
    int max_sum = INT_MIN, *pos = NULL;
 
    // 2: CALCULATE SUM of Sub-Squares using stripSum[][]
    for (int i=0; i<N-k+1; i++)
    {
        // Calculate and print sum of first subsquare
        // in this row
        int sum = 0;
        for (int j = 0; j<k; j++)
            sum += stripSum[i][j];
 
        // Update max_sum and position of result
        if (sum > max_sum)
        {
            max_sum = sum;
            pos = &(mat[i][0]);
        }
 
        // Calculate sum of remaining squares in
        // current row by removing the leftmost
        // strip of previous sub-square and adding
        // a new strip
        for (int j=1; j<N-k+1; j++)
        {
            sum += (stripSum[i][j+k-1] - stripSum[i][j-1]);
 
            // Update max_sum and position of result
            if (sum > max_sum)
            {
                max_sum = sum;
                pos = &(mat[i][j]);
            }
        }
    }
 
    // Print the result matrix
    for (int i=0; i<k; i++)
    {
        for (int j=0; j<k; j++)
            cout << *(pos + i*N + j) << " ";
        cout << endl;
    }
}
 
// Driver program to test above function
int main()
{
    int mat[N][N] = {{1, 1, 1, 1, 1},
        {2, 2, 2, 2, 2},
        {3, 8, 6, 7, 3},
        {4, 4, 4, 4, 4},
        {5, 5, 5, 5, 5},
    };
    int k = 3;
  
    cout << "Maximum sum 3 x 3 matrix is\n";
    printMaxSumSub(mat, k);
 
    return 0;
}
