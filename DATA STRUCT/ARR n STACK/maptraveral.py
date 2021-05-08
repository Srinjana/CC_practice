# Mark is playing a game on a 2D map. The 2D map is a rectangle of size n*m, where n is the number of rows, and m is the number of columns. The cell(1, 1) is located at the top left corner of the map, and the cell(n, m) is located at the bottom right corner.
# In one step, Mark can move from any cell to any of the adjacent cells(UP, DOWN, RIGHT, or LEFT). There’s also a blocked cell(x, y) which Mark can’t pass on. Mark can’t go off the map.
# The goal of the game is to reach the cell(n, m). Mark is initially at cell(1, 1) and he wants to achieve the goal of the game in the minimum number of steps. Now he’s wondering how many paths he can take such that the number of steps is minimized and he gets to cell(n, m). Can you help him find this number?
# It is guaranteed that both cells(1, 1) and (n, m) are NOT blocked.
# Author @Srinjana
import math

n = int(input()) - 1
m = int(input()) - 1
x = int(input()) - 1
y = int(input()) - 1

var1 = n-x
var2 = m-y

ans = math.factorial(n+m)
ans = ans//(math.factorial(n))
ans = ans//(math.factorial(m))

ans1 = math.factorial(x+y)
ans1 = ans1//(math.factorial(x))
ans1 = ans1//(math.factorial(y))

ans2 = math.factorial(var1+var2)
ans2 = ans1//(math.factorial(var1))
ans2 = ans1//(math.factorial(var2))

result = ans-(ans1*ans2)
print(result)