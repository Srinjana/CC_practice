// kth smallest element of an array of size n without swapping
#include <stdio.h>
#include <conio.h>

clrscr();

void swap(int *a, int *b)
{
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

void minHeapify(int a[], int size, int i)
{
    int l = 2 * i;
    int r = 2 * i + 1;
    int smallest = i;
    if (l < size && a[l] < a[smallest])
        smallest = l;
    if (r < size && a[r] < a[smallest])
        smallest = r;
    if (smallest != i)
    {
        swap(&a[i], &a[smallest]);
        minHeapify(a, size, smallest);
    }
}

void buildMinHeap(int a[], int size)
{
    int i;
    for (i = size / 2; i >= 0; i--)
        minHeapify(a, size, i);
}

int kthsmallest(int a[], int size, int k)
{
    k = size - k + 1;
    int minHeap[1000];
    int i;
    for (i = 0; i < k; i++)
        minHeap[i] = a[i];
    buildMinHeap(minHeap, k);
    for (i = k; i < size; i++)
    {
        if (a[i] > minHeap[0])
        {
            minHeap[0] = a[i];
            minHeapify(minHeap, k, 0);
        }
    }
    return minHeap[0];
}

int main()
{
    printf("Enter the size of the set\n");
    int size;
    scanf("%d", &size);
    printf("Enter a set of %d integers\n", size);
    int arr[100];
    int i;
    for (i = 0; i < size; i++)
        scanf("%d", &arr[i]);
    printf("Enter the value of i\n");
    int k;
    scanf("%d", &k);
    printf("%d is the %dth smallest element", kthsmallest(arr, size, k), k);
    return 0;
}