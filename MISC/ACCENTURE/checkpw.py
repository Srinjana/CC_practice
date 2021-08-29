# You are given a function.
# int CheckPassword(char str[], int n)
# The function accepts string str of size n as an argument. Implement the function which returns 1 if given string str is valid password else 0.
# str is a valid password if it satisfies the below conditions.

# – At least 4 characters
# – At least one numeric digit
# – At Least one Capital Letter
# – Must not have space or slash(/)
# – Starting character must not be a number
# Assumption:
# Input string will not be empty.

# Example:

# Input:
# aA1_67
# Output:
# 1

# Sample Input:
# a987 abC012
# Output:
# 0

def checkpeewee(a, S):
    if a < 4:
        return 0
    if s[0].isdigit():
        return 0
    cap = 0
    nu = 0
    for i in range(a):
        if s[i] == ' ' or s[i] == '/':
            return 0
        if s[i] >= 'A' and s[i] <= 'Z':
            cap += 1
        elif s[i].isdigit():
            nu += 1

    if cap > 0 and nu > 0:
        return 1
    else:
        return 0


s = input()
a = len(s)
print(checkpeewee(a, s))
