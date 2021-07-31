# n this even odd problem Given a range [low, high] (both inclusive), select K numbers from the range (a number can be chosen multiple times) such that sum of those K numbers is even.

# Calculate the number of all such permutations.

# As this number can be large, print it modulo (1e9 +7).

# Constraints

# 0 <= low <= high <= 10^9
# K <= 10^6.
# Input

# First line contains two space separated integers denoting low and high respectively
# Second line contains a single integer K.
# Output

# Print a single integer denoting the number of all such permutations
# Time Limit

# 1

# Examples

# Example 1

# Input

# 4 5

# 3

# Output

# 4

# Explanation

# There are 4 valid permutations viz. {4, 4, 4}, {4, 5, 5}, {5, 4, 5} and {5, 5, 4} which sum up to an even number.

# Example 2

# Input

# 1 10

# 2

# Output

# 50

# Explanation

# There are 50 valid permutations viz. {1,1}, {1, 3},.. {1, 9} {2,2}, {2, 4},… {2, 10} . . . {10, 2}, {10, 4},… {10, 10}. These 50 permutations, each sum up to an even number.


mod = 1000000007
# Function to return the number
# of all permutations such that
# sum of K numbers in range is even


def countEvenSum(low, high, k):

    even_count = high / 2 - (low - 1) / 2
    odd_count = (high + 1) / 2 - low / 2

    even_sum = 1
    odd_sum = 0

    # Iterate loop k times and update
    # even_sum & odd_sum using
    # previous values
    for i in range(0, k):

        # Update the prev_even and
        # odd_sum
        prev_even = even_sum
        prev_odd = odd_sum

        # Even sum
        even_sum = ((prev_even * even_count) + (prev_odd * odd_count))

        # Odd sum
        odd_sum = ((prev_even * odd_count) + (prev_odd * even_count))

    # Return even_sum
    return int(even_sum)

# Driver Code

high, low = map(int, input().split())
k = int(input())

res = countEvenSum(high, low, k) % mod
print(res)
