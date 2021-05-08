# for a given number from a list of numbers find the factors and add the factors . If the sum of factors is present in the original list, sort the factors in acsending order 
# and print them. If sum not in the original list, print -1.
# Author @Srinjana

def findFactorSum(n):
    factor = [1]
    for i in range (2 ,n+1):
        if i%n ==0:
            factor.append(i)
        return sum(factor)

inplist = list(map(int, input().strip().split(",")))
flag = 0

for i in inplist:
    if findFactorSum(i) in inplist:
        flag = 1
        print(i)
if flag==0:
    print(-1)
