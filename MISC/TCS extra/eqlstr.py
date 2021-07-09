# Given an array of equal-length strings arr[], the task is to make all the strings of the array equal by replacing any character of a string with any other character, minimum number of times.

# Examples:

# Input: arr[] = {“west”, “east”, “wait”}
# Output: 3
# Explanation:
# Replacing arr[0][1] with ‘a’ modifies arr[] to {“west”, “east”, “wait”}.
# Replacing arr[1][0] with ‘w’ modifies arr[] to {“wast”, “wast”, “wait”}.
# Replacing arr[2][2] with ‘s’ modifies arr[] to {“wast”, “wast”, “wast”}.
# Therefore, the required output is 3.

# Approach: The problem can be solved using Hashing. Follow the steps below to solve the problem:


# Initialize a 2D array, say hash[][], where hash[i][j] stores the frequency of the character i present at the jth index of all the strings.
# Traverse the array arr[] using variable i. For every ith string encountered, count the frequency of each distinct character of the string and store it into the hash[][] array.
# Initialize a variable, say cntMinOp, to store the minimum count of operations required to make all the strings of the array equal.
# Traverse the array hash[][] using variable i. For every ith column encountered, calculate the sum of the column, say Sum, the maximum element in the column, say Max, and update cntMinOp += (Sum – Max).
# Finally, print the value of cntMinOp.


def minOperation(lst, n):
    cntMinOp = 0
    strLen = len(lst[0])

    hash = [[0 for i in range(strLen)] for j in range(256)]

    for i in range(n):
        for j in range(strLen):

            # logs the frequency of characters 
            hash[ord(lst[i][j])][j] += 1
    
    for i in range(strLen):
        # Stores sum of i-th column and max element of ith column
        sum, maxm = 0, 0

        for j in range(256):
            sum += hash[j][i]
            maxm = max(maxm, hash[j][i])

            cntMinOp += (sum - maxm)

    return(cntMinOp)



if __name__ == '__main__':

    arr = (input().split())
    N = len(arr)

    # Function call
    print(minOperation(arr, N))
