# Find the numbers
# A modified Kaprekar number is a positive whole number with a special property. If you square it, then split the number into two integers and sum those integers, you have the same value you started with. Consider a positive whole number n with d digits. We square n to arrive at a number that is either 2 x d digits long or (2 x d)-1 digits long. Split the string representation of the square into two parts, l and r. The right-hand part r must be d digits long. The left is the remaining substring. Convert those two substrings back to integers, add them and see if you get n.

# Note: r may have leading zeros.
# Here’s an explanation from Wikipedia about the ORIGINAL Kaprekar number(spot the difference!):
# In mathematics, a Kaprekar number for a given base is a non-negative integer, the representation of whose square in that base can be split into two parts that add up to the original number again. For instance, 45 is a Kaprekar number, because 45² = 2025 and 20+25 = 45.
# Given two positive integers p and q where p is lower than q, write a program to print the modified Kaprekar numbers in the range between p and q, inclusive.
# Function Description
# Complete the kaprekarNumbers function in the editor below. It should print the list of modified Kaprekar numbers in ascending order.
# kaprekarNumbers has the following parameter(s):

# p: an integer
# q: an integer
# Input Format
# The first line contains the lower integer limit p.
# The second line contains the upper integer limit q.
# Note: Your range should be inclusive of the limits.
# Output Format
# Output each modified Kaprekar number in the given range, space-separated on a single line. If no modified Kaprekar numbers exist in the given range, print INVALID RANGE.
# Sample Input
# 1
# 100
# Sample Output
# 1 9 45 55 99



def kaprekarNumbers(p, q):
    c = []
    if p == 1 or p < 4:
        if p == 1:
            c.append(1)
        for i in range(4, q+1):
            a = i**2
            k = str(a)
            j = k[:len(k)//2]
            m = k[len(k)//2:len(k)]
            s = int(j)
            f = int(m)
            if s + f == i:
                c.append(i)
        for e in c:
            print(e, end=" ")
    else:
        for i in range(p, q+1):
            a = i**2
            k = str(a)
            j = k[:len(k)//2]
            m = k[len(k)//2:len(k)]
            s = int(j)
            f = int(m)
            if s + f == i:
                c.append(i)
        if len(c) <= 0:
            print('INVALID RANGE')
        else:
            for e in c:
                print(e, end=" ")


p = int(input())
q = int(input())
kaprekarNumbers(p, q)
