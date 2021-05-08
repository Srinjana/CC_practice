# Given a 6x6 2D Array,arr :
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g
# There are  hourglasses in . An hourglass sum is the sum of an hourglass' values. Calculate the hourglass sum for every hourglass in , then print the maximum hourglass sum. The array will always be 6x6.
# @author = srinjana

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
row = 6
col = 6


def hourglassSum(arr):
    # Write your code here
    max_sum = -80000
    #if (row < 3 and col < 3):
    #return -1
    for i in range(0, row-2):
        for j in range(0, col-2):
            arr_sum = (arr[i][j] + arr[i][j+1] + arr[i][j+2]) + (arr[i+1]
                                                                 [j+1]) + (arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
            if (arr_sum > max_sum):
                max_sum = arr_sum
            else:
                continue
    return max_sum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
