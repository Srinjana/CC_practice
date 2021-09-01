# Vohra joined a social networking site to stay in touch with his friends. The signup page required him to input a name and a password. However, the password must be strong. The website considers a password to be strong if it satisfies the following criteria:

# Its length is at least 6.
# It contains at least one digit.
# It contains at least one lowercase English character.
# It contains at least one uppercase English character.
# It contains at least one special character. The special characters are: !@  # $%^&*()-+
# He typed a random string of length n in the password field but wasn’t sure if it was strong. Given the string he typed, can you find the minimum number of characters he must add to make his password strong?

# Note: Here’s the set of types of characters in a form you can paste in your solution:
# numbers = “0123456789”
# lower_case = “abcdefghijklmnopqrstuvwxyz”
# upper_case = “ABCDEFGHIJKLMNOPQRSTUVWXYZ”
# special_characters = “!@  # $%^&*()-+”

# Input Format
# The first line contains an integer n denoting the length of the string.
# The second line contains a string consisting of n characters, the password typed by Vohra. Each character is either a lowercase/uppercase English alphabet, a digit, or a special character.

# Output Format
# Print a single line containing a single integer denoting the answer to the problem.

# Sample Input
# 3
# Ab1
# Sample Output
# 3
# Explanation
# She can make the password strong by adding 3 characters, for example, $hk, turning the password into Ab1$hk which is strong.
# 3 characters aren’t enough since the length must be at least 6.

numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"


def minimumNumber(n, password):
    res = 0

    if not any(x in numbers for x in password):
        res += 1

    if not any(x in lower_case for x in password):
        res += 1

    if not any(x in upper_case for x in password):
        res += 1

    if not any(x in special_characters for x in password):
        res += 1

    if len(password) < 6:
        return max(res, 6 - len(password))

    return res


n = int(input())
password = input()
answer = minimumNumber(n, password)
print(str(answer) + '\n')
