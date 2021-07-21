# You are given a number, at a time either you can increase a number by 1 or decrease by 1 it is considered as one move find the minimum number of moves required to convert a given into a lucky number. A number is called lucky if all the digits in it are even

# A function that checks if all digits are even
def check(n):
	while n > 0:
		r = n%10
		n /= 10
		if r % 2 != 0:
			return False
	return True

n = int(input())
s = str(n)
low, high = 10 * (len(s) - 1), 10 * len(s) - 1
i, j = n, n

# Checking for both cases where the digits are reduced and increased by 1

while (i >= low):
	if check(i):
		break
	i -= 1

while (j <= high):
	if check(j):
		break
	j += 1

res = min(n -i, j-n)
print(res)



