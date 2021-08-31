# Write a program where every element in the array is replaced with the greatest element on the right handside of the array and the last element is replaced with -1.
# When there is no element next to the last element, replace it with -1. For example, if the array is {16, 17, 4, 3, 5, 2}, then it should be modified to {17, 5, 5, 5, 2, -1}.

arr = list(map(int, input().split()))
n = len(arr)

m1 = max(arr[0:4])
print(m1)

for i in range (n-1):
    maxim = max(arr[i+1:n])
    arr[i] = maxim

arr[-1] = -1 

print(arr)


