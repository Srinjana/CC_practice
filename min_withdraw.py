# here is a unique ATM in Wonderland. Imagine this ATM as an array of numbers. You can withdraw cash only from either ends of the array. Sarah wants to withdraw X amount of cash from the ATM. What is the minimum number of withdrawals Sarah would need to accumulate X amount of cash. If it is not possible for Sarah to withdraw X amount, return -1. 
# Input Format 
# The first line contains an integer, N, denoting the number of elements in ATM. 
# Each line i of the N subsequent lines (where 0 <= i < N) contains an integer describing the cash in the ATM. 
# The next line contains an integer, X, denoting the total amount to withdraw. 
# Constraints 
# 1 <= N <= 10^5 
# 1 <= ATM [i] <= 10^5 
# 1 <= X <= 10^5 \
# Author @Srinjana

N = int(input())
Arr = []

for i in range(N):
    Arr.append(int(input()))

def answer(strt, end, amt):
    if amt == 0:
        return 0
    if strt>end or amt<0:
        return (10**9)
    else:
        return min(1 + answer(strt+1, end, amt-Arr[strt]), 1 + answer(strt, end-1, amt-Arr[end]))


amt = int(input())
amt2 = answer(0, N-1, amt)
if amt2 >= (10**9):
    print(-1)
else:
    print("Minimum Number of Withdrawls possible are: ")
    print(amt2)