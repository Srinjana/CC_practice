# Abhijeet is one of those students who tries to get his own money by part time jobs in various places to fill up the expenses for buying books. He is not placed in one place, so what he does, he tries to allocate how much the book he needs will cost, and then work to earn that much money only. He works and then buys the book respectively. Sometimes he gets more money than he needs so the money is saved for the next book. Sometimes he doesn’t. In that time, if he has stored money from previous books, he can afford it, otherwise he needs money from his parents.
# Now His parents go to work and he can’t contact them amid a day. You are his friend, and you have to find how much money minimum he can borrow from his parents so that he can buy all the books.He can Buy the book in any order.
# N	        -Integer 	    How many Books he has to buy that day.
# EarnArray[]	-Integer array	Array of his earnings for the ith book
# CostArray[]	-Integer array	Array of the actual cost of the ith book.

n = int(input())
EarnArr = [0]*n
CostArr = [0]*n

for i in range (n):
    EarnArr[i] = int(input())

for i in range (n):
    CostArr[i] = int(input())

for i in range (n):
    EarnArr[i] = CostArr[i] - EarnArr[i]

EarnArr.sort()
sums = 0
res = 0
for i in range(n):
    sums = sums + EarnArr[i]
    if (sums < 0):
        res = res + abs(sums)
        sums = 0

print(res)