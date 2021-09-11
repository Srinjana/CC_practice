# Given an array arr  which represents the marks of n  students. The passing grade is 50 and maximum marks that a student can score is 100, the task is to maximize the student that are passing the exam by giving bonus marks to the students.
# Note that if a student is given bonus marks then all other students will also be given the same amount of bonus marks without any student’s marks exceeding 100  . Print the total students that can pass the exam in the end.

# Examples:

# Input: arr[] = {0, 21, 83, 45, 64}
# Output: 3
# We can only add maximum of 17 bonus marks to the marks of all the students. So, the final array becomes {17, 38, 100, 62, 81}

# Only 3 students will pass the exam.

# Input: arr[] = {99, 50, 46, 47, 48, 49, 98}
# Output: 4


def check(n, marks):

    x = max(marks)
    # maximum bonus marks that can be given
    bonus = 100-x
    c = 0

    for i in range(n):
        # counting the number of students that can pass
        if(marks[i] + bonus >= 50):
            c += 1

    return c


# Driver code

marks = list(map(int, input().split()))
n = len(marks)
print(check(n, marks))
