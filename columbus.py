# # SAME AS MAP TRAVERAL PROBLEM
# Nobel Prize-winning Austrian-Irish physicist Erwin Schrödinger developed a machine and brought as many Christopher Columbus from as many parallel universes he could. Actually he was quite amused by the fact that Columbus tried to find India and got America. He planned to dig it further.
# Though totally for research purposes, he made a grid of size n X m, and planted some people of America in a position (x, y) [ in 1 based indexing of the grid], and then planted you with some of your friends in the (n, m) position of the grid. Now he gathered all the Columbus in 1, 1 positions and started a race.
# Given the values for n, m, x, y, you have to tell how many different Columbus(s) together will explore you as India for the first time.
# Remember, the Columbus who will reach to the people of America, will be thinking that as India and hence wont come further.
# Author @Srinjana

import math 

# map coordinates
n = int(input()) - 1
m = int(input()) - 1

# America coordinates
x = int(input()) - 1
y = int(input()) - 1

a = n - x
b = m - y 

# total permutations
ans = math.factorial(n+m)
ans = ans//(math.factorial(n))
ans = ans//(math.factorial(m))

# Blocked Permutations
ans1 = math.factorial(x+y)
ans1 = ans1//(math.factorial(x))
ans1 = ans1//(math.factorial(y))

# Allowed Permutations
ans2 = math.factorial(a+b)
ans2 = ans2//(math.factorial(a))
ans2 = ans2//(math.factorial(b))

# Minimum allowed path
result = int(ans - (ans1 * ans2))
print (result)
