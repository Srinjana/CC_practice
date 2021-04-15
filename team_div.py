# Consider an array inarr containing at least two non-zero positive integers ranging between 1 to 300 (inclusive of the boundary values). Divide the integers in inarr into two groups based on the below rules:
# Each of the integers should belong to either of the two groups
# The total sum of integers in each of the groups must be as nearly equal as possible
# The total number of integers between the two groups should not differ by more than 1
# Print, outnum1 and outnum2, the sum of the integers of two groups separated by a space. If outnum1 and outnum2 are not equal, then print the smaller sum followed by the larger sum.
# Input Format:
# Read the array inarr elements separated by(‘, ’) comma.
# Read the input from the standard input stream.
# Output Format:
# Print outnum1 and outnum2 in the required order separated by a space.
# Print the output to the standard output stream.
# Author @Srinjana


a = list(map(int, input().split(',')))
n1 = len(a)
n2 = n1//2
sums = sum(a)/2
# print (sums)
# THIS FUNCTION PERFORMS GROUPING
def answer(lenfull, lnsubset, sumation):
    if lenfull < (lnsubset-1):
        return float('inf')
    if lnsubset == 0:
        return abs(sumation)
    else:
        return min(answer(lenfull-1, lnsubset-1, sumation-a[lenfull-1]), answer(lenfull-1, lnsubset, sumation))


k = answer(n1-1, n2, sums)
print(int(sums-k), int(sums+k))
