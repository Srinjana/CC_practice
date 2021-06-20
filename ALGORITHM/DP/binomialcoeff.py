# Write a function that takes two parameters n and k and returns the value of Binomial Coefficient C(n, k). For example, your function should return 6 for n = 4 and k = 2, and it should return 10 for n = 5 and k = 2.

# C(n, k) = C(n-1, k-1) + C(n-1, k)
# C(n, 0) = C(n, n) = 1

def Binomial_coeff(n, k):
    m = (10**9 + 7)
    if (k > n):
        return 0
    elif (k == 0 or k == n) :
        return 1
    else:
        res = Binomial_coeff(n-1, k-1) + Binomial_coeff(n-1, k)
        res = res % m
        return res


# Driver code


n, k = [int(x) for x in input("Enter n and k values seperated by space: ").split()]
print(" ")
print ("The value of C ({}, {}) is {}".format(n, k, Binomial_coeff(n, k)))
