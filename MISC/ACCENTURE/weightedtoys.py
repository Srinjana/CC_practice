# Pragati works for an international gifts company that ships by container. Her task is to determine the lowest cost way to combine her orders for shipping. She has a list of item weights. The shipping company has a requirement that all items loaded in a container must weigh less than or equal to 4 units plus the weight of the minimum weight item. All items meeting that requirement will be shipped in one container.

# What is the smallest number of containers that can be contracted to ship the items based on the given list of weights?


# For example, there are items with weights w = [1, 2, 3, 4, 5, 10, 11, 12, 13]. This can be broken into two containers: [1, 2, 3, 4, 5] and [10, 11, 12, 13].Each container will contain items weighing within 4 units of the minimum weight item.

# Input Format
# The first line contains an integer n, the number of orders to ship.
# The next line contains n space-separated integers, w[1], w[2], …, w[n], representing the orders in a weight array.

# Output Format
# Return the integer value of the number of containers Priyanka must contract to ship all of the toys.

# Sample Input
# 8
# 1 2 3 21 7 12 14 21

# Sample Output
# 4

def toys(weight):
    w = sorted(weight)
    res = 0
    limit = -1

    for element in w:
        if element > limit:
            limit = element + 4
            res += 1

    return res

n = int(input())
w = list(map(int, input().split()))
result = toys(w)
print(result)
