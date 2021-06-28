# Given a value V, if we want to make a change for V Rs, and we have an infinite supply of each of the denominations in Indian currency, i.e., we have an infinite supply of {1, 2, 5, 10, 20, 50, 100, 500, 1000} valued coins/notes, what is the minimum number of coins and / or notes needed to make the change?

# Algorithm:

# Sort the array of coins in decreasing order.
# Initialize result as empty.
# Find the largest denomination that is smaller than current amount.
# Add found denomination to result. Subtract value of found denomination from amount.
# If amount becomes 0, then print result.
# Else repeat steps 3 and 4 for new value of V.

def findcoins(v):
    deno = [1,2,5,10,20,50,100,500,1000]
    res = []
    count = 0

    i = len(deno) - 1

    while(i >= 0):
        while(v  >= deno[i]):
            v -= deno[i]
            res.append(deno[i])
        
        i -= 1
    
    for i in range(len(res)):
        count += 1
        print(res[i], end = " ")
        
    print("")
    print("Number of coins needed:", count)


if __name__ == '__main__':
    n = int(input())
    print("Following is minimal number",
          "of change for", n, ": ", end="")
    findcoins(n)
