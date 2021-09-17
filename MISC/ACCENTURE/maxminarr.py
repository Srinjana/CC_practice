# function accepts 2 arrays  and an integer k.
# return the max among the number of elements in arr1 greater than k and numer of elements in arr2 lesser than k


def maxminarr (n1, ar1, n2, ar2, k):
    count1 = 0
    count2 = 0
    for i in range(n1):
        if ar1[i] > k:
            count1+= 1
    for i in range(n2):
        if ar2[i]< k:
            count2 += 1

    res = max(count1, count2)
    return res


n1 = int(input())
ar1 = list(map(int, input().split()))[:n1]
n2 = int(input())
ar2 = list(map(int, input().split()))[:n2]
k = int(input())
print(maxminarr (n1, ar1, n2, ar2, k))

