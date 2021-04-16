# Shovon is an HR in a renowned company and he is assigning people to work. Now he is assigning people work in a fashion where if he assigns somework a work of cost 2, the next person will be strictly getting a job with cost equal or more than 2. Given that Shovon’s company has infinite work and a number of digitoyees, how many distributions can be possible. The cost of jobs can go 0 to 9.
# N	    Integer	        The number of depts.
# arr[]	Integer array	The number of  digitoyees in each dept..
# Return: The function must return an INTEGER denoting the sum of answers for all distinct distributions
# Author @Srinjana

# Since cost of job ranges 0-9 , upper lim of cost = 9+1 = 10
cost_lim = 10

# RECURSIVE FUNCTION
def func (start, depth, n):
    ans = 0
    if ( depth == n-1):
        return 1
    for i in range (start, cost_lim):
        ans += func(i, depth+1, n)
    return ans

n = int(input())
ans = 0
a = []

for i in range (n):
    a = a.append(i)
    # a = (int(input()))
    for i in range (0, cost_lim):
        ans += func(i, 0, a[i])

print(ans)