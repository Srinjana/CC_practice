# Given an array arr[] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always - 1.

from collections import deque


def findNextGreaterElements(L):
    n = len(L)
    result = [-1] * n

    # create an empty stack
    s = deque()

    # process each element from right to left
    for i in reversed(range(n)):
        # loop till we have a greater element on top or stack becomes empty.
        while s:
            # pop elements that aren't greater than the current element
            if s[-1] <= L[i]:
                s.pop()
            # the next greater element or -1 is now on the top of the stack
            else:
                result[i] = s[-1]
                break
        # push current element into the stack
        s.append(L[i])

    return result


if __name__ == '__main__':

    L = [2, 7, 3, 5, 4, 6, 8]
    print(L)
    print ("The next greatest elements: ")
    result = findNextGreaterElements(L)
    print(result)
