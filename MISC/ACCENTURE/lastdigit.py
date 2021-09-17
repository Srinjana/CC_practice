# input a and b, find the last digit of smaller^bigger

import math

a = int(input())
b = int(input())
if (a>=b):
    val = math.pow(b,a)
else:
    val = math.pow(a,b)
val = int(val)
print (val)
res = [int(d) for d in str(val)]
print(res[-1])
