# Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits.
# Input: 9834698765123
# Expected Output: 1

number = [n for n in str(input("Enter the number: "))]

even, odd = 0, 0

for i in range(0, len(number)):
    if i % 2 == 0:
        even = even + int(number[i])
    else:
        odd = odd + int(number[i])


print(abs(odd-even))
12
