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

if result == -1:
    print("Target is not found")
else:
    print("Target found at index:", result)
