# Tom is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Tom: one is black and the other is white. To make her happy, Tom has to buy b black gifts and w white gifts.

# The cost of each black gift is bc units.
# The cost of every white gift is wc units.
# The cost of converting each black gift into a white gift or vice versa is z units.
# Help Tom by deducing the minimum amount he needs to spend on Diksha’s gifts.

# Function Description
# Complete the function tomBday in the editor below. It should return the minimal cost of obtaining the desired gifts.
# tomBday has the following parameter(s):

# b: the number of black gifts
# w: the number of white gifts
# bc: the cost of a black gift
# wc: the cost of a white gift
# z: the cost to convert one color gift to the other color
# Input Format
# The first line will contain an integer t, the number of test cases.
# The next t pairs of lines are as follows:

# The first line contains the values of integers b and w.
# The next line contains the values of integers bc, wc, and z.
# Output Format
# t lines, each containing an integer: the minimum amount of units Tom needs to spend on gifts.
# Sample Input
# 5
# 10 10
# 1 1 1
# 5 9
# 2 3 4
# 3 6
# 9 1 1
# 7 7
# 4 2 1
# 3 3
# 1 9 2
# Sample Output
# 20
# 37
# 12
# 35
# 12


def taumBday(b, w, bc, wc, z):

    originalCost = b*bc + w*wc
    if bc < wc:
        wc = bc+z
    else:
        bc = wc+z

    calculatedCost = b*bc+w*wc
    if calculatedCost < originalCost:
        return calculatedCost
    else:
        return originalCost


t = int(input().strip())

for t_itr in range(t):

    first_multiple_input = input().rstrip().split()
    b = int(first_multiple_input[0])
    w = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()
    bc = int(second_multiple_input[0])
    wc = int(second_multiple_input[1])
    z = int(second_multiple_input[2])

    result = taumBday(b, w, bc, wc, z)
    print(result)
