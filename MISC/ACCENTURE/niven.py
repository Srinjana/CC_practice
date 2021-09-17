# A number is said to be the Niven number if it is divisible by the sum of its digit.

# For example, if number is 156, then sum of its digit will be 1 + 5 + 6 = 12. Since 156 is divisible by 12. So, 156 is a Niven number.

# Some of the other examples of Niven number are 8, 54, 120, etc.

# To find whether the given number is a Niven number or not, calculate the sum of the digit of the number then, check whether the given number is divisible by the sum of its digit. If yes, then given number is a Niven number.

n = int(input())
lst = [int(d) for d in str(n)]
# print(*lst)
sum = sum(lst)
# print(sum)

if (n%sum == 0):
    print (n//sum)
else:
    print(0)
