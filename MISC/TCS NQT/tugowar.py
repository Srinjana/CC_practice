# Given a set of n integers, divide the set in two subsets of n/2 sizes each such that the difference of the sum of two subsets is as minimum as possible. If n is even, then sizes of two subsets must be strictly n/2 and if n is odd, then size of one subset must be(n-1)/2 and size of other subset must be(n+1)/2.

# For example, let given set be {3, 4, 5, -3, 100, 1, 89, 54, 23, 20}, the size of set is 10. Output for this set should be {4, 100, 1, 23, 20} and {3, 5, -3, 89, 54}. Both output subsets are of size 5 and sum of elements in both subsets is same(148 and 148).
# Let us consider another example where n is odd. Let given set be {23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4}. The output subsets should be {45, -34, 12, 98, -1} and {23, 0, -99, 4, 189, 4}. The sums of elements in two subsets are 120 and 121 respectively.

from collections import defaultdict

def Findsubsets(lst):
    M = defaultdict(int)
    for i in range(len(lst)):
        M[lst[i]] += 1
    subsets = [0] * len(M)
    i = 0
    for j in M:
        subsets[i] = M[j]
        i += 1
    return subsets


def subsetSum(subsets, target):

    # dp[i][j] store the answer to

    # form sum j using 1st i elements

    dp = [[0 for x in range(target + 1)]

          for y in range(len(subsets) + 1)]

    # Initialize dp[][] with true

    for i in range(len(dp)):

        dp[i][0] = True

    # Fill the subset table in the

    # bottom up manner

    for i in range(1, len(subsets) + 1):

        for j in range(1, target + 1):

            dp[i][j] = dp[i - 1][j]

            # If current element is

            # less than j

            if (j >= subsets[i - 1]):

                # Update current state

                dp[i][j] |= (dp[i - 1][j -

                                       subsets[i - 1]])

    # Return the result

    return dp[len(subsets)][target]

# Function to check if the given
# array can be split into required sets


def divideInto2Subset(arr, n):

    # Store frequencies of arr[]

    subsets = Findsubsets(arr)

    # If size of arr[] is odd then

    # print "Yes"

    if (n % 2 == 1):

        print("NO")

        return
     # Check if answer is true or not

    isPossible = subsetSum(subsets, n // 2)

    # Print the result

    if (isPossible):

        print("YES")

    else:

        print("NO")

#Driver Code

if __name__ == "__main__":
    iters = int(input())

    for round in range(iters+1):
        n = int(input())
        lst = [int(i) for i in input().split()][:n]
        divideInto2Subset(lst, n)
    
