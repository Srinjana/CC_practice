# Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = {S1, S2, .., SM} valued coins.

# Example 1:

# Input:
# n = 4, m = 3
# S[] = {1, 2, 3}
# Output: 4
# Explanation: Four Possible ways are:
# {1, 1, 1, 1}, {1, 1, 2}, {2, 2}, {1, 3}.

def count(array, m, n):
    if n == 0:
        return 1
    if (n < 0):
        return 0
    if (m <= 0 and n >= 1):
        return 0
    return count(array, m-1, n) + count (array, m, n-array[m-1])
    
# Driver Code  
if __name__ == "__main__":  
    arr = [1, 2, 3]
    m = len(arr)
    print(count(arr, m, 4))
