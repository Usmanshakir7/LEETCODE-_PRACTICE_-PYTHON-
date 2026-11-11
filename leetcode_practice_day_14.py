#  Student Information System
#  1. Create a class Student.
class student:
#  2. Add a class variable university = "DUET".
    university ="DUET"
#  3. Initialize name, roll_no, and marks as instance variables.
    def __init__(self,name,roll_no,marks):
        self.name= name
        self.roll_no = roll_no
        self.marks = marks
        pass
    def display(self):
        print("\nuni :",self.university)
        print("name :",self.name)
        print("roll-no :",self.roll_no)
        print("marks :",self.marks)
#  4. Create three student objects.
s1 = student("usman",122,11)
s2 = student("aziz",124,11)
s3 = student("asim",143,12)
#  5. Display each student's information and university.
s1.display()
s2.display()
s3.display()
#  Concepts: Class variables, instance variables, constructor.


# Student Counter
# 1. Create a Student class.
class student:
# 2. Add a class variable total_students = 0.
    total_students = 0
# 3. Increment total_students whenever a new object is created.
    def __init__(self):
        student.total_students+=1
        
# 4. Create a class method show_total_students().
    @classmethod
    def show_total_students(cls):
        print("total_students :",cls.total_students)
# 5. Create five student objects and display the total count.
student()
student()
student.show_total_students()