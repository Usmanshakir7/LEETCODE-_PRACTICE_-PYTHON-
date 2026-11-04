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
print("even no are ",even_no)
print("odd no are ",odd_no)