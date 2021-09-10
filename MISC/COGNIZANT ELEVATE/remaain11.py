# Question 6 – Find the remainder when a large number is divided by 11


# Problem Statement: Given a number n, the task is to find the remainder when n is divided by 11. The input number may be very large. Since the given number can be very large, you can not use n % 11.


# Input Specification:

# inputs a large number in the form of a string
# Output Specification:

# Return the remainder modulo 11 of input1

def remainder(st):

    # len is variable to store the
    # length of number string.
    ln = len(st)

    rem = 0

    # loop that find remainder
    for i in range(0, ln):
        num = rem * 10 + (int)(st[i])
        rem = num % 11

    return rem


# Driver code
st = "3435346456547566345436457867978"
print(remainder(st))
