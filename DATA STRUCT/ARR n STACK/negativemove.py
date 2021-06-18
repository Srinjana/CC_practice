# MOVE ALL NEGATIVE ELEMENTS TO ONE SIDE OF AN ARRAY

def segregateElements(arr , n):
    temp = [0] * n
    j = 0  # index of temp
    for i in range(n):
        if (arr[i] >= 0):
            temp[j] = arr[i]
            j += 1

    if (j == n or j == 0):
        return

    for i in range(n):
        if (arr[i] < 0):
            temp[j] = arr[i]
            j += 1
    
    for k in range(n):
        arr[k] = temp[k]
    



arr = [1 ,-1 ,-3 , -2, 7, 5, 11, 6 ] 
n = len(arr)

segregateElements(arr, n)
   
for i in range(n): 
    print (arr[i], end=" ")
    
