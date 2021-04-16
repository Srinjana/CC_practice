# # Shovon is an HR in a renowned company and he is assigning people to work. Now he is assigning people work in a fashion where if he assigns somework a work of cost 2, the next person will be strictly getting a job with cost equal or more than 2. Given that Shovon’s company has infinite work and a number of digitoyees, how many distributions can be possible. The cost of jobs can go 0 to 9.
# N	    Integer	            The number of depts.
# arr[]	Integer array	The number of  digitoyees in each dept..
# Return: The function must return an INTEGER denoting the sum of answers for all distinct distributions

def answer(digit, depth, start):
    global val
    if depth > digit:
        return
    for i in range(start):
        if digit == depth:
            val += 1
        answer(digit, depth+1, start-i)


ans = 0 
val = 0
for _ in range (int(input())):
    val = 0
    depts = int(input())
    answer(depts, 1, 10)
    ans += val

print(ans)