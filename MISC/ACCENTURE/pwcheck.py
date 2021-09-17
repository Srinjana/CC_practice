
# You are given a function: 

# int CheckPassword(char str[ ], int n);

# The function accepts string 'std of size int as argument Implement the function which returns 1 if given string 'str' is a valid password else 0. 

# 'str' is a valid password if it satisfies below conditions: 

# At least 4 characters 
# At least one numeric digit 
# At least one Capital letter 
# Must not have space or slash (/) 
# Starting character must not be a number 
# Assumption: Input string will not be empty. 



# Example:

# Input: 
# aA1_67 


# Output: 
# 1 


# Sample Input:

# a987 abC012 

pw = input()
n = len(pw)

if n < 4:
    print (0)

if s[0].isdigit():
    print 0

cap=0
nu=0
for i in range(n):

    if s[i]==' ' or s[i]=='/':
        print 0
    if s[i]>='A' and s[i]<='Z':
        cap+=1
    elif s[i].isdigit():
        nu+=1
 
if cap>0 and nu>0:
    print 1
else:
    print 0
