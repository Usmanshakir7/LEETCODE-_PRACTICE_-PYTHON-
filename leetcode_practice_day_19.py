# Exercise 1 — Easy
# Find the Largest and Smallest Numbers

numbers = [45, 12, 89, 23, 67, 5, 91]
# Tasks:
# 1. Find the largest number without using max().
# 2. Find the smallest number without using min().
# 3. Print both results.
def largest():
    largest_no=numbers[0]
    for i in numbers:
        if i>largest_no:
            largest_no=i
            
    return largest_no

# print("largest no is", largest())

def smallest ():
    smallest_no = numbers[0]
    for i in numbers:
        if i<smallest_no:
            smallest_no=i
    return smallest_no


# print("smallest no is",smallest())


# Problem 2 — Linear Search (Medium)
numbers = [10, 25, 30, 45, 60, 75, 90]
target = 60
# Tasks:
def linear_search(numbers, target):

    for i in range(len(numbers)):
        if target == numbers[i]:
            return i
    return -1

result = linear_search(numbers, target)

# if result == -1:
#     print("Target is not found")
# else:
#     print("Target found at index:", result)
#time complexity O(n).
# 


# Problem 3 — Count Occurrences Using Linear Search
# Medium Difficulty
# Topics: Arrays, Linear Search, Loops, Functions
# Problem Statement
# Given a list of numbers and a target value, find how many times the target appears and at which indices.
numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20
# Your Tasks
# 1. Create a function count_occurrences(numbers, target).
# 2. Use a for loop to traverse the list.
# 3. Count how many times the target appears.
# 4. Store all matching indices in a separate list.
# 5. Print the matching indices and return the total count.
# 6. If the target doesn't exist, return 0.

def count_occurrences(numbers, target):
    count = 0
    index = []
    for i in range(len(numbers)):
      if target == numbers[i]:
          index.append(i)
          count+=1
    return count,index



numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20

result = count_occurrences(numbers, target)
count, indices = count_occurrences(numbers, target)

print("target",target)
print("Total occurrences:", count)
print("Found at indices:", indices) 

