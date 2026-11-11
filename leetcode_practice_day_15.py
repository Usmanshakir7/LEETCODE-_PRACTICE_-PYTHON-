# Student Marks Protection

# Create a class named Student.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = 0
        self.set_marks(marks)

    # Getter method
    def get_marks(self):
        return self.__marks

    # Setter method
    def set_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.__marks = new_marks
            print("Marks updated successfully")
        else:
            print("Invalid marks!")


# Create student objects
s1 = Student("Usman", 80)

print("Student:", s1.name)
print("Initial Marks:", s1.get_marks())

# Valid update
s1.set_marks(95)
print("Updated Marks:", s1.get_marks())

# Invalid update
s1.set_marks(150)
print("Final Marks:", s1.get_marks())
