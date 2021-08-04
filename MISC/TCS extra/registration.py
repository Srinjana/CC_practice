# // ABC University has N number of colleges with students. They want to automate some processes, like:

# // Registration of College
# // Registration of students(storing the data),
# // Count of students(fetching the data),
# // Search student name by their roll number,
# // Year-wise count of students
# // Write the code for the same.

# While registering the College you have to store the following details of the college:
# College Name, List of Students studying in that college
# While registering the Student you have to store the following details of the student:
# Student Name, Roll, Session of Admission(Year), Gender
# (Note: You can use your OOPS programming skills to code for the above problem)

class Student():
    def __init__(self, roll, name, year, gender):
        self.roll = roll
        self.name = name
        self.year = year
        self.gender = gender


class College():
    def __init__(self, name, student_list):
        self.name = name
        self.student_list = student_list
    
    def addStudent(self, name, student_list):
        self.student_list.append(Student(roll, name, year, gender))
    
    def getStudentCount(self):
        return len(self.student_list)
    
    def findStudent(self, roll):
        for i in self.student_list:
            if (i.roll == roll):
                return i.name
        return -1
    
    def countYearwiseStudent(self, year):
        count = 0
        for i in self.student_list:
            if (i.year == year):
                count += 1
        return count


# Driver code

students = []
c = College('XYZ', students)
n = int(input("ENTER THE NUMBER OF STUDENTS: "))
for i in range(n):
    roll = int(input("Enter Roll: "))
    name = input("Enter Name: ")
    year = int(input("Enter Academic Year: "))
    gender = input("Enter Gender: ")
    c.addStudent(id, name,  year, gender)

print("FUNCTIONS IN THE DATABASE")
print (" Enter your choice /n 1. get number of students: /n 2. Find a student /n Count students in a year")
choice = int(input())
if choice == 1:
    print(c.getStudentCount())
elif choice == 2:
    roll = int(input("Enter student Roll: "))
    print(c.findStudent(roll))
elif choice == 3:
    year = int(input("Enter an academic year: "))
    print(c.countYearwiseStudents(year))
else:
    print("ERROR")


