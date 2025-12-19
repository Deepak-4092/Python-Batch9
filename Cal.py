# Read two numbers from the user
n = int(input("Enter the first number: "))
m = int(input("Enter the second number: "))

# Function to perform calculation based on user choice
def cal(a, b):
    # Display menu for operations
    print("Choose operation: (1-Addition/2-Subtraction/3-Multiplication/4-Division)")
    
    # Read user's choice
    choice = int(input("Enter your choice: "))
    
    # Perform operation based on choice
    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        if b != 0:
            return a / b
        else:                           
            return "Error: Division by zero"
    else:
        return "Wrong input"

# Call the function and print the result
result = cal(n, m)
print("Result:", result)
