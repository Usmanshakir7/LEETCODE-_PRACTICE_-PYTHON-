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
print("middle value is :",mid)
print("middle value index is :",index)



