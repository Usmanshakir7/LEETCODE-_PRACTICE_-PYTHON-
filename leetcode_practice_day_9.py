# Exercise 1 — Student Grade Calculator
# Create a function that accepts student marks.

# Tasks:
# 1. Create calculate_average() that accepts three subject marks and returns the average.

# def calculate_avg(s1,s2,s3):
#     return (s1+s2+s3)/calculate_avg.__code__.co_argcount
   
# 2. Create calculate_grade() that accepts the average.
# 3. Return a grade according to these rules:
#    - 90 or above → A
#    - 80 or above → B
#    - 70 or above → C
#    - 60 or above → D
#    - Below 60 → F
# def calculate_grade(avg):
#     if avg>=90:
#         return "A"
#     elif avg>=80:
#         return "B"
#     elif avg>=70:
#         return "C"
#     elif avg>=60:
#         return "D"
#     else:
#         return "F"

#4. Use one function inside another.

# def calculate_result(s1,s2,s3):
#     avg =calculate_avg(s1,s2,s3)
#     grade = calculate_grade(avg)

#     return grade,avg 

# 5. Print the final average and grade.
# grade,avg = calculate_result(20,30,50)
# print("avg :",avg)
# print("grade :",grade)



# Exercise 2 — Number Analyzer
# Create a number analyzer using functions.

# Tasks:
# 1. Create check_even_odd(num) that returns "Even" or "Odd".
def check_even_odd(num):
    if num%2 == 0:
      return "Even"
    else:
      return "Odd"
# 2. Create check_positive_negative(num) that returns "Positive", "Negative", or "Zero".
def check_positive_negative(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"
    else:
        return "zero"
# 3. Create analyze_number(num) that calls both functions.
# 4. Use keyword arguments in at least one function call.
def  analyze_number(num):
    no_type = check_even_odd(num)
    no_state = check_positive_negative(num=num)
    return  no_type,no_state
no_type,no_state = analyze_number(-0)
print("the type of no is :",no_type)
print("the state of no is :",no_state)
