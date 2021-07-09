# In one pass, Train A can start from the source station at time T[0], halt at each station for h unit of time until it reaches the last station at time T[N – 1], where N is the positive integer representing a total number of stations.

# Given, Train A’s timings at each unit of time as T[] = {10.00, 10.04, 10.09, 10.15, 10.19, 10.22}.

# Now, suppose Railway Admin wants to add more trains to increase the frequency. So, to launch other Train B, for the same stations as of Train A’s. Provided the Train B starts at time t, they would like to know the timings for Train B. The program should return a String array S (timestamp( in float) for Train B at each station from first to the last station like train A).  

# Note:


# The time is represented in 24-Hour.
# Start Hour should be in the range[0, 23].
# Start Minute should be in the range[0, 59].
# Enter start time(24 Hrs)
# Examples:

# Input: t = 11.00
# Output: 11.00 11.04 11.09 11.15 11.19 11.22
# Explanation: Start time for train B is 11.00 and also the time difference between the stations for train B is same as for train A.

# Input: t = -26.15
# Output: Invalid Input
# Explanation: No such time as -26.15 exists. Hence, print “Invalid Input”.

def findTime(train_A, n, t):
    train_B = [0.0]*n
    train_B[0] == t
    for i in range(1,n):
        train_B[i] = train_A[i]- train_A[i - 1]
    
    it = int(t)
    if (t >= 0.0 and t <= 24.0 and (t - it) <= 60.0):
        for i in range(6):
            x = t + train_B[i]
            ix = int(x)

            if (x - ix >= 0.60):
                x = x + 0.40
            if (x > 24.00):
                x = x - 24.0
            
            print ("{:.2f}".format(x))
            t = x
    
    else:
        print("INVALID input")


if __name__ == '__main__':
    train_A = [10.00, 10.04, 10.09, 10.15, 10.19, 10.22]

    n = len(train_A)
    # print(n)

    t = float(input("Train B time: "))

    findTime(train_A, n, t)
