# Exercise 1 — Find Maximum and Minimum
# Easy
# Given:
# Find the largest number using a loop.
# Find the smallest number using a loop.
numbers = [12, 45, 7, 89, 23, 56, 3]
def max():
    maxi = numbers[0]
    for num in numbers:
       if  maxi<num:
           maxi = num
    return  maxi
print("maximum no:",max())     

numbers = [12, 45, 7, 89, 23, 56, 3]
def min():
    mini = numbers[0]
    for num in numbers:
       if  mini>num:
           mini = num
    return  mini
print("minimum no:",min()) 


# Exercise 2 — Reverse an Array
# Intermediate
# Given: