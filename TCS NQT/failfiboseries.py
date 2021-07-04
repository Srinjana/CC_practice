# Consider the below series:
# 1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…..

# This series is a mixture of 2 series fail the odd terms in this series form a Fibonacci series and all the even terms are the prime numbers in ascending order

# Write a program to find the Nth term in this series

# The value N in a positive integer that should be read from mm. The Nth term that is calculated by the program should be written to STDOUT Otherthan the value of Nth term, no other characters / string or message should be written to STDOUT.

# For example, when N: 14, the 14th term in the series is 17 So only the value 17 should be printed to STDOUT
MAX = 9999999


def fibo(n):
    a, b = 0, 1
    for i in range(n):
        next = a + b
        a = b
        b = next
    
    print(a)


def prime(n):
    count = 1
    for i in range(2, MAX):
        flag = 0
        for j in range(2, i):
             if (i % j == 0):
                flag = 1
                break
        if (flag == 1):
            continue
        else:
            if (count == n):
                print(i)
                break
            else:
                count = count+1


# Driver code
if __name__ == '__main__':
    n = int(input())

    if (n%2 == 0):
        prime(int(n/2))
    else:
        fibo(int(n/2)+1)
