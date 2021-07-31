# Compute the nearest larger number by interchanging its digits updated.Given 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible print -1.

# Input Format
# 2 numbers a and b, separated by space.
# Output Format
# A single number greater than b.
# If not possible, print -1

# Constraints
# 1 <= a,b <= 10000000

# Example 1:

# Sample Input:

#     459 500

# Sample Output:
#     549

# Example 2:

# Sample Input:

#     645757 457765

# Sample Output:
#     465577

import sys

a, b = map(int, input().split())
a = ''.join(sorted(a)[::-1])

if int(a) <= int(b):
    print(-1)
    
    sys.exit()
else:
    if len(a) > len(b):
        print(int(a[::-1]))

        sys.exit()
    else:
        n = len(b)
        a = list(a[::-1])
        s = ''
        n1 = len(a)

        for i in range(n):
            d = b[i]
            j = 0

            while a[j] < b[i] and n1:
                j += 1

            if a[j] > b[i]:
                s += a[j]
                a.remove(a[j])
                a.sort()
                s += ''.join(a)
                print(int(s))

                sys.exit()

            else:
                s1 = s+a[j]
                g = a.copy()
                g.remove(a[j])

                if n1 > 1:
                    g.sort()
                    g = g[::-1]
                    s1 += ''.join(g)

                if int(s1) > int(b):
                    s += a[j]
                    a.remove(a[j])
                    n1 -= 1

                else:
                    while a[j] <= b[i]:

                        j += 1
                    s += a[j]
                    a.remove(a[j])
                    a.sort()
                    s += ''.join(a)
                    print(int(s))

                    sys.exit()

print(int(s))