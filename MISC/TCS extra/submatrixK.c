// Given an n x n square matrix, find sum of all sub - squares of size k x k where k is smaller than or equal to n.

#include <stdio.h>

int main()
{
    int n, k, i, j, a[100][100], b[100][100], m, l, sum = 0;
    scanf("% d", &n);
    scanf("% d", &k);
    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            scanf("%d", &a[i][j]);
        }
    }
    for (m = 0; m < k; m++)
    {
        for (l = 0; l < k; l++)
        {
            for (i = m; i < m + k; i++)
            {
                for (j = l; j < l + k; j++)
                {
                    sum = sum + a[i][j];
                }
            }
            b[m][l] = sum;
            sum = 0;
        }
    }
    for (m = 0; m < k; m++)
    {
        for (l = 0; l < k; l++)
        {
            printf("%d ", b[m][l]);
        }
        printf("\n");
    }
}