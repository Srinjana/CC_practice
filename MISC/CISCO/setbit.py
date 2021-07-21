# from right is 0. The number after changing
# Given a number N and a value K. From the right, set the Kth bit in the binary representation of N. The position of Least Significant Bit(or last bit) is 0, the second last bit is 1 and so on. 

# Example 1:

# Input:
# N = 10
# K = 2
# Output:
# 14
# Explanation:
# Binary representation of the given number
# 10 is : 1 0 1 0, number of bits in the
# binary reprsentation is 4. Thus 2nd bit
# this bit to 1 is: 14(1 1 1 0).

def deci_bin(num):
    if (num == 0):
        return ''
    else:
        return (deci_bin(num//2)) + str(num%2)

def bitreverse(lst, bit):
    if(lst[-bit] == 0):
        lst[-bit] = 1
    else:
        lst[-bit] = 0

decimal = int(input("Enter number: "))
bit = int(input("Enter Bit value: "))

binary = deci_bin(decimal)
lst = [int(b) for b in str(binary)]
# print(lst)
bitreverse(lst, bit)
# print(lst)
res = int("".join(map(str,lst)))
print(res)



