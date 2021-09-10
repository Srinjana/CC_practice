# After Watching a movie at PVR, Adil is pondering over the number of ways in which he can pay for the movie. He has x1, x2, x3, x4 coins of values 1,2,5 and 10 respectively. He wants to determine the number of ways in which he can pay an amount A.

# You need to fill in a function that returns the number of ways to pay total amount

# Input Specifications:

# Input 1: An integer value denoting the total amount to be paid

# Output Specification:
# Return an Integer value denoting the number of ways to pay the total amount

# Example1:
# Input1: 40
# Output : 195

# Example2:
# Input1: 4
# Output : 3


def find_possible_ways(coins, sum):
    size = 4

    # Declaring a 2-D array
    # for storing solutions to subproblems:
    arr = [[0] * (sum + 1) for x in range(size + 1)]

    # Initializing first column of array to 1
    # because a sum of 0 can be made
    # in one possible way: {0}
    for i in range(size + 1):
        arr[i][0] = 1

    # Applying the recursive solution:
    for i in range(1, size + 1):
        for j in range(1, sum + 1):
            if coins[i - 1] > j:  # Cannot pick the highest coin:
                arr[i][j] = arr[i - 1][j]
            else:  # Pick the highest coin:
                arr[i][j] = arr[i - 1][j] + arr[i][j - coins[i - 1]]

    return arr[size][sum]


total_p = int(input())
coins = [1, 2, 5, 10]
print(find_possible_ways(coins, total_p))
