# There is one meeting room in a firm. There are N meetings in the form of(S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time? Also note start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

def printMaxActivities(S, F):
    n = len(F)
    counter = 0
    print ("The following activities are selected")

    # The first activity is always selected
    i = 0
    print (i)

    # Consider rest of the activities
    for j in range(n):

        # If this activity has start time greater than
        # or equal to the finish time of previously
        # selected activity, then select it
        if S[j] >= F[i]:
            print (j)
            counter += 1
            i = j
    print("Total number of meetings = ", counter+1)


# Driver program to test above function
start_time = [1, 3, 0, 5, 8, 5]
fin_time = [2, 4, 6, 7, 9, 9]

start = [10, 12, 20]
fin = [20, 25, 30]

printMaxActivities(start_time, fin_time)
printMaxActivities(start, fin)
