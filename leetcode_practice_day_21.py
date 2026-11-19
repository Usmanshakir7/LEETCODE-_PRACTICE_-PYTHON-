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

# Time complexity: O(n²) in the average and worst cases.


# Selection Sort in Descending Order
# Tasks:
# 1. Implement Selection Sort using nested loops.
# 2. Find the largest element in the unsorted portion.
# 3. Place it at the current position.
# 4. Sort in descending order without built-in sorting functions.

def selection_sort(numbers):

    for i in range(len(numbers) - 1):
        max_index = i

        for j in range(i + 1,len(numbers)):
            if numbers[j] > numbers[max_index]:
                max_index = j

        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

    return numbers


numbers = [29, 10, 14, 37, 13]

print(selection_sort(numbers))