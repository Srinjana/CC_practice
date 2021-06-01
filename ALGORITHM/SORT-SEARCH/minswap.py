# Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.

def minSwaps(arr):
    n = len(arr)
    print (arr)
    #make an array containing indexes of unsorted array and sort them to obtain correct positions
    index = [*enumerate(arr)]
    # print(index)
    index.sort(key = lambda x : x[1])
    # print(index)

    #initialize all elements as not visited
    visited = {k: False for k in range(n)}
    # print(visited)

    ans = 0
    for i in range(n):
        # if already swapped or in correct place
        if visited[i] or index[i][0] == i:
            continue
        
        # find number of elements in this cycle and add to ans
        cycle_size = 0
        j = i

        while not visited[j]:
            # mark node as visited
            visited[j] = True

            # go to next node
            j = index[j][0]
            cycle_size += 1

        # Add answer by adding current cycle 
        if cycle_size > 0:
            ans += (cycle_size - 1)

    return ans


# Driver Code
arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))
