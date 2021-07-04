# We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and exterior wall painting cost is Rs.12 per sq.ft.

# Take input as
# 1. Number of Interior walls
# 2. Number of Exterior walls
# 3. Surface Area of each Interior 4. Wall in units of square feet
# Surface Area of each Exterior Wall in units of square feet

# If a user enters zero  as the number of walls then skip Surface area values as User may don’t  want to paint that wall.

# Calculate and display the total cost of painting the property
# Example 1:

# 6
# 3
# 12.3
# 15.2
# 12.3
# 15.2
# 12.3
# 15.2
# 10.10
# 10.10
# 10.00
# Total estimated Cost : 1847.4 INR

int_walls = int(input())
ext_walls = int(input())

if int_walls:
    iwalls = []
    for i in range(int_walls):
        iwalls.append(float(input()))

if ext_walls:
    ewalls = []
    for i in range (ext_walls):
        ewalls.append(float(input()))

if int_walls < 0 or ext_walls < 0:
    print("Invalid input")
    exit()

if ext_walls and int_walls:
    print("Total estimated Cost : ", (sum(iwalls) * 18 + sum(ewalls) * 12), "INR")
else:
    if ext_walls:
        print("Total estimated Cost : ", sum(ewalls) * 12, "INR")
    elif int_walls:
        print("Total estimated Cost : ", sum(iwalls) * 18, "INR")
    else:
        print("Total estimated Cost : 0.0 INR")
