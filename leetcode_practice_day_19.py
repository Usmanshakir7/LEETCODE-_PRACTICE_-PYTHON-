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

print("largest no is", largest())

def smallest ():
    smallest_no = numbers[0]
    for i in numbers:
        if i<smallest_no:
            smallest_no=i
    return smallest_no


print("smallest no is",smallest())