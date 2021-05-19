
# You have an empty sequence, and you will be given queries. Each query is one of these three types: 1 x - Push the element x into the stack. 2 - Delete the element present at the top of the stack. 3 - Print the maximum element in the stack.

# Input Format

# The first line of input contains an integer, ....

# You can find the full details of the problem Maximum Element at HackerRank


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
# not using array sorry


if __name__ == '__main__':

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = str(input())
        if ops_item[0] == '1':
            val = int(ops_item[2:])
            ops.append(val if len(ops) == 0 else max(val, ops[-1]))
        elif ops_item[0] == '2':
            ops.pop()
        else:
            res = ops[-1]
            print(res)
