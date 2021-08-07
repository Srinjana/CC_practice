# Rotate a list clockwise K times


def rightrot(n, a, k):
    k = k% n
    for i in range(0, n):
        if (i < k):
            print(a[n+i-k], end = " ")
        else:
            print(a[i - k], end = " ")
        
    
n = int(input())
Arr = [int(i) for i in input().split()][:n]
k = int(input())

rightrot(n, Arr, k)