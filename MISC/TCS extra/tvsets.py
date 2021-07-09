# Dr. Vishnu is opening a new world-class hospital in a small town designed to be the first preference of the patients in the city. Hospital has N rooms of two types with TV and without TV, with daily rates of R1 and R2 respectively. However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead, it follows a pattern. The number of patients on any given day of the year is given by the following formula:

# Patients per day = (6 – M)2 + |D – 15|
# where,
# M: the number of month starting from 1 to 12
# D: the date from 1 to 31

# All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and the values of N, R1, and R2 you need to identify the number of TVs the hospital should buy so that it meets the revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year.

# Examples:

# Input: N = 20, R1 = 1500, R2 = 1000, target = 7000000
# Output: 14
# Explanation:
# Using the formula:
# The number of patients on 1st Jan will be 39, on 2nd Jan will be 38 and so on.
# Considering there are only twenty rooms and rates of both type of rooms are 1500 and 1000 respectively.
# Therefore, 14 TV sets are needed to get the revenue of 7119500 with 13 TV sets.
# The total revenue will be less than 7000000.

no_of_rooms = int(input())

with_ac, without_ac = map(int, input().split(' '))

estimation = int(input())

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

money, total = 0, 0

per_month, total_year = [], []

for i in range(len(month_days)):

   for j in range(1, month_days[i]+1):

       per_month.append((6-(i+1))*(6-(i+1))+abs(j-15))

   total_year.append(per_month)

   per_month = []

for i in range(no_of_rooms+1):

   for j in total_year:

       for k in j:

           if(k >= no_of_rooms):

               t = no_of_rooms-i

               money = money+(i*with_ac+t*without_ac)

           else:

               h = no_of_rooms-i

               t = k-h

               if(t <= 0):

                   money = money+(k*without_ac)

               else:

                   money = money+(t*with_ac+h*without_ac)

       total = total+money

       money = 0

   if(total >= estimation):

       print(i)

       break

   else:

       total = 0

else:

   print(no_of_rooms)

