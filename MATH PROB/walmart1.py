# soln to question 1

N = int(input())
q = int(input())
# l = []
# r = []
lst = []
for _ in range(q):
    lst.append(list(map(int, input().split())))

for i in range(len(lst)):
    print(lst[i])
print(*lst)