# Chocolate distribution
# Christy is interning at PrepInsta. One day she has to distribute some chocolates to her colleagues. She is biased towards her friends and plans to give them more than the others. One of the program managers hears of this and tells her to make sure everyone gets the same number.

# To make things difficult, she must equalize the number of chocolates in a series of operations. For each operation, she can give 1, 2 or 5 chocolates to all but one colleague. Everyone who gets chocolate in a round receives the same number of pieces.
# Function Description
# It should return an integer that reperesents the minimum number of operations required.
# equal has the following parameter(s):

# arr: an array of integers to equalize
# Input Format
# The first line contains an integer t, the number of test cases.
# Each test case has 2 lines.

# The first line contains an integer n, the number of colleagues.
# The second line contains n space-separated integers denoting the number of chocolates each colleague has.
# Output Format
# Print the minimum number of operations needed for each test case, one to a line.
# Sample Input
# 1
# 4
# 2 2 3 7
# Sample Output
# 2

def minOpers(interns, target):
    count = 0
    for curr in interns:
        if curr - target >= 5:
            count += (curr - target) // 5
            curr = target + (curr - target) % 5
        if curr - target >= 2:
            count += (curr - target) // 2
            curr = target + (curr - target) % 2
        if curr - target == 1:
            count += 1
    return count

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    interns = input().strip().split(' ')
    interns = sorted([int(i) for i in interns])
    target = interns[0]
    scores = [minOpers(interns, target)]
    if target >= 2:
        scores.append(minOpers(interns, target - 2))
    if target >= 1:
        scores.append(minOpers(interns, target - 1))
    print(min(scores))