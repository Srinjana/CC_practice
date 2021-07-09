# A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain But based on weight measured by sensors, it decides time and water level which can be changed by menus given on the machine control area.

# For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive number below that.
# For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.
# For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams.
# Assume the capacity of machine is maximum 7000 grams
# Where approximately weight is zero, time estimate is 0 minutes.

# Write a function which takes a numeric weight in the range [0, 7000] as input and produces estimated time as output is : “OVERLOADED”, and for all other inputs, the output statement is
# “INVALID INPUT”.

# Input should be in the form of integer value –
# Output must have the following format –
# Time Estimated: Minutes


weight = int(input())

if (weight in range(1, 2001)):
    print("Estimated time is 25 mins")
elif (weight == 0):
    print("Estimated time is 0 mins.")
elif(weight in range(2001, 4001)):
    print("Estimated time is 35 mins")
elif (weight in range(4001, 7001)):
    print("Estimated time is 45 mins.")
else:
    print("INVALID INPUT")