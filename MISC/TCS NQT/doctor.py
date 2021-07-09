# A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a code to calculate earnings in a day for which one array/List of values representing age of patients visited on that day is passed as input.

# Note:

# Age should not be zero or less than zero or above 120
# Doctor consults a maximum of 20 patients a day
# Enter age value(press Enter without a value to stop):
# Example 1:

# Input
# 20
# 30
# 40
# 50
# 2
# 3
# 14


# Output
# Total Income 2000 INR

age = []

while True:

    m = input("->")

    if not m:

        break

    age.append(int(m))


print(age)

fee = 0
for i in age:
    
    # print("12")
    if (i <= 17):
        fee += 200
    elif (i > 17 and i <= 40):
        fee += 400
    elif(i > 40 and i <= 120 ):
        fee += 300
    else:
        print ("Error")

print(fee)
