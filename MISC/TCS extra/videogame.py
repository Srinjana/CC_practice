# Purchase Video game’s
# You wish to buy video games from the famous online video game store Mist.
# Usually, all games are sold at the same price,p dollars. However, they are planning to have the seasonal Halloween Sale next month in which you can buy games at a cheaper price. Specifically, the first game you buy during the sale will be sold at p dollars, but every subsequent game you buy will be sold at exactly d dollars less than the cost of the previous one you bought. This will continue until the cost becomes less than or equal to m dollars, after which every game you buy will cost m dollars each.

# Input Format
# The first and only line of input contains four space-separated integers p, d, m and s.
# Output Format
# Print a single line containing a single integer denoting the maximum number of games you can buy.
# Sample Input
# 20 3 6 80
# Sample Output
# 6



def howManyGames(p, d, m, s):
    a = []
    a.append(p)
    for i in range(s):
        p = p - d
        if p > m:
            a.append(p)
        else:
            a.append(m)
    sum = 0
    c = 0
    for i in range(len(a)):
        if sum <= s:
            sum = sum + a[i]
            c+=1
    return c-1

pdms = input().split()
p = int(pdms[0])
d = int(pdms[1])
m = int(pdms[2])
s = int(pdms[3])
answer = howManyGames(p, d, m, s)
print(answer)