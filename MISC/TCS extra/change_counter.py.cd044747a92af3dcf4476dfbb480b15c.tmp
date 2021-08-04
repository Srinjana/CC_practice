# Change Counter
# You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities. The value of each coin is already given. Can you determine the number of ways of making change for a particular number of units using the given types of coins?

# Function Description
# It must return an integer denoting the number of ways to make change.
# getWays has the following parameter(s):

# n: an integer, the amount to make change for
# c: an array of integers representing available denominations
# Input Format
# The first line contains two space-separated integers describing the respective values of n and m, where:
# n is the number of units
# m is the number of coin types
# The second line contains m space-separated integers describing the respective values of each coin type : c = c[0], c[1], … c[m-1](the list of distinct coins available in infinite amounts).
# Output Format
# Print a long integer denoting the number of ways we can get a sum of n from the given infinite supply of m types of coins.
# Sample Input
# 4 3
# 1 2 3
# Sample Output
# 4

n, m = map(int,input().split())
coins = list(map(int,input().split()))
dp = [1]+[0]*n
for i in range(m): 
    for j in range(coins[i], n+1): dp[j]+=dp[j-coins[i]]
print(dp[-1])