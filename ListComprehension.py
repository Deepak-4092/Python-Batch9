# List comprehension
# A way to create a new list with less syntax
# Can mimic certain lambda functions
# Syntax:
# list = [expression for item in iterable]
# list = [expression for item in iterable if condition]
# list = [expression if/else for item in iterable]

# --------------------------------------------------

# Method 1: Using normal for loop
squares = []                 # create an empty list
for i in range(1, 11):       # create a for loop
    squares.append(i * i)    # square each number
print(squares)

# --------------------------------------------------

# Method 2: Using list comprehension
squares1 = [i ** 2 for i in range(1, 11)]
print(squares1)

# --------------------------------------------------

# Student marks example
students = [100, 90, 80, 70, 60, 50, 40, 30, 0]

# Using filter with lambda (commented in image)
# pass_students = list(filter(lambda x: x >= 60, students))

# Using list comprehension with condition
# pass_students = [i for i in students if i >= 60]

# Using list comprehension with if-else
pass_students = [i if i >= 60 else "Failed" for i in students]
print(pass_students)
