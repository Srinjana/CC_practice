# Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

# Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
# Count the number of possible Binary Search Trees with n keys (See this)
# Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
# Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.
# See this for more applications. 
# The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …  

# can be solved using recursive formula [SUMATION{for i in range(0,n+1)}(Ci *C(n-i))]
# RECURSIVE

def catalan(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)

    return res

def DynamicCatalan(n):
    if (n == 0 or n == 1):
        return 1
    # Table to store results of subproblems
    catalan = [0]*(n+1)
    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i-j-1]

    # Return last entry
    return catalan[n]

# Driver Code
for i in range(10):
    print (catalan(i))
    print(DynamicCatalan(i))
