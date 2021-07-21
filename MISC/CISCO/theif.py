# A thief trying to escape from a jail has to cross N walls whose heightd are given in arr[] each with varying heights. He climbs X feet every time. But, due to the slippery nature of those walls, every times he slips back by Y feet.  Now the task is to calculate the total number of jumps required to cross all walls and escape from the jail.

# Example 1:

# Input: X = 10, Y = 1, N = 1
# arr = {5}
# Output: 1
# Explaination: He jumps 10 feet and cross 
# the walls.

def theifwalled(x, y,arr,n):
    jumps = 0
    # one jump
    for i in range(n):
        if (arr[i] <= x):
            jumps += 1
            continue
    
    # multiple jumps
        h = arr[i]
        while (h > x):
            jumps += 1
            h = h - (x - y)
        jumps += 1
    return jumps
 

#  Driver Code  
x = int(input("Wall height : "))
y = int(input("Slips: "))
n = int(input("no of walls: "))

arr = []
for i in range (n):
    val = int(input())
    arr.append(val)

print (arr)

jumps = theifwalled(x,y,arr,n)
print(jumps)
