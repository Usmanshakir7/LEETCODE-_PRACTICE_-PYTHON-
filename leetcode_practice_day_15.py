# Student Marks Protection

# Create a class named Student.
class students:
# 1. Create a constructor that accepts name and marks.
    def __init__(self,name,marks):
# 2. Store name as a public attribute.
        self.name=name
# 3. Store marks as a private attribute (__marks).
        self.__marks = marks
# 4. Create a getter method get_marks() that returns the marks.
    def  get_marks(self):
        return self.__marks
# 5. Create a setter method set_marks(new_marks) that accepts marks only between 0 and 100.
    def set_marks(self, marks):
     if 0 <= marks <= 100:
        self.__marks = marks
     else:
        print("Invalid marks")
# 6. Create one student object and test valid and invalid marks.

s1 = students("usman",33)
s2 = students("aziz",102)

s1.get_marks()