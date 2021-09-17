# Problem statement

# You have to implement the following function: int CircularPrimesSum(int rangeMin, int rangeMax)

# A number is said to be a circular prime if all the rotations of the number are Prime. For the number 142, rotation set is defined as (142, 214, 421). Given a range, from 'rangeMin' to 'rangeMax', both inclusive, you have to return sum of all Circular prime numbers. Note: If there are no circular prime numbers within the given range then return -1

# Assumptions:

# • rangeMin > 1, rangeMax > 1 
# • rangeMin <= rangeMax

import itertools
import math

min = int(input())  # Lower Limit
max = int(input())  # Upper Limit
t = []  # empty list to store numbers


def prime(max):  # function to find prime no in the given Range

	for x in range(2, int(math.sqrt(max)) + 1):
		if (max % x) == 0:
			break
	else:
		return max


def cirpirme(max):  # Function to classify if the prime no is circular prime or not
	no = str(max)
	for x in range(0, len(no)):
		r = no[x:len(no)] + no[0:x]
		if not prime(int(r)):
			return False
	return True


for x in range(min, max+1):  # To increase the efficiency of the code
	if prime(x):
		if cirpirme(x):
			t.append(x)
print(sum(t))
