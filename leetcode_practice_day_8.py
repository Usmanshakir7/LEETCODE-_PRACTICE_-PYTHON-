#Exercise 1 — Student Records Analyzer
students = (
    ("Usman", 85),
    ("Ali", 72),
    ("Ahmed", 91),
    ("Sara", 85),
    ("Hina", 65)
)
# Tasks:
# 1. Print each student's name and marks using tuple unpacking.
# for student in students:
#     name, marks = student
#     print(name, marks)

# 2. Find the student with the highest marks.
# highest_marks=0
# for student in students:
#     name, marks = student
#     if marks>highest_marks:
#         highest_marks=marks

# print(highest_marks)
# 3. Calculate the average marks.
total_marks=0
for student in students:
    name, marks = student
    total_marks+=marks

total_students = len(students)

avg_marks= total_marks/total_students
print(total_marks)
print(total_students)
print(avg_marks)

# 4. Print the names of students who scored above 80.