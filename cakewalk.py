# Marc loves cupcakes, but he also likes to stay fit. Each cupcake has a calorie count, and Marc can walk a distance to expend those calories. If Marc has eatenJcupcakes so far, after eating a cupcake withccalories he must walk atleast 2^j*c miles to maintain his weight.
# Example Calorie = [5, 10, 7]
# Given the individual calorie counts for each of the cupcakes, determine the minimum number of miles marc must walk to maintain his weight. Note that he can eat the cupcakes in any order.
# The first line contains an integer n, the number of cupcakes in calorie.The second line contains n space-separated integers, calorie[i].
# Returns minimum miles necessary to burn calories.

n = int(input().strip())
calories = list(map(int, input().strip().split(' ')))
calories.sort(reverse=True)
ans = 0
for x in range(0,n):
    ans = ans + (2**x)*calories[x]

print(ans)