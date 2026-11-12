# Exercise 1 — Person and Student

# Create a parent class Person and a child class Student.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name :",self.name) 
        print("age",self.age)   

class student(person):
    def study(self,course):
        print("course :",self.course)  
# Requirements:
# 1. Person should have name and age attributes.
# 2. Create a method display_info() in Person.
# 3. Create a child class Student that inherits from Person.
# 4. Add a study() method to Student.
# 5. Create a student object and call both methods.