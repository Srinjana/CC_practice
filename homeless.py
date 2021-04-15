# There are N Homeless people in the community and N houses in the community. It will be given in the array(people), height of the person and in the array house capacity of the house is given.
# Government decided to give homes for people on the basis of following conditions:
# Priority is given for the people from left to right of the array
# Each person is allotted to a house if and only if the capacity of house is greater than or equal to persons height
# Nearby empty Houses are alloted to the person(starting from extreme left)
# You need to find the number of homeless people who have not allotted any home if the government follows the above conditions.So that government will have an idea for how many people they need to allot home for next time.
# The first line contains an integer, N, denoting the number of  people and number of houses.
# Each line i of the N subsequent lines(where 0 <= i <= N) contains an integer describing peoples.
# Each line i of the N subsequent lines(where 0 <= i <= N) contains an integer describing houses.

N = int(input())
people = []
houses = []
for i in range(N):
    people.append(int(input()))

for i in range (N):
    houses.append(int(input()))

count = 0

for i in range (N):
    for j in range (N):
            if(people[i]<houses[j]):
                count += 1
                houses[j] = -1
                break
print(N - count)