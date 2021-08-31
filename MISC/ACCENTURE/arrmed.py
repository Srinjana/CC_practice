# Write a program to enter two array having the same number of elements and after that print the median of those arrays


def getMedian(ar1, ar2, n):
    
    ar1.extend(ar2)
    ar1= sorted(ar1)
    n1 = len(ar1)

    if (n1%2 != 0):
        median = int(n1/2)
        return ar1[median]
    
    else:
        med1 = int(n1/2)-1
        med2 = int(n1/2)

        avg = (ar1[med1] + ar1[med2])/2
        return (int(avg))


# Driver code to test above function
ar1 = list(map(int, input().split()))
n1 = len(ar1)
ar2 = list(map(int, input().split()))[:n1]
n2 = len(ar2)
if n1 == n2:
    print(getMedian(ar1, ar2, n1))
else:
    print("Error")
