# Problem 1 — Easy
# Find the Middle Element
numbers = [5, 10, 15, 20, 25, 30, 35]
# Tasks:
# 1. Initialize low and high.
# 2. Calculate mid.
# 3. Print the middle index and its value.
def middle():
    low = numbers[0]
    high = numbers[-1]
    mid = (low + high) // 2
    index =numbers.index(mid)
    return mid,index
mid,index = middle()
# print("middle value is :",mid)
# print("middle value index is :",index)



# Problem 2 — Medium
# Implement Binary Search
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
target = 100
# Tasks:
# 1. Create binary_search(numbers, target).
# 2. Use a while loop.
# 3. Calculate mid in each iteration.
# 4. Update low or high based on comparisons.
# 5. Return the target's index, or -1 if absent.

def binary_search(numbers,target):
    low = 0
    high = len(numbers) - 1
   
    while low <= high:
        mid = (low + high) // 2
        if numbers[mid] < target:
            low = mid + 1
        elif numbers[mid] > target:
            high = mid - 1
        elif numbers[mid] == target:
            return mid
    return -1
print(binary_search(numbers,target))


# Problem 3: Find the First Occurrence Using Binary Search
# Medium Difficulty
# Topics: Binary Search, Arrays, Loops, Time Complexity
# Problem Statement
# You are given a sorted list containing duplicate numbers. Your task is to find the index of the first occurrence of a target using binary search.
numbers = [10, 20, 20, 20, 30, 40, 50]
target = 20        

def First_occurrence(numbers,target):
    low = 0
    high = len(numbers) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] < target:
            low = mid + 1

        elif numbers[mid] > target:
            high = mid - 1

        else:
            result = mid
            high = 

    return result


numbers = [10, 20, 20, 20, 30, 40, 50]
target = 20

print(first_occurrence(numbers, target))