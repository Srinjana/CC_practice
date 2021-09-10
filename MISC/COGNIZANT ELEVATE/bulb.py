# Bulb Factory


# Problem Statement: Jasleen has bought a new bulb factory. The factory has a single file of machines, numbered from 1 to N. Each machine has a certain number of fully prepared bulbs. Allie has a rule she wants to follow. She wants to collect an equal amount of bulbs from each machine from which she collects bulbs. Allie can start collecting bulbs from any machine, but once she starts collecting, she collects from every consecutive machine until she reaches the last machine she wants to collect from. Find the maximum number of bulbs she can collect.


# Input Specification:

# Input1: N, the number of machines
# Input2: An array of N elements(a1, a2 a3……aN], denoting the number of fully prepared bulbs in each machine of the factory.
# Output Specification:

# An integer output denoting the maximum number of bulbs that Allie can collect.


# Test Cases:

# Example 1:

# input1: 3
# Input2: [1, 2, 3]
# Output: 3

# Example 2:

# input1: 4
# Input2: [5, 8, 9, 10]
# Output: 20

# Overall Course Completion percent

n = int(input())
inp = list(map(int, input().split()))[:n]
p = []*100
inp = sorted(inp)

for i in range(n+1):
    p[i] = (n-1)*inp[i]

for i in range(n+1):
    if (p[0] < p[i]):
        p[0] = p[i]

print(p[0])

