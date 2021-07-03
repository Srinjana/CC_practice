# Question. Find the nth term of the series.

# 1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, 64, 729, 128, 2187 ….
# 2(0), 3(0), 2(1), 3(1), 2(2), 3(2), 2(3), 3(3), 2(4), 3(4), 2(5), 3(5), 2(6), 3(6) ….
# This series is a mixture of 2 series – all the odd terms in this series form a geometric series and all the even terms form yet another geometric series. Write a program to find the Nth term in the series.

# The value N in a positive integer that should be read from STDIN.
# The Nth term that is calculated by the program should be written to STDOUT.
# Other than value of n th term, no other character / string or message should be written to STDOUT.
# For example, if N = 16, the 16th term in the series is 2187, so only value 2187 should be printed to STDOUT.
# You can assume that N will not exceed 30.

# this canbe split into two series the power of 2 and the power of 3.
#  all even terms = power of 3 and all odd terms =  power of 2

num = int(input())

if(num % 2 == 0):
    num = num // 2
    print(3**(num-1))
else:
    num = num // 2 + 1
    print(2**(num-1))
