# An integer d is a divisor of an integer n if the remainder of n/d = 0. Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

# Note: Each digit is considered to be unique, so each occurrence of the same digit should be counted (e.g. for n = 111, 1 is a divisor of 111 each time it occurs so the answer is 3).
# Function Description
# Complete the findDigits function in the editor below. It should return an integer representing the number of digits of d that are divisors of d.
# findDigits has the following parameter(s):

# n: an integer to analyze
# Input Format
# The first line is an integer, t, indicating the number of test cases.
# The t subsequent lines each contain an integer,n .
# Sample Input
# 2
# 12
# 1012
# Sample Output
# 2
# 3
def findDigits(num):
    m = num
    count = 0
    while num != 0:
        a = num % 10
        if a == 0:
            pass
        else:
            if m % a == 0:
                count+=1
            else:
                pass
        num = num//10
    return count

t = int(input())
for t_itr in range(t):
    n = int(input())
    result = findDigits(n)
    print(result)
