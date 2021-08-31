# Write a program to find the maximum sum of the elements of an array such that no two elements are adjacent to each other.
# Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).


def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:

        # Current max excluding i (No ternary in Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

    # return max of incl and excl
    return (excl if excl > incl else incl)


# Driver program to test above function
arr = list(map(int, input().split()))
print (find_max_sum(arr))
