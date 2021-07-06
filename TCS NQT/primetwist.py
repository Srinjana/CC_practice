# Ques. Write a code to check whether no is prime or not. Condition use function check() to find whether entered no is positive or negative, if negative then enter the no, And if yes pas no as a parameter to prime() and check whether no is prime or not?

def check(num):
    if (num <= 0):
        print("Please enter a positive number.")


def prime(num):

    if (num == 1):
        return 0

    for i in range(2, num):
        if (num % i) == 0:
            return 0
            # break
        else:
            return 1


if __name__ == '__main__':
    num = int(input())
    check(num)
    res = prime(num)

    if res == 0:
        print("NON PRIME")
    elif res == 1:
        print("PRIME")
    else:
        print("ERROR")