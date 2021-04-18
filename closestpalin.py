# Given an integer as input, check for the closest possible palindromes of that number. (one greater and one lesser than the number). Calculate the sum of the numbers and if it is a palindrome print it and if not reduce the input number by 1 and run the comparison again until the sum is a palindrome.

N = int(input())

def isPalindrome(n):
    for i in range(len(n)//2):
        if (n[i] != n[-1 -i]):
            return False
        return True

def closestPalin(num):
    sum = 0

    num1 = num - 1
    while (not isPalindrome(str(abs(num1)))):
        num1 -= 1
    
    num2 = num + 1
    while(not isPalindrome(str(num2))):
        num2 += 1

    sum = int(num1 + num2)

    while (not isPalindrome(str(sum))):
        return (closestPalin(num-1))

    return (sum)

res = closestPalin(N)
print(res)
