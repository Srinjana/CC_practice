# The binary number system only uses two digits, 0 and 1. Any string that represents a number in the binary number system can be called a binary string. You are required to implement the following function:

# int OperationsBinaryString(char * str)


# The function accepts a string 'str' as its argument. The string 'str' consists of binary digits separated with an alphabet as follows:

# 'A' denotes AND operation
# 'B' denotes OR operation
# 'C' denotes XOR operation
# You are required to calculate the result of the string 'str', scanning the string left to right, taking one operation at a time, and return the same.


# Note:

# No order of priorities of operations is required.
# Length of 'str' is odd
# If 'str' is NULL or None(in case of python), return -1 


# Example:


# Input:

# str: ICOCICIAOBI


# Output:

# 1


# Explanation:

# The alphabet in 'str' when expanded becomes "1 XOR 0 XOR 1 XOR 1 AND 0 OR 1", the result of the expression becomes 1, hence 1 is returned.


# Code Solution in C++:


# Sample Input:

# str: 0C1A1B1C1C1B0A0

def OperationsBinaryString(str):
    a = int(str[0])
    i = 1
    while i < len(str):
        if str[i] == 'A':
            a &= int(str[i+1])
        elif str[i] == 'B':
            a |= int(str[i+1])
        else:
            a ^= int(str[i+1])
        i += 2
    return a


str = input()
print(OperationsBinaryString(str))
