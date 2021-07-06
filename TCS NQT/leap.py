# Explanation:

# To check whether a year is leap or not

# Step 1:

# We first divide the year by 4.
# If it is not divisible by 4 then it is not a leap year.
# If it is divisible by 4 leaving remainder 0
# Step 2:

# We divide the year by 100
# If it is not divisible by 100 then it is a leap year.
# If it is divisible by 100 leaving remainder 0
# Step 3:

# We divide the year by 400
# If it is not divisible by 400 then it is a leap year.
# If it is divisible by 400 leaving remainder 0
# Then it is a leap year

def leap(year):
    
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else: 
        return False

if __name__ == '__main__':
    
    year = int(input("Enter a year: "))
    res = leap(year)

    if res == True:
        print("IT IS A LEAP YEAR")
    else:
        print("IT IS NOT A LEAP YEAR")


