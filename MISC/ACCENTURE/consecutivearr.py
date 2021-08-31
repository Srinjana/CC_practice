# Write a program to print the elements of the array that are consecutive in nature.
# Example:

# Sample input: 5
# Sample output: 20 23 24 22 21
# Array elements are consecutive

n = int(input())
ar = list(map(int, input().split()))[:n]
var = 0
ar = sorted(ar)
# print(ar)

for i in range(n-2):
    if ar[i]+1 != ar[i+1]:
        var += 1

if var == 0:
    print("consecutive")
else:
    print("not consecutive")
