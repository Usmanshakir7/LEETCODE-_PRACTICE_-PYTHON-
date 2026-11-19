# Bubble Sort in Ascending Order
numbers = [64, 34, 25, 12, 22, 11, 90]
# Tasks:
# 1. Implement Bubble Sort using nested for loops.
# 2. Sort the numbers in ascending order.
# 3. Don't use sort() or sorted().
# 4. Print the sorted list.

def bubble_sort(numbers):

    for i in range(len(numbers) - 1):
     for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers
print(bubble_sort(numbers))
