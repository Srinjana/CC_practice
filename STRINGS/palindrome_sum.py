# For a given positive number num, identify the palindrome formed by performing the following operations-
# Add num and its reverse
# Check whether the sum is palindrome or not. If not, add the sum and its reverse and repeat the process until a palindrome is obtained
# Author @Srinjana

def isPalindrome(n):
    return str(n)[::-1] == str(n)


def reverse(n):
    return int(str(n)[::-1])


n = int(input())
while(1):
    n = n + reverse(n)
    if (isPalindrome(n)):
        print (n)
        break
    

