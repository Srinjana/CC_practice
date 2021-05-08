# Declare a 2-dimensional array, arr, of n empty arrays. All arrays are zero indexed.
# Declare an integer,lastanswer , and initialize it to 0.
# There are 2 types of queries, given as an array of strings for you to parse:

# Query: 1 x y
# Let idx = (x XOR lastanswer)%n
# Append the integer y to arr[idx].

# Query: 2 x y
# Let idx = (x XOR lastanswer)%n
# Assign the value arr[idx][y%size(arr[idx])] to lastanswer.
# Store the new value of lastanswer to an answers array.
# @author Srinjana

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    last_answer = 0
    arr = [[] for i in range(n)]
    ans = []

    for q in queries:
        data = (q[1] ^ last_answer) % n

        # QUERY IS 1
        if q[0] == 1:
            arr[data].append(q[2])

        # QUERY IS 2
        elif q[0] == 2:
            index = q[2] % len(arr[data])
            last_answer = arr[data][index]
            ans.append(last_answer)

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
