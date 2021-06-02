// Given weights and values of N items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
// Note: Unlike 0/1 knapsack, you are allowed to break the item.

#include <stdio.h>
#include<conio.h>
#include<stdlib.h>

int n = 5;
float capacity = 50;

int profit[10] = {12, 1, 2, 1, 4};
int weight[10] = {4, 2, 2, 1, 10};

void fractionalKnapsack(float capacity, int n) {
    float x[100], total_cost = 0;
    int i;

    for (i = 0; i < n; i++)
        x[i] = 0.0;

    for (i = 0; i < n; i++)
    {
        if (weight[i] <= capacity)
            {
                x[i] = 1.0;
                total_cost = total_cost + profit[i];
                capacity = capacity - weight[i];
            }
        else
            break;
    }

    if (i < n)
    {
        x[i] = capacity/ weight[i];
    }
    total_cost = total_cost + (x[i] * profit[i]);

//    for(i = 0; i < n; i++){
//        printf("%f\t", x[i]);
//    }
    printf("\nMaximum profit is:- %f", total_cost);
}

void swap(float a, float b)
{
    float temp = a;
    a = b;
    b = temp;
}

int main(){
    int i, j;
    float temp, ratio[10];

    for (i = 0; i < n; i++)
    {
        ratio[i] = profit[i]/weight[i];
    }

    for (i = 0; i < n; i++)
    {
        for(j = i + 1; j < n ; j++)
        {
            if (ratio[i] < ratio[j])
            {
                swap(ratio[i], ratio[j]);

                swap(weight[i], weight[j]);

                swap(profit[i], profit[j]);
            }
        }

    }

    fractionalKnapsack(capacity, n);
    return(0);
}
