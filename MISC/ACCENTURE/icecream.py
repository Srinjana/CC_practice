# Sonu and Monu like to pool their money and go to the ice cream parlor. Sonu never buys the same flavor that Monu does. The only other rule they have is that they spend all of their money.

# Given a list of prices for the flavors of ice cream, select the two that will cost all of the money they have.
# For example, they have m=6 to spend and there are flavors costing cost = [1,3,4,5,6] . The two flavors costing 1 and 5 meet the criteria. Using 1-based indexing, they are at indices 1 and 4.

# Accenture coding questions 10
# Input Format
# The first line contains an integer, t, denoting the number of trips to the ice cream parlor. The next t sets of lines each describe a visit. Each trip is described as follows:

# The integer m, the amount of money they have pooled.
# The integer n, the number of flavors offered at the time.
# n space-separated integers denoting the cost of each flavor: cost[cost[1],cost[2],…cost[n]].
# Note: The index within the cost array represents the flavor of the ice cream purchased.

# Output Format
# For each test case, print two space-separated integers denoting the indices of the two flavors purchased, in ascending order.

# Sample Input
# 2
# 4
# 5
# 1 4 5 3 2
# 4
# 4
# 2 2 4 3

# Sample Output
# 1 4
# 1 2

# Explanation
# Sonu and Monu make the following two trips to the parlor:

# The first time, they pool together m=4 dollars. Of the five flavors available that day, flavors 1 and 4 have a total cost of 1+3=4.
# The second time, they pool together m=4 dollars. Of the four flavors available that day, flavors 1 and 2 have a total cost of 2+2 = 4.

def solve(f, m):
    cost_map = {}
    for i, cost in enumerate(f):
        s= money - cost
        if s in cost_map.keys():
            print("{} {}".format(cost_map[s]+1, i+1))
        else:
            cost_map[cost] = i

t = int(input())
for _ in range (t):
    money = int(input())
    n = int(input())
    flavs = list(map(int, input().split()))[:n]

    solve(flavs, money)
