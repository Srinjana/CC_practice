#include <stdio.h>
int main()
{
    int x = 6, y = 22, n, i, j, k = 0;

    scanf("%d", &n);
    if (n > 0 && n <= 14)
    {
        for (i = 1; i <= n; i++)
        {
            for (j = i; j < n; j++)
            {
                printf(" ");
            }
            for (k = 1; k <= i; k++)
            {
                printf("%05d ", x);

                x = x + y;

                y = y + 16;
            }
        printf("\n");
        }
    }
    return 0;
}
