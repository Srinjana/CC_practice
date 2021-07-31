# Dr. Vishnu is opening a new world class hospital in a small town designed to be the first preference of the patients in the city. Hospital has N rooms of two types – with TV and without TV, with daily rates of R1 and R2 respectively.

# However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead it follows a pattern. The number of patients on any given day of the year is given by the following formula –

# (6-M)^2 + |D-15 | ,
# where M is the number of month(1 for jan, 2 for feb …12 for dec) and D is the date(1, 2…31).

# All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and the values of N, R1 and R2 you need to identify the number of TVs the hospital should buy so that it meets the revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year.


# Constraints

# Hospital opens on 1st Jan in an ordinary year

# 5 <= Number of rooms <= 100
# 500 <= Room Rates <= 5000
# 0 <= Target revenue < 90000000
# Input Format

# First line provides an integer N that denotes the number of rooms in the hospital
# Second line provides two space-delimited integers that denote the rates of rooms with TV(R1) and without TV(R2) respectively
# Third line provides the revenue target
# Output

# Minimum number of TVs the hospital needs to buy to meet its revenue target. If it cannot achieve its target, print the total number of rooms in the hospital.
# Test Case

# Example-1:

# Input

# 20

# 1500 1000

# 7000000

# Output

# 14

# Explanation

# Using the formula, the number of patients on 1st Jan will be 39, on 2nd Jan will be 38 and so on. Considering there are only twenty rooms and rates of both type of rooms are 1500 and 1000 respectively, we will need 14 TV sets to get revenue of 7119500. With 13 TV sets Total revenue will be less than 7000000

# Example-2:

# Input

# 10

# 1000 1500

# 10000000

# Output

# 10

# Explanation

# In the above example, the target will not be achieved, even by equipping all the rooms with TV. Hence, the answer is 10 i.e. total number of rooms in the hospital.


n = int(input("No. of rooms in hospital: "))
with_ac , without_ac = map(int, input().split())
Rev = int(input("Enter Target revenue: "))

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

money, total = 0, 0

per_month, total_year = [], []

for i in range(len(month_days)):
   for j in range(1, month_days[i]+1):

       per_month.append((6-(i+1))*(6-(i+1))+abs(j-15))

   total_year.append(per_month)
   per_month = []

   for i in range(n+1):
    for j in total_year:
       for k in j:

           if(k >= n):
               t = n-i
               money = money + (i * with_ac+t*without_ac)

           else:
               h = n-i
               t = k-h

               if(t <= 0):
                   money = money + (k*without_ac)

               else:
                   money = money + (t*with_ac+h*without_ac)

       total = total + money
       money = 0

   if(total >= Rev):
       print(i)
       break

   else:
       total = 0

else:
   print(n)
