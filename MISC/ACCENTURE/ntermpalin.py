#  You are required to write the code. You can click on compile and run anytime to check compilation/execution status. The code should be logically/syntactically correct.

# Question: Write a program in C such that it takes a lower limit and upper limit as inputs and print all the intermediate pallindrome numbers.

# Test Cases:

# TestCase 1:
# Input :
# 10 , 80
# Expected Result:
# 11 , 22 , 33 , 44 , 55 , 66 , 77.

# Test Case 2:
# Input:
# 100,200
# Expected Result:
# 101 , 111 , 121 , 131 , 141 , 151 , 161 , 171 , 181 , 191.

lo = int(input())
hi = int(input())

rev_lst = []
for i in range(lo, hi+1):
    if str(i) == str(i)[::-1]:
        rev_lst.append(i)

print(*rev_lst, end = " ")
