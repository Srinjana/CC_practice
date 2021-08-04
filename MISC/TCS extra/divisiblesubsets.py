# Given a set of distinct integers, print the size of a maximal subset of S where the sum of any 2 numbers in S’ is not evenly divisible by k.

# Function Description
# It should return an integer representing the length of the longest subset of S meeting the criteria.
# nonDivisibleSubset has the following parameter(s):

# S: an array of integers
# k: an integer
# Input Format
# The first line contains 2 space-separated integers, n and k, the number of values in S and the non factor.
# The second line contains n space-separated integers describing S[i], the unique values of the set.
# Output Format
# Print the size of the largest possible subset (S’).
# Sample Input
# 4 3
# 1 7 2 4
# Sample Output
# 3


def nonDivisibleSubset(k, s):
    temp = [0]*k
    res = 0
    for i in s:
        temp[i % k] += 1                            
    for j in range((k + 2) // 2):                
        if not j or not k % 2 and j == k // 2:
            res += temp[j] > 0                        
        else:
            res += max(temp[j], temp[k - j])             
    return res

    
# Driver Code
n, k = map(int, input().split())
s = list(map(int, input().rstrip().split()))[:n]
result = nonDivisibleSubset(k, s)
print(result)