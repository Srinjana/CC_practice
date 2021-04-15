# In an airport, the Airport  authority decides to charge some minimum amount to the passengers who are carrying luggage with them. They set a threshold weight value, say T, if the luggage exceeds the weight threshold you should pay double the base amount. If it is less than or equal to threshold then you have to pay $1.
# The function must return an INTEGER denoting the required amount to be paid.
# The first line contains an integer, N, denoting the number of luggages.
# Each line i of the N subsequent lines(where 0 <= i < n) contains an integer describing weight of ith luggage.
# The next line contains an integer, T, denoting the threshold weight of the boundary wall.
# Author @srinjana

n = int(input())
weights = []

def weightMachine(n, weights, Threshold):
    amount = 0
    for i in weights:
        amount += 1
        if (i> Threshold):
            amount += 1
    return amount

for i in range (n):
    weights.append(int(input()))

t = int(input())
print(weightMachine(n, weights, t))
