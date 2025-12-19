#Write a Python program using the sys module that accepts numbers as command-line arguments and prints their sum and average.

import sys                     # Import sys module to access command-line arguments

# Read numbers from command-line arguments (excluding script name)
# Convert each argument to integer and store in a list
NumberList = list(map(int, sys.argv[1:]))

# Calculate the sum of all numbers in the list
total = sum(NumberList)

# Calculate the average of the numbers
average = total / len(NumberList)

# Display the entered numbers
print("Numbers Entered :: ", NumberList)

# Display the sum of numbers
print("Sum of numbers ::", total)

# Display the average value
print("Average ::", average)
