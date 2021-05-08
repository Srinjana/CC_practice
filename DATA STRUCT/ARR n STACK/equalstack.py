# You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
# Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height. An empty stack is still a stack
# The first line contains three space-separated integers, , , and , the numbers of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:
# The second line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
# The third line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.
# The fourth line contains  space-separated integers, the cylinder heights in stack . The first element is the top cylinder of the stack.

# @author = Srinjana
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    # reverse stack
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]

    # sum of stack
    sum1 = sum(h1)
    sum2 = sum(h2)
    sum3 = sum(h3)

    # logic
    while(True):
        min_sum = min(sum1, sum2, sum3)

        # base case
        if min_sum == 0:
            return 0

        # general case
        if (min_sum < sum1):
           sum1 -= h1.pop()

        if (min_sum < sum2):
            sum2 -= h2.pop()

        if (min_sum < sum3):
            sum3 -= h3.pop()

        if sum1 == sum2 == sum3:
            return sum1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
