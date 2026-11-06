# # Complete Guide: Error Handling in Python

# Today we're covering Day 12 — Error Handling, from beginner level to practical examples.

# Error handling is an important Python concept, especially when building real-world applications, working with datasets, and developing Data Science projects.

# ## 1. What is Error Handling?

# Error handling is a way to manage errors that occur while a program is running, so the program can respond properly instead of terminating unexpectedly.

# Consider this example:

# ```
# num1 = 10num2 = 0result = num1 / num2print(result)
# ```

# Output:

# ```
# ZeroDivisionError: division by zero
# ```

# Python stops executing the program because dividing by zero is not allowed.

# We can handle this error using `try` and `except`.

# ## 2. Types of Errors in Python

# Before learning error handling, understand three common types of errors.

# ### A. Syntax Error

# Occurs when Python code violates its syntax rules.

# ```
# if 10 > 5    print("Greater")
# ```

# Error: Missing colon (`:`).

# ### B. Runtime Error (Exception)

# Occurs while the program is executing.

# ```
# num = 10 / 0
# ```

# Error: `ZeroDivisionError`.

# ### C. Logical Error

# The program executes, but produces an incorrect result.

# ```
# length = 10width = 5area = length + width  # Incorrect calculationprint(area)
# ```

# Expected area is 50, but the program produces 15.

# Note: try/except handles exceptions, but it does not automatically fix syntax or logical errors.

# ## 3. The `try` and `except` Blocks

# These are the main building blocks of error handling.

# - `try`: Contains code that might produce an exception.
# - `except`: Handles an exception if it occurs.

# Syntax:

# ```
# try:    # Risky codeexcept:    # Handle error
# ```

# Example:

# ```
# try:    num = int(input("Enter a number: "))    print("Your number:", num)except:    print("Something went wrong!")
# ```

# If the user enters `hello`, the program catches the error instead of crashing.

# ### Why avoid a bare `except`?

# A bare `except` catches almost every exception, including unexpected ones. It can hide programming mistakes.

# Prefer catching specific exceptions:

# ```
# except ValueError:    print("Invalid input")
# ```

# ## 4. Common Python Exceptions

# Learn these important exceptions.

# | Exception           | Meaning                       | Example                        |
# | ------------------- | ----------------------------- | ------------------------------ |
# | `ValueError`        | Invalid value                 | `int("hello")`                 |
# | `ZeroDivisionError` | Division by zero              | `10 / 0`                       |
# | `TypeError`         | Incorrect data type operation | `"5" + 5`                      |
# | `IndexError`        | Invalid list index            | `[1, 2][5]`                    |
# | `KeyError`          | Dictionary key doesn't exist  | `{"a": 1}["b"]`                |
# | `FileNotFoundError` | File doesn't exist            | Opening missing file           |
# | `NameError`         | Variable not defined          | `print(x)` when x is undefined |

# ### Example: ValueError

# ```
# try:    age = int(input("Enter your age: "))except ValueError:    print("Please enter a valid number!")
# ```

# ### Example: ZeroDivisionError

# ```
# try:    a = 10    b = 0    print(a / b)except ZeroDivisionError:    print("Cannot divide by zero!")
# ```

# ### Example: IndexError

# ```
# numbers = [10, 20, 30]try:    print(numbers[5])except IndexError:    print("Index does not exist!")
# ```

# ## 5. Multiple `except` Blocks

# Sometimes a program can produce different types of errors.

# We can handle each one separately.

# ```
# try:    num1 = int(input("Enter first number: "))    num2 = int(input("Enter second number: "))    result = num1 / num2    print("Result:", result)except ValueError:    print("Please enter numbers only!")except ZeroDivisionError:    print("Cannot divide by zero!")
# ```

# Dry run:

# | Input    | Result                    |
# | -------- | ------------------------- |
# | 10, 2    | 5.0                       |
# | 10, 0    | Cannot divide by zero     |
# | hello, 2 | Please enter numbers only |

# Important: Python executes the first matching `except` block and skips the remaining ones.

# ## 6. The `else` Block

# The `else` block runs only when the `try` block completes successfully without an exception.

# Syntax:

# ```
# try:    # Risky codeexcept:    # Error handlingelse:    # Runs if no error occurs
# ```

# Example:

# ```
# try:    num = int(input("Enter a number: "))except ValueError:    print("Invalid input!")else:    print("Your number is:", num)
# ```

# Dry run:

# Input: `25`

# ```
# Your number is: 25
# ```

# Input: `hello`

# ```
# Invalid input!
# ```

# Notice that `else` doesn't execute when an exception occurs.

# ## 7. The `finally` Block

# The `finally` block executes whether an exception occurs or not.

# It is commonly used for cleanup operations, such as closing files or releasing resources.

# Syntax:

# ```
# try:    # Risky codeexcept:    # Handle errorfinally:    # Always executes
# ```

# Example:

# ```
# try:    num = int(input("Enter a number: "))    print(num)except ValueError:    print("Invalid input!")finally:    print("Program execution completed.")
# ```

# If input is `10`:

# ```
# 10
# Program execution completed.
# ```

# If input is `hello`:

# ```
# Invalid input!
# Program execution completed.
# ```

# Both times, `finally` executes.

# ## 8. Understanding All Four Together

# This is the most important structure to remember.

# ```
# try:    num = int(input("Enter your age: "))except ValueError:    print("Invalid age!")else:    print("Your age is:", num)finally:    print("Age checking completed.")
# ```

# Execution flow

# TRY

# Execute risky code

# No error

# ELSE

# Runs after successful try

# Error

# EXCEPT

# Handles matching exception

# FINALLY

# Executes in either case

# Remember:

# - `try` → Try the code.
# - `except` → Handle the error.
# - `else` → Run if successful.
# - `finally` → Run at the end.

# ## 9. Raising Exceptions Using `raise`

# Sometimes you want to create an error yourself when a condition is not satisfied.

# This is called raising an exception.

# Syntax:

# ```
# raise ValueError("Error message")
# ```

# Example: Age validation.

# ```
# age = int(input("Enter your age: "))if age < 0:    raise ValueError("Age cannot be negative")print("Age:", age)
# ```

# If the user enters `-5`, Python raises a `ValueError`.

# ### Another example: Marks validation

# ```
# marks = int(input("Enter marks: "))if marks < 0 or marks > 100:    raise ValueError("Marks must be between 0 and 100")print("Valid marks:", marks)
# ```

# `raise` is useful when you want to enforce rules in your program.

# ## 10. Combining Everything — Safe Calculator

# Let's combine what we learned.

# ```
# try:    num1 = float(input("Enter first number: "))    num2 = float(input("Enter second number: "))    operator = input("Enter operator (+, -, *, /): ")    if operator == "+":        result = num1 + num2    elif operator == "-":        result = num1 - num2    elif operator == "*":        result = num1 * num2    elif operator == "/":        result = num1 / num2    else:        raise ValueError("Invalid operator")except ValueError as e:    print("Error:", e)except ZeroDivisionError:    print("Cannot divide by zero!")else:    print("Result:", result)finally:    print("Calculator closed.")
# ```

# Here we used:

# - `try` for potentially risky operations.
# - `except` for handling errors.
# - `raise` for invalid operators.
# - `as e` to access the exception message.
# - `else` to display the result only when successful.
# - `finally` to display the closing message.

# ## 11. Quick Revision Notes

# | Concept   | Purpose                                   |
# | --------- | ----------------------------------------- |
# | `try`     | Executes risky code                       |
# | `except`  | Handles exceptions                        |
# | `else`    | Runs when no exception occurs             |
# | `finally` | Executes at the end                       |
# | `raise`   | Manually raises an exception              |
# | `as e`    | Stores the exception object in a variable |

# ## 12. Practice Tasks — Day 12

# Now apply what you learned.

# Exercise 1 — Easy

# Safe Number Input

# - Take an integer from the user.
# - Handle invalid input using `ValueError`.
# - Print `"Valid number entered"` if successful.

# Exercise 2 — Easy

# Division Calculator

# - Take two numbers.
# - Divide the first by the second.
# - Handle `ValueError` and `ZeroDivisionError`.

# Exercise 3 — Intermediate

# Age Validator

# - Take the user's age.
# - Handle invalid input.
# - Use `else` to print valid age.
# - Use `finally` to print `"Age checking completed"`.

# Exercise 4 — Intermediate

# Marks Validator

# - Take marks as input.
# - Handle invalid input.
# - Raise `ValueError` if marks are below 0 or above 100.
# - Print `"Valid marks"` for marks within range.

# Exercise 5 — Challenge

# Safe Calculator

# Build a calculator supporting `+`, `-`, `*`, `/`.

# Requirements:

# - Handle invalid number inputs.
# - Handle division by zero.
# - Handle unsupported operators.
# - Use `finally` to print `"Calculator closed"`.

# ## 13. How This Helps in Data Science

# Error handling is especially useful when:

# - Reading CSV and Excel files that might not exist.
# - Converting dataset columns from strings to numbers.
# - Handling missing or invalid values.
# - Working with APIs that may fail.
# - Building applications using Streamlit or FastAPI.

let = 10 + 30
print(let)

