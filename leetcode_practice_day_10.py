# Exercise 1 — Easy
# Square Numbers

# Given this list:

#numbers = [2, 4, 6, 8, 10]

# Tasks:
# 1. Create a list of squares using list comprehension.
#square =[num**2 for num in numbers]
# 2. Print the new list.
#print("square of each num is :",square)


# Filter Even Numbers
numbers = [11, 12, 13, 14, 15, 16, 17, 18]



# Tasks:
# 1. Extract only even numbers using list comprehension.
even_no = [num for num in numbers if num%2 == 0]
# 2. Extract only odd numbers.
odd_no = [num for num in numbers if num%2 != 0]
# 3. Print both lists.
print("even no are :",even_no)
print("odd no are :",odd_no)


# Exercise 3 — Intermediate
# Student Marks Analyzer

marks = [45, 78, 90, 32, 88, 67, 95]

# Tasks:
# 1. Create a list of marks greater than or equal to 80.
A_grade = [i for i in marks if i>=80]
print("a grade :",A_grade)
# 2. Create a list of marks below 50.
c_grade = [i for i in marks if i<=50]
print("c grade :",c_grade)
# 3. Add 5 bonus marks to every student using list comprehension.
grace_marks= [grace+5 for grace in marks]
print("5 geace marks",grace_marks)


# Exercise 4 — Intermediate
# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5, 6]

# Tasks:
# 1. Create a dictionary where keys are numbers and values are cubes.
dict ={num:num**3 for num in numbers}
print("cubes of numbers ",dict)
# 2. Create a dictionary containing only even numbers and their squares.
dict2 = {num :num**2 for num in numbers if num%2==0 }
print(dict2)