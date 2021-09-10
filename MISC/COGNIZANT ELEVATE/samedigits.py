# Given a positive whole number n, find the smallest number which has the very same digits existing in the whole number n and is greater than n. In the event that no such certain number exists, return – 1.  Note that the returned number should fit in a 32-digit number, if there is a substantial answer however it doesn’t fit in a 32-bit number, return – 1.


# Test Cases:

#  Example 1:

# Input: n = 12
# Output: 21
# Explanation:

# Using the same digit as the number of permutations, the next greatest number for 12 is 21.

# Example 2:

# Input: n = 21
# Output: -1
# Explanation:

# The returned integer does not fit in a 32-bit integer


n = input()
nl = [x for x in n]
nl = sorted(nl)
# print(nl)
nf = ("".join(nl))
# print(nf)
if nf == n:
    print(-1)
else: 
    print(int(nf))