# Exercise 1 — Person and Student

# Create a parent class Person and a child class Student.
# Requirements:
# 1. Person should have name and age attributes.
# 2. Create a method display_info() in Person.
# 3. Create a child class Student that inherits from Person.
# 4. Add a study() method to Student.
# 5. Create a student object and call both methods.
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display_info(self):
        print("name :",self.name) 
        print("age",self.age)   

class student(person):
    def study(self,course):
        print("course :",course)  

s1 = student("usman",22)
s1.display_info()
s1.study("data")


# Exercise 3 — Employee and Manager Using super()


# Create a parent class Employee and a child class Manager.
class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print("name:",self.name)
        print("salary:",self.salary)   

class manager(employee):
    def __inti__(self,name,salary,department):
        super().__init__(name,salary)   
        self.department= department 

    def manager_info(self):
        print("name:",self.name)
        print("salary:",self.salary) 
        print("depatment: ",self.department) 


m1 =manager("usman",22000,"datascience")     
m1.manager_info()       
# Requirements:
# 1. Employee should have name and salary.
# 2. Create a method display_info() in Employee.
# 3. Manager should inherit from Employee.
# 4. Add a new attribute department to Manager.
# 5. Use super().__init__() to initialize the inherited attributes.
# 6. Create a method manager_info() that displays all three attributes.