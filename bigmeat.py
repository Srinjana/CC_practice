# Bhojon is a restaurant company and has started a new wing in a city. They have every type of cook except the meatball artist. They had fired their last cook because the sale of meatballs in their restaurant is really great, and they can’t afford to make meatballs again and again every time their stock gets empty. They have arranged a hiring program, where you can apply with their meatball.
# They will add the meatball in their seekh(a queue) and everytime they cut the meatball they take it and cut it on the day’s quantity and then re-add the meatball in the seekh. You are the hiring manager there and you are going to say who is gonna be hired.
# Day’s quantity means, on that very day the company sells only that kg of meatballs to every packet.
# If someone has less than a day’s quantity, it will be counted as a sell.
# N-Integer	How many people are participating in the hiring process.
# D-Integer	Day’s quantity, how many grams of meatball is being sold    to every packet.
# Array[]-Integer array	Array of integers, the weight of meatballs everyone came with.
# Output Format: The 1 based index of the man whose meatball is served at the last. (Last index that remains unaltered)
# Author @Srinjana

people = int(input())
m = 0
maxposi = 0
ballwt = [0]*people
soldball = int(input())

for i in range(people):
    ballwt[i] = int(input())

# this function finds out which value stays the greatest after iterations
for i in range(people):
    ballwt[i] = (ballwt[i]-1)//soldball
    #  print (ballwt[i])

for i in range(people):
    if ballwt[i] >= m:
        m = ballwt[i]
        maxposi = i

print(maxposi + 1)
