# a string has a mixture of letter, integer and special char. from here fin the largest even number combination possible from the available digits after removing duplicates. If no even number, return -1.
# Author @Srinjana

import itertools

s = input()
s_unique = set()
x = -1
for i in s:
    if i.isdigit():
        s_unique.add(i)

# for i in s:
    # print(i)

comb = list(itertools.permutations(s_unique))
for i in comb:
    num = "".join(i)
    if int(num)%2 == 0 and int(num)>x:
        x= int(num)

print(x)
        