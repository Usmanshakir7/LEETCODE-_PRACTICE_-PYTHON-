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