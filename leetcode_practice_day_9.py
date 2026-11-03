# Exercise 1 — Student Grade Calculator
# Create a function that accepts student marks.

# Tasks:
# 1. Create calculate_average() that accepts three subject marks and returns the average.
def calculate_avg(s1,s2,s3):
    avg = (s1+s2+s3)/calculate_avg.__code__.co_argcount
    return avg

print(calculate_avg(10,10,10))

# 2. Create calculate_grade() that accepts the average.
# 3. Return a grade according to these rules:
#    - 90 or above → A
#    - 80 or above → B
#    - 70 or above → C
#    - 60 or above → D
#    - Below 60 → F
# 4. Use one function inside another.
# 5. Print the final average and grade.