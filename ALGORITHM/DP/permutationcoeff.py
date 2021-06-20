# Permutation refers to the process of arranging all the members of a given set to form a sequence. The number of permutations on a set of n elements is given by n!, where “!” represents factorial.

# The Permutation Coefficient represented by P(n, k) is used to represent the number of ways to obtain an ordered subset having k elements from a set of n elements.
# # Mathematically it’s given as:
# P(n, k) = P(n-1, k) + k * P(n-1, k-1)

def perm_coeff(n, k):
    fact = [0 for i in range(n + 1)]

    fact[0] = 1

    # Calculate value of
    # factorials up to n
    for i in range(1, n + 1):

        # (i*i-1*i-2...)
        fact[i] = i * fact[i - 1]

    # P(n, k) = n!/(n-k)!
    return int(fact[n] / fact[n - k])


# Driver code
n, k = [int(x)
        for x in input("Enter n and k values seperated by a space: ").split()]
print(" ")
print("The value of P ({}, {}) is {}".format(n, k, perm_coeff(n, k)))
