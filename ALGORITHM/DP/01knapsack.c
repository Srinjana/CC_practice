#include<stdio.h>
#include<conio.h>

clrscr();

int max(int x, int y) 
{
    // MACROS
    return (x > y) ? x : y;
}

int knapsack(int W, int wt[], int val[], int n)
{
    int i, w;
    int k[n+1][W+1];
    for(int i = 0; i <=n; i++){
        for(int w = 0; w <= W; w++){
            if (i == 0 || w == 0)
            {
                k[i][w] = 0;
            }
            else if (wt[i] <= wt[w])
            {
                k[i][w] = max(val[i - 1] + k[i - 1][w - wt[i - 1]], k[i - 1][w]);
            }
            else
            {
                k[i][w] = k[i - 1][w];
            }

        }
    return k[n][w];
    }
}

    int main()
{
    int i, n, val[20], wt[20], W;

    printf("Enter number of items:");
    scanf("%d", &n);

    printf("Enter value and weight of items:\n");
    for (i = 0; i < n; ++i)
    {
        scanf("%d %d", &val[i], &wt[i]);
    }

    printf("Enter size of knapsack:");
    scanf("%d", &W);

    printf("%d", knapSack(W, wt, val, n));
    return 0;
}