# Given a sequence of n integers p(1), p(2), …p(n), where each element is distinct and satisfies 1 <= p(x) <= n. For each x where 1 <= x <= n, find any integer y such that p(p(y)) = x and print the value of y on a new line.
# Input Format

# The first line contains an integer n, the number of elements in the sequence.
# The second line contains n space-separated integers p[i] where 1 <= i <= n.

# Output Format

# For each x from 1 to n, print an integer denoting any valid y satisfying the equation p(p(y)) on a new line.

# Sample Input

# 3

# 2 3 1

# Sample Output

# 2

# 3

# 1

def soln(p, n):
    for i in range(1, n+1):
        for y in range(n):
            if p[p[y]-1] == i:
                print(y+1)


n = int(input())
p = [int(i) for i in input().split()][:n]
# print(p)
soln(p, n)
