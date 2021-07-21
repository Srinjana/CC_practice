# Given a positive integer N, print count of set bits in it. 

# Example 1:

# Input:
# N = 6
# Output:
# 2
# Explanation:
# Binary representation is '110' 
# So the count of the set bit is 2.


def deci_bin(num):
    if (num == 0):
        return ''
    else:
        return (deci_bin(num//2)) + str(num % 2)

def count (lst):
    cnt = 0
    for i in range(0, len(lst)):
        if (lst[i] == 1):
            cnt += 1
    return cnt

decimal = int(input("Enter number: "))
binary = deci_bin(decimal)
lst = [int(b) for b in str(binary)]

res = count(lst)
print(res)